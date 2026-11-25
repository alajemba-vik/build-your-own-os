# Build your own operating system, with AI

A step-by-step tutorial from the **aivancity Tech Club**: build a tiny operating system from scratch,
on **macOS** or **Windows**, vibe-coding it with the AI of your choice.

**Start here: https://alajemba-vik.github.io/build-your-own-os/**

You go from an empty screen to a kernel with a console, interrupts, a keyboard driver, a shell,
a memory allocator and a small desktop with windows. It runs in QEMU, an emulated PC, so nothing on your computer changes.

| Folder | What's inside |
|---|---|
| `starter/` | Copy this to begin: a kernel that boots and says hello, a Makefile, and `AGENTS.md`, the brief your AI reads |
| `os/` | The finished reference OS (all chapters). Peek at it when you are stuck |
| `index.html`, `setup-*.html`, `chapter-*.html`, `assets/` | The tutorial website (GitHub Pages) |
| `tools/boot-test.sh` | Boots the OS in QEMU and checks the shell answers (run by GitHub Actions on Linux and macOS) |

```bash
git clone https://github.com/alajemba-vik/build-your-own-os.git
cp -R build-your-own-os/starter my-os
cd my-os
make run
```

Made for the Thursday build session of 26 November 2026. Licence: MIT.
