#!/bin/sh
# Boots a kernel in QEMU with no window, types a few commands through the serial port,
# and checks the answers. Used by GitHub Actions on Linux and macOS.
#   tools/boot-test.sh os        the finished OS: checks the boot log and the shell
#   tools/boot-test.sh starter   the starter: checks that it boots and keeps running
set -u
WHAT=${1:-os}
KERNEL="$WHAT/build/kernel.elf"
LOG="$WHAT/build/boot-test.log"
[ -f "$KERNEL" ] || { echo "No $KERNEL: run make -C $WHAT first"; exit 1; }

( sleep 4; printf '\nhelp\nabout\nmem\nalloc\necho testing 123\nuptime\nshutdown\n' ) |
  qemu-system-i386 -kernel "$KERNEL" -m 128M -no-reboot -display none -serial stdio \
    -device isa-debug-exit,iobase=0xf4,iosize=0x04 > "$LOG" 2>&1 &
PID=$!

i=0
while kill -0 "$PID" 2>/dev/null && [ "$i" -lt 45 ]; do sleep 1; i=$((i + 1)); done
RUNNING=no
if kill -0 "$PID" 2>/dev/null; then RUNNING=yes; kill "$PID" 2>/dev/null; fi
echo "----- serial output -----"; cat "$LOG"; echo "-------------------------"

if [ "$WHAT" = starter ]; then
  # the starter only draws on the screen, so we check QEMU loaded it and it did not crash
  [ "$RUNNING" = yes ] || { echo "FAIL: QEMU stopped (bad kernel or crash)"; exit 1; }
  if grep -qi "error" "$LOG"; then echo "FAIL: QEMU reported an error"; exit 1; fi
  echo "PASS: the starter boots and keeps running"; exit 0
fi

for want in "Welcome to" "[ OK ] GDT" "[ OK ] IDT" "[ OK ] Timer" "[ OK ] Keyboard" "MiB found" \
            "Commands:" "a tiny operating system" "Got a free page at" "testing 123" "Up for" "Shutting down"; do
  grep -qF "$want" "$LOG" || { echo "FAIL: expected to see \"$want\""; exit 1; }
done
echo "PASS: the OS boots and the shell answers"
