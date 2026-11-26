"""English text of the tutorial pages. The French version is content_fr.py: keep the two in step."""
from pagekit import REPO, SCREEN, DESKTOP, GET_STARTER


def build(s):
    # ---------------------------------------------------------------- index
    s.page("index", "Build your own operating system, with AI", f'''
    <p class="eyebrow">aivancity Tech Club · build session</p>
    <h1>Build your own <b>operating system</b></h1>
    <p class="lede">From a black screen to a shell and a desktop with windows. Written from scratch in C, vibe-coded with the AI of your choice, on a Mac or a Windows PC. Eight short chapters.</p>
    <div class="actions">
      <a class="btn btn-primary only-mac" href="setup-mac.html">Set up my Mac →</a>
      <a class="btn btn-primary only-win" href="setup-windows.html">Set up my Windows PC →</a>
      <a class="btn only-mac" href="setup-windows.html">I'm on Windows</a>
      <a class="btn only-win" href="setup-mac.html">I'm on a Mac</a>
    </div>
    {SCREEN.format(label="What your OS shows when it starts")}
    <p><small>This is what the finished OS shows when it starts. Everything on that screen is code you will write.</small></p>

    <div class="note thursday">
    <p><b>Thursday 26 November, 1:00–2:00 PM, AIClinic – Room 107.</b></p>
    <p><b>Before you come (15 minutes):</b> follow the setup for <a href="setup-mac.html">Mac</a> or <a href="setup-windows.html">Windows</a> until you see "Hello from my own operating system!". The downloads are big, so don't wait for the school Wi-Fi.<br>
    <b>In the room:</b> chapters 1 to 3, together. <b>At home:</b> chapters 4 to 8, at your own pace. Bring a laptop and a charger.</p>
    </div>

    <h2>What is an <b>operating system</b>?</h2>
    <p>It is the program that runs first and owns the computer: it talks to the hardware (screen, keyboard, memory, timer), it decides what runs when, and it gives other programs a simple way to use all of it. Windows, macOS, Linux, Android and iOS are operating systems. At its centre is the <b>kernel</b>, and that is what we build.</p>
    <p>When you press the power button, this is what happens. You will write the parts in bold:</p>
    <div class="chain" aria-label="The boot chain"><span>Power on</span><i>→</i><span>Firmware (BIOS)</span><i>→</i><span>Bootloader</span><i>→</i><span><b>boot.S</b></span><i>→</i><span><b>kernel_main()</b></span><i>→</i><span><b>drivers</b></span><i>→</i><span><b>your shell</b></span></div>

    <h2>Will it replace <b>Windows or macOS</b>?</h2>
    <p>No. Your OS runs inside <b>QEMU</b>, a free program that pretends to be a whole PC (an <i>emulator</i>). Nothing on your computer changes, and if your OS crashes you just close the window. It is a real OS all the same: the same code could start a real PC.</p>
    <p>We build for the classic 32-bit Intel PC (x86), because it is the best documented and the simplest to start. It runs the same on Intel Macs, Apple Silicon Macs (M1–M4) and Windows PCs.</p>

    <h2>How to <b>vibe-code</b> an OS</h2>
    <p>You describe what you want, the AI writes code, and you run it, read it and steer. An OS is a great place for this: the AI knows the hardware tricks, and you learn what each one does. Five rules that make it work:</p>
    <ol class="steps">
    <li><b>Give your AI the brief.</b> The starter comes with <a href="{REPO}/blob/main/starter/AGENTS.md"><code>AGENTS.md</code></a>: the rules of the project (32-bit, no C library, clang, QEMU…). Coding agents read it by themselves; with a chat AI, paste it first.</li>
    <li><b>One chapter, one step at a time.</b> Each chapter gives you a prompt. Don't ask for the whole OS at once: you would get something you can't fix.</li>
    <li><b>Ask why, not only what.</b> Every chapter has questions to ask. If you can't explain a line, ask until you can.</li>
    <li><b>Run it after every change</b> with <code>make run</code>. When it breaks, paste the full error to the AI.</li>
    <li><b>Save with Git</b> when something works. Stuck? Each chapter has the reference code from a finished OS to compare with.</li>
    </ol>

    <h2>Which <b>AI</b>?</h2>
    <div class="grid">
    <div class="card"><h3>Coding agents</h3><p>Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI. They read the files in your folder and <code>AGENTS.md</code>, edit the code and can run <code>make</code>. The easiest choice.</p></div>
    <div class="card"><h3>Chat AIs</h3><p>ChatGPT, Claude.ai, Gemini. Paste <code>AGENTS.md</code> at the start, then paste the files you want changed, and copy the answers back into your files.</p></div>
    <div class="card"><h3>No AI?</h3><p>That works too. Each chapter explains the idea, and the reference code is fully commented. Read it, then write it yourself.</p></div>
    </div>

    <h2>The <b>chapters</b></h2>
    <table>
    <thead><tr><th>#</th><th>You build</th><th>Time</th></tr></thead>
    <tbody>
    <tr><td>1</td><td><a href="chapter-1-boot.html">Boot and say hello</a>: the starter kernel, how a PC starts</td><td>20 min</td></tr>
    <tr><td>2</td><td><a href="chapter-2-console.html">A real console</a>: scrolling, colours, <code>kprintf</code>, the serial port</td><td>30 min</td></tr>
    <tr><td>3</td><td><a href="chapter-3-interrupts.html">Interrupts and crashes</a>: GDT, IDT, a kernel panic screen</td><td>40 min</td></tr>
    <tr><td>4</td><td><a href="chapter-4-keyboard.html">Timer and keyboard</a>: your first drivers</td><td>40 min</td></tr>
    <tr><td>5</td><td><a href="chapter-5-shell.html">A shell</a>: commands you can type</td><td>30 min</td></tr>
    <tr><td>6</td><td><a href="chapter-6-memory.html">Memory</a>: find the RAM, hand out pages</td><td>40 min</td></tr>
    <tr><td>7</td><td><a href="chapter-7-desktop.html">A desktop with windows</a>: move them with the arrow keys</td><td>40 min</td></tr>
    <tr><td>8</td><td><a href="chapter-8-make-it-yours.html">Make it yours and share it</a></td><td>as long as you like</td></tr>
    </tbody></table>
    <p>The whole finished OS is in the <a href="{REPO}">GitHub repository</a> (folder <code>os/</code>). Every change to it is built and started automatically on Linux and macOS, so we know the instructions work.</p>
    ''', "Build a tiny operating system from scratch, on macOS or Windows, vibe-coding it with the AI of your choice. An aivancity Tech Club tutorial.")

    # ---------------------------------------------------------------- setup mac
    s.page("setup-mac", "Set up a Mac", f'''
    <p class="eyebrow">Set up · about 15 minutes</p>
    <h1>Set up <b>your Mac</b></h1>
    <p class="lede">You need three things: the Apple developer tools (Git and make), a compiler that can build for a PC (LLVM's clang and lld), and QEMU to run your OS. Intel and Apple Silicon Macs both work.</p>
    <ol class="steps">
    <li><h3>Open Terminal</h3><p>Press <kbd>⌘</kbd> <kbd>Space</kbd>, type <b>Terminal</b>, press <kbd>Return</kbd>. Paste each command below and press <kbd>Return</kbd>.</p></li>
    <li><h3>Install the Apple developer tools</h3>{s.code("xcode-select --install")}<p>A window opens: click <b>Install</b>. If it says they are already installed, that's fine: go on.</p></li>
    <li><h3>Install Homebrew</h3><p>Homebrew installs developer tools with one command. Skip this if <code>brew --version</code> already works.</p>
    {s.code('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')}
    <p>It asks for your Mac password (nothing shows while you type: that's normal). <b>At the end it prints "Next steps" with two or three commands: run them</b>, then close Terminal and open it again.</p></li>
    <li><h3>Install the compiler and QEMU</h3>{s.code("brew install llvm lld qemu")}<p>This takes 5 to 10 minutes. <b>llvm</b> gives you <code>clang</code>, the C compiler, <b>lld</b> the linker that puts the pieces together, and <b>qemu</b> the emulated PC.</p></li>
    <li><h3>Check it worked</h3>{s.code('''
    "$(brew --prefix llvm)/bin/clang" --version
    ls "$(brew --prefix lld)/bin/ld.lld"
    qemu-system-i386 --version
    ''')}<p>Each line should print a version or a path, not "command not found" or "No such file".</p></li>
    <li><h3>Get the starter and run it</h3>{s.code(GET_STARTER)}
    <p>A QEMU window opens with <b>"Hello from my own operating system!"</b>. That is your OS. To stop it, close the window or press <kbd>Ctrl</kbd> <kbd>C</kbd> in Terminal.</p>
    <p>The first time, Git may ask who you are. Run these with your own name and email, then the commit again:</p>
    {s.code('git config --global user.name "Your Name"\ngit config --global user.email "you@example.com"')}</li>
    <li><h3>Open it with your AI</h3><p>Open the <code>my-os</code> folder in your editor or AI tool. For example:</p>
    {s.code('''
    code .        # VS Code (with Copilot), or: cursor .
    claude        # Claude Code, in the my-os folder
    codex         # Codex CLI, in the my-os folder
    ''')}<p>Using a chat AI instead? Open <code>my-os/AGENTS.md</code> (or <a href="{REPO}/blob/main/starter/AGENTS.md">read it on GitHub</a>), copy all of it and paste it as your first message.</p></li>
    </ol>
    <div class="note"><p><b>"command not found: brew"</b>: you missed the "Next steps" lines at the end of the Homebrew install. Run <code>eval "$(/opt/homebrew/bin/brew shellenv)"</code> (Apple Silicon) or <code>eval "$(/usr/local/bin/brew shellenv)"</code> (Intel), and add that line to <code>~/.zprofile</code>.</p>
    <p><b>The QEMU window doesn't show up</b>: look for it behind Terminal or in the Dock. Or run <code>make run-text</code> to see the screen inside Terminal (quit with <kbd>Esc</kbd> then <kbd>2</kbd>, type <code>quit</code>, <kbd>Return</kbd>).</p>
    <p>More fixes on the <a href="help.html">help page</a>.</p></div>
    ''', "Install clang, lld and QEMU on macOS with Homebrew, and boot the starter OS.")

    # ---------------------------------------------------------------- setup windows
    s.page("setup-windows", "Set up Windows", f'''
    <p class="eyebrow">Set up · about 20 minutes</p>
    <h1>Set up <b>your Windows PC</b></h1>
    <p class="lede">OS tools are easiest on Linux, and Windows can run Linux inside it with <b>WSL</b> (Windows Subsystem for Linux). You install Ubuntu once, then everything happens in its terminal. Windows 11 is best; Windows 10 works too.</p>
    <ol class="steps">
    <li><h3>Install WSL and Ubuntu</h3><p>Open the Start menu, type <b>PowerShell</b>, right-click it and choose <b>Run as administrator</b>. Then:</p>{s.code("wsl --install")}<p><b>Restart your PC</b> when it asks. Ubuntu opens by itself after the restart (or open <b>Ubuntu</b> from the Start menu). Choose a username and a password for Linux. Nothing shows while you type the password: that's normal. Remember it, you'll need it for <code>sudo</code>.</p></li>
    <li><h3>Install the compiler and QEMU</h3><p>In the <b>Ubuntu</b> window (not PowerShell):</p>{s.code("sudo apt update && sudo apt install -y clang lld make git qemu-system-x86 qemu-system-gui")}<p><b>clang</b> is the C compiler, <b>lld</b> the linker that puts the pieces together, <b>qemu</b> the emulated PC. This is the exact command our automatic test uses, so it works.</p></li>
    <li><h3>Check it worked</h3>{s.code('''
    clang --version
    ld.lld --version
    qemu-system-i386 --version
    ''')}</li>
    <li><h3>Get the starter and run it</h3><p>Stay in your Linux home folder (<code>cd ~</code>). Don't work in <code>/mnt/c/…</code>: it is much slower there.</p>{s.code(GET_STARTER)}
    <p>On Windows 11 a QEMU window opens with <b>"Hello from my own operating system!"</b>. That is your OS. To stop it, close the window or press <kbd>Ctrl</kbd> <kbd>C</kbd> in Ubuntu.</p>
    <p><b>No window (Windows 10)?</b> Run <code>make run-text</code>: the screen of your OS shows inside the Ubuntu window. Quit with <kbd>Esc</kbd> then <kbd>2</kbd>, type <code>quit</code>, <kbd>Enter</kbd>.</p>
    <p>The first time, Git may ask who you are. Run these with your own name and email, then the commit again:</p>
    {s.code('git config --global user.name "Your Name"\ngit config --global user.email "you@example.com"')}</li>
    <li><h3>Open it with your AI</h3><p><b>VS Code</b>: install it on Windows with the <b>WSL</b> extension, then in Ubuntu, in <code>my-os</code>, run <code>code .</code>. Cursor works the same way. Terminal AIs (Claude Code, Codex, Gemini CLI) install and run <b>inside Ubuntu</b>, in the <code>my-os</code> folder.</p>
    {s.code('''
    code .        # VS Code (with Copilot) through WSL
    claude        # Claude Code, in the my-os folder
    ''')}<p>Using a chat AI instead? Open <code>my-os/AGENTS.md</code> (in VS Code, with <code>cat AGENTS.md</code>, or <a href="{REPO}/blob/main/starter/AGENTS.md">on GitHub</a>), copy all of it and paste it as your first message.</p></li>
    </ol>
    <div class="note"><p><b>"Please enable the Virtual Machine Platform" or error 0x80370102</b>: virtualization is off. Turn on <b>Virtualization</b> (Intel VT-x / AMD-V / SVM) in your PC's BIOS settings, then run <code>wsl --install</code> again.</p>
    <p><b>wsl --install only shows help text</b>: WSL is already there. Run <code>wsl --install -d Ubuntu</code>, then <code>wsl --update</code>.</p>
    <p>More fixes on the <a href="help.html">help page</a>.</p></div>
    ''', "Install WSL, Ubuntu, clang, lld and QEMU on Windows, and boot the starter OS.")

    # ---------------------------------------------------------------- chapter 1
    s.page("ch1", "Chapter 1: Boot and say hello", f'''
    <p class="eyebrow">Chapter 1 · about 20 minutes</p>
    <h1>Boot and <b>say hello</b></h1>
    <p class="lede">Your starter already boots. In this chapter you find out exactly how, line by line, with your AI, and you make the first screen your own.</p>

    <h2>The <b>idea</b></h2>
    <p>A PC starts its firmware (the BIOS), which loads a <b>bootloader</b>. Our bootloader is built into QEMU: <code>qemu-system-i386 -kernel build/kernel.elf</code>. It follows a standard called <b>Multiboot</b>: it looks for a magic number, <code>0x1BADB002</code>, at the start of our file, loads the kernel at 1 MiB in memory and jumps into it, with the CPU already in 32-bit mode.</p>
    <p>From there, it's all ours:</p>
    <ul>
    <li><code>src/boot.S</code> (assembly) holds the magic number, sets up a <b>stack</b> (memory C needs for its variables) and calls <code>kernel_main</code>.</li>
    <li><code>linker.ld</code> says where each piece of the kernel goes in memory.</li>
    <li><code>src/kernel.c</code> writes to the screen. In text mode the screen <i>is</i> memory: 80 × 25 cells starting at address <code>0xB8000</code>, 2 bytes each (the character, then its colour). Write there, and letters appear.</li>
    <li><code>Makefile</code> builds it with <code>--target=i686-elf -ffreestanding</code>: code for a bare 32-bit PC, with no operating system and no C library under it. We <i>are</i> the operating system.</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>Run it</h3>{s.code("make run")}<p>You see the hello message. Close QEMU.</p></li>
    <li><h3>Let your AI explain it</h3>{s.prompt('''
    Read AGENTS.md and every file in this project. Explain in simple words what happens from the moment QEMU starts until "Hello" appears on the screen. Go file by file: Makefile, linker.ld, src/boot.S, src/kernel.c. For boot.S, explain each line.''')}
    <p>Then ask about anything you don't get. Good questions:</p>
    <ul><li>Why does the stack start at the top and grow down?</li><li>What would happen if <code>kernel_main</code> returned?</li><li>What is in the colour byte <code>0x0B</code>?</li><li>Why can't I use <code>printf</code> here?</li></ul></li>
    <li><h3>Make it yours</h3>{s.prompt('''
    Change the first screen: show my name instead of "my own operating system", draw a border around the whole screen with the box-drawing characters of the VGA font (code page 437), and use at least three colours. Explain how the colour byte works (text colour, background colour). Keep everything in kernel.c.''')}
    {s.code("make run")}</li>
    <li><h3>Break it on purpose</h3><p>In <code>boot.S</code>, change <code>0x1BADB002</code> to another number and run <code>make run</code>. QEMU refuses to start it: no magic number, no boot. Put it back.</p></li>
    </ol>

    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>QEMU shows your name, a border and several colours.</li><li>You can say what <code>boot.S</code>, <code>linker.ld</code> and <code>0xB8000</code> are for.</li></ul>
    {s.ref(["starter/src/boot.S", "starter/linker.ld", "starter/src/kernel.c", "starter/Makefile"], "The starter files")}
    {s.save("Chapter 1: my own first screen")}
    ''', "How a PC boots, the multiboot header, and writing to the VGA screen.")

    # ---------------------------------------------------------------- chapter 2
    s.page("ch2", "Chapter 2: A real console", f'''
    <p class="eyebrow">Chapter 2 · about 30 minutes</p>
    <h1>A real <b>console</b></h1>
    <p class="lede">Writing letters at fixed places gets old fast. You build a console like a terminal's: a cursor, new lines, scrolling, colours, and your own <code>printf</code>. And a second output, the serial port, that shows up in your terminal and makes debugging much easier.</p>

    <h2>The <b>idea</b></h2>
    <ul>
    <li>The console remembers a <b>row and column</b>. Each character goes there and moves the cursor on. <code>\\n</code> goes to the next row.</li>
    <li>When the last row is full, you <b>scroll</b>: copy every row one up and clear the bottom one.</li>
    <li>The blinking cursor is moved by talking to the VGA chip through <b>I/O ports</b> <code>0x3D4</code> and <code>0x3D5</code>. Ports are a second address space for hardware, used with the <code>outb</code> and <code>inb</code> instructions.</li>
    <li><b>kprintf</b> is our <code>printf</code> (the k is for kernel). It uses <code>stdarg.h</code>, which the compiler gives us even without a C library.</li>
    <li>The <b>serial port</b> (COM1, port <code>0x3F8</code>) sends bytes one by one. <code>make run</code> connects it to your terminal, so every line your OS prints also appears there, and you can copy it into your AI.</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>Build the console</h3>{s.prompt('''
    Chapter 2. Create src/io.h with outb/inb/outw helpers (inline assembly). Then src/console.c and src/console.h: a text console on the VGA screen with a cursor position, newline, backspace, tab, scrolling when the screen is full, colours (an enum of the 16 VGA colours) and moving the blinking hardware cursor.

    Add src/serial.c for COM1 (0x3F8) so every character printed on the console is also sent to the serial port (send \\r before \\n).

    Add src/printf.c with kprintf supporting %s %c %d %u %x %p %%, a width like %5d, zero padding like %02u, and left alignment like %-10s. Also a ksnprintf that writes into a buffer. And src/string.c with memset, memcpy, memmove, strlen, strcmp, strncmp, because we have no C library.

    Update kernel_main to clear the screen, print a coloured title, a few lines with numbers (negative, hex), then 30 numbered lines to test scrolling.''')}
    {s.code("make run")}</li>
    <li><h3>Understand it</h3><p>Ask your AI:</p><ul><li>How does <code>va_list</code> work when there is no C library?</li><li>Why do we write <code>volatile</code> for the screen memory?</li><li>Why might the compiler call <code>memset</code> even if I never wrote it?</li></ul></li>
    <li><h3>Make it yours</h3><p>Print a coloured ASCII-art logo with your OS's name when it starts. Ask your AI to make one (keep it under 7 lines and 60 columns), and to escape the backslashes.</p></li>
    </ol>

    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>The 30 lines scroll and the last ones are visible.</li><li><code>kprintf("%d %x %05u", -42, 255, 7)</code> prints <code>-42 ff 00007</code>.</li><li>The same text appears in your terminal (the serial port).</li></ul>
    <div class="note"><p><b>"undefined symbol: memset"</b> (or memcpy): the compiler uses them for big copies, and we have no C library. Make sure <code>string.c</code> exists and is built.</p><p><b>Strange symbols instead of letters</b>: each screen cell is <code>character | (colour &lt;&lt; 8)</code>. Check the character is cast to <code>uint8_t</code> first.</p></div>
    {s.ref(["os/src/io.h", "os/src/console.h", "os/src/console.c", "os/src/serial.c", "os/src/printf.c", "os/src/string.c"])}
    {s.save("Chapter 2: console, kprintf and serial port")}
    ''', "A VGA text console with scrolling and colours, kprintf, and the serial port.")

    # ---------------------------------------------------------------- chapter 3
    s.page("ch3", "Chapter 3: Interrupts and crashes", f'''
    <p class="eyebrow">Chapter 3 · about 40 minutes</p>
    <h1>Interrupts <b>and crashes</b></h1>
    <p class="lede">Right now, if your code does something wrong, the PC silently restarts. You teach the CPU where to go when something happens, and you get a proper red <b>kernel panic</b> screen that says what went wrong.</p>

    <h2>The <b>idea</b></h2>
    <ul>
    <li>An <b>interrupt</b> makes the CPU drop what it's doing and run a handler, then come back. Some come from the CPU itself when code goes wrong (<b>exceptions</b>: division by zero, invalid instruction, page fault… numbers 0 to 31). Others come from hardware like the keyboard (chapter 4).</li>
    <li>The <b>IDT</b> (Interrupt Descriptor Table) is a list of 256 handler addresses. We load it with the <code>lidt</code> instruction.</li>
    <li>Before that, the CPU wants a <b>GDT</b> (Global Descriptor Table): old x86 chips cut memory into segments. We make two segments that both cover all 4 GiB (code at <code>0x08</code>, data at <code>0x10</code>), and then never think about them again.</li>
    <li>Handlers start in assembly (<b>stubs</b>): they save every register, call one C function with a pointer to them, then restore everything and run <code>iret</code>. Some exceptions push an error code and some don't; the stubs push a fake 0 so every interrupt looks the same.</li>
    <li>If a crash happens while handling a crash, the CPU gives up: a <b>triple fault</b>. QEMU stops (we use <code>-no-reboot</code>).</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>GDT, IDT and the panic screen</h3>{s.prompt('''
    Chapter 3. Add a flat GDT with three entries (null, kernel code 0x08, kernel data 0x10, both covering 4 GiB) in src/gdt.c, loaded by an assembly function gdt_flush in src/cpu.S that reloads all segment registers and does a far jump to reload CS.

    Then an IDT in src/idt.c with 48 entries pointing to assembly stubs isr0..isr47 in cpu.S. Each stub pushes a fake error code 0 when the CPU doesn't push one (the CPU pushes one for 8, 10-14, 17, 21, 29, 30), pushes its number, and jumps to a common stub that saves all registers (pushal and the segment registers), loads the kernel data segment, and calls isr_handler(struct regs *r) in C. Put a table of the 48 stub addresses in cpu.S. Define struct regs in src/cpu.h in the exact order things are on the stack.

    Also remap the PIC so hardware IRQs 0-15 use interrupts 32-47, but keep them all masked for now.

    For exceptions 0-31, show a red KERNEL PANIC screen with the exception's name, the error code, eip and the registers, then stop the CPU forever. In kernel_main, print "[ OK ]" lines after each step.''')}
    {s.code("make run")}</li>
    <li><h3>Crash it on purpose</h3>{s.prompt('''
    Add a temporary test at the end of kernel_main that runs the ud2 instruction (inline assembly), so I can see the panic screen. Explain what "Invalid opcode" means.''')}<p>You should see the red screen with <b>Invalid opcode</b>. Then try a division by zero (ask the AI how to make one the compiler doesn't remove), then delete the test.</p></li>
    <li><h3>Understand it</h3><p>Ask your AI: What exactly does the CPU push on the stack when an interrupt happens? Why must <code>struct regs</code> match the stub's pushes exactly? What is <code>iret</code>? Why does the PIC need to be remapped?</p></li>
    </ol>

    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>The boot shows <code>[ OK ] GDT</code> and <code>[ OK ] IDT</code>.</li><li><code>ud2</code> gives a red panic screen with "Invalid opcode" and QEMU stays open.</li></ul>
    <div class="note"><p><b>QEMU closes as soon as it starts</b>: a triple fault. Run this and paste the end of it to your AI, it shows the last interrupts and why the CPU reset:</p>
    {s.code("qemu-system-i386 -kernel build/kernel.elf -no-reboot -d int,cpu_reset 2>&1 | tail -40")}
    <p>The usual causes: a stub with the wrong error-code setting, <code>struct regs</code> in the wrong order, a missing <code>__attribute__((packed))</code> on the table structs, or the far jump in <code>gdt_flush</code>.</p></div>
    {s.ref(["os/src/cpu.S", "os/src/cpu.h", "os/src/gdt.c", "os/src/idt.c", "os/src/panic.c"])}
    {s.save("Chapter 3: GDT, IDT and kernel panic screen")}
    ''', "The GDT, the IDT, interrupt stubs in assembly and a kernel panic screen.")

    # ---------------------------------------------------------------- chapter 4
    s.page("ch4", "Chapter 4: Timer and keyboard", f'''
    <p class="eyebrow">Chapter 4 · about 40 minutes</p>
    <h1>Timer and <b>keyboard</b></h1>
    <p class="lede">Your first two <b>drivers</b>. The timer lets your OS count time; the keyboard lets you type. After this chapter, your OS reacts to you.</p>

    <h2>The <b>idea</b></h2>
    <ul>
    <li>Hardware raises <b>IRQs</b> (interrupt requests). The <b>PIC</b> chip collects them and passes them to the CPU as interrupts 32–47 (we moved them there in chapter 3). After each one, we must send the PIC an <b>End Of Interrupt</b>, or it never sends another.</li>
    <li>The <b>PIT</b> timer counts at 1,193,182 Hz. Divide that by 100 and it raises IRQ 0 a hundred times a second. Each one is a <b>tick</b>.</li>
    <li>The keyboard raises IRQ 1 for each key pressed or released. We read a <b>scancode</b> from port <code>0x60</code>: a number for the key's position, not a letter. We turn it into a letter with a table, and track Shift ourselves.</li>
    <li>Keys wait in a small <b>ring buffer</b> (a queue that wraps around) until someone reads them.</li>
    <li><code>sti</code> turns interrupts on. <code>hlt</code> sleeps until the next interrupt: no wasted CPU while waiting for a key.</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>The timer</h3>{s.prompt('''
    Chapter 4, part 1. Add irq_install(irq, handler) in idt.c: it stores the handler and unmasks that IRQ in the PIC. In isr_handler, for interrupts 32-47 call the handler and send End Of Interrupt (to both PICs for IRQ 8-15). Ignore spurious IRQ 7 and 15.

    Then src/timer.c and timer.h: program the PIT channel 0 to 100 Hz, count ticks on IRQ 0, and add timer_ticks(), uptime_seconds() and timer_sleep_ms(). Turn interrupts on with sti at the end of kernel_main, then print the uptime once a second as a test.''')}
    {s.code("make run")}</li>
    <li><h3>The keyboard</h3>{s.prompt('''
    Chapter 4, part 2. Add src/keyboard.c and keyboard.h: on IRQ 1 read the scancode from port 0x60, ignore key releases (except to track Shift), translate scancode set 1 to characters with two tables for a US QWERTY layout (normal and shifted), handle Caps Lock, and turn the arrow keys (0xE0 prefix) into special codes KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT. Put keys in a 64-byte ring buffer.

    Add input_poll() that returns the next key or -1, and input_getc() that waits for a key with hlt. Both should also accept characters typed in the serial terminal (\\r means Enter, 0x7F means Backspace). Replace the uptime test with a loop that prints every key I type.''')}
    {s.code("make run")}<p>Click inside the QEMU window, then type.</p></li>
    <li><h3>Understand it</h3><p>Ask your AI: What happens if I forget the End Of Interrupt? Why is the variable that counts ticks <code>volatile</code>? Why do the arrow keys send two bytes?</p></li>
    </ol>
    <div class="note idea"><p><b>On an AZERTY keyboard</b>, letters come out in QWERTY places (A gives Q). That's expected: scancodes are key <i>positions</i>. A nice challenge: ask your AI to add a French AZERTY table and a way to switch.</p></div>
    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>The boot shows <code>[ OK ] Timer</code> and <code>[ OK ] Keyboard</code>.</li><li>What you type appears, with capitals when you hold Shift.</li><li>Your terminal shows the same text, and typing in the terminal works too.</li></ul>
    <div class="note"><p><b>Nothing happens when I type</b>: did you call <code>sti</code>? Is IRQ 1 unmasked? Do you send End Of Interrupt after <i>every</i> IRQ, including the timer's? If the timer works only once, it's the End Of Interrupt.</p></div>
    {s.ref(["os/src/timer.h", "os/src/timer.c", "os/src/keyboard.h", "os/src/keyboard.c", "os/src/idt.c"])}
    {s.save("Chapter 4: timer and keyboard drivers")}
    ''', "IRQs, the PIC, the PIT timer and a PS/2 keyboard driver.")

    # ---------------------------------------------------------------- chapter 5
    s.page("ch5", "Chapter 5: A shell", f'''
    <p class="eyebrow">Chapter 5 · about 30 minutes</p>
    <h1>A <b>shell</b></h1>
    <p class="lede">The part people actually use: a prompt where you type commands and your OS answers. You have all the pieces; now you put them together.</p>

    <h2>The <b>idea</b></h2>
    <p>A shell is a loop: <b>show a prompt → read a line → split it into a command and its arguments → find the command → run it</b>. A table of <code>{{name, help text, function}}</code> makes adding commands easy: one line each.</p>
    <p>Turning the computer off or restarting it is hardware too: QEMU turns off when you write <code>0x2000</code> to port <code>0x604</code>, and every PC restarts when you send <code>0xFE</code> to the keyboard controller on port <code>0x64</code>.</p>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>The shell</h3>{s.prompt('''
    Chapter 5. Write src/shell.c and shell.h with shell_run(): show a coloured prompt with the OS name, read a line with input_getc (support Backspace, ignore other control keys, max 127 characters, echo what is typed), split the command from its arguments, and look it up in a table of commands {name, help text, function}.

    Commands: help (lists all commands with their help text, aligned), clear, echo <text>, about (OS name, version, uptime), uptime (hh:mm:ss), color <name> (changes the text colour), reboot (keyboard controller, 0xFE on port 0x64), shutdown (outw(0x604, 0x2000) for QEMU, then halt) and crash (runs ud2 to show the panic screen). Unknown commands print a short message.

    Put the OS name and version in src/os.h. kernel_main calls shell_run() after setting everything up.''')}
    {s.code("make run")}<p>Type <code>help</code>, then try every command.</p></li>
    <li><h3>Invent your own commands</h3><p>Pick one or two, and ask your AI for them one at a time:</p>
    <ul><li><b>calc 12 * 7</b>: a calculator for whole numbers.</li><li><b>Command history</b> with the up arrow.</li><li><b>guess</b>: guess-the-number, using the timer ticks as randomness.</li><li><b>banner hello</b>: big letters.</li><li><b>time</b>: the real date and time from the PC's clock chip (the CMOS RTC, ports <code>0x70</code>/<code>0x71</code>).</li></ul></li>
    </ol>
    <h2>It works <b>when</b></h2>
    <ul class="checks"><li><code>help</code> lists your commands and each one works.</li><li><code>shutdown</code> closes QEMU; <code>crash</code> shows the panic screen.</li><li>You added at least one command of your own.</li></ul>
    {s.ref(["os/src/shell.c", "os/src/os.h", "os/src/kernel.c"])}
    {s.save("Chapter 5: a shell with commands")}
    ''', "A command shell with a command table, reboot and shutdown.")

    # ---------------------------------------------------------------- chapter 6
    s.page("ch6", "Chapter 6: Memory", f'''
    <p class="eyebrow">Chapter 6 · about 40 minutes</p>
    <h1><b>Memory</b></h1>
    <p class="lede">Programs need memory, and the OS is the one that hands it out. You find out how much RAM the PC has, which parts are free, and you write an allocator that gives out pieces of it.</p>

    <h2>The <b>idea</b></h2>
    <ul>
    <li>Not all addresses are RAM you can use: the first megabyte holds the BIOS and the screen, some areas belong to hardware, and your kernel itself sits at 1 MiB. The bootloader gives us a <b>memory map</b>: a list of areas, each marked usable (type 1) or not. <code>boot.S</code> already passes it to <code>kernel_main</code>.</li>
    <li>We cut memory into <b>pages</b> of 4 KiB and keep a <b>bitmap</b>: one bit per page, 1 = used, 0 = free. 128 MiB is 32,768 pages, so the whole bitmap fits in 4 KiB.</li>
    <li><code>linker.ld</code> defines <code>kernel_end</code>, the first address after our kernel, so we never hand out our own code.</li>
    <li>For small objects we add a <b>heap</b> with <code>kmalloc</code>. The simplest one just gives the next free bytes and never takes them back. Real ones do better; that can be your challenge.</li>
    <li>Careful: dividing 64-bit numbers on a 32-bit CPU needs a helper library we don't have. Use shifts (<code>&gt;&gt; 12</code> is "divide by 4096").</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>The page allocator</h3>{s.prompt('''
    Chapter 6. kernel_main receives the multiboot magic and a pointer to the multiboot info. Write src/memory.c and memory.h: define struct multiboot_info and the memory map entry struct (packed). In memory_init: mark every page used, then free the pages of every area of type 1 in the memory map (flag bit 6; fall back to mem_upper if there is no map), then mark the first 1 MiB and the kernel (up to the kernel_end symbol from linker.ld) as used again. Use a bitmap with one bit per 4 KiB page, for up to 512 MiB. Don't use 64-bit division.

    Add page_alloc() (returns the address of a free page, or 0), page_free(), pages_total() and pages_used(). Add a bump kmalloc from a 64 KiB static heap, 16-byte aligned. Print "[ OK ] Memory: N MiB found" at boot, and add shell commands mem (totals) and alloc (takes one page and prints its address).''')}
    {s.code("make run")}<p>Run <code>mem</code>, then <code>alloc</code> a few times.</p></li>
    <li><h3>Play with it</h3><p>In the <code>Makefile</code>, change <code>-m 128M</code> to <code>-m 256M</code> and run again: <code>mem</code> should follow. Ask your AI to add a <code>memmap</code> command that lists every area of the memory map with its type.</p></li>
    <li><h3>Understand it</h3><p>Ask your AI: What is in the first megabyte? Why are pages 4 KiB? What would <b>paging</b> add (the next big step in a real OS)?</p></li>
    </ol>
    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>The boot shows about <code>127 MiB found</code> with <code>-m 128M</code>.</li><li><code>alloc</code> gives a new address each time, above where your kernel ends.</li></ul>
    <div class="note"><p><b>"undefined symbol: __udivdi3"</b> (or <code>__umoddi3</code>): a 64-bit division slipped in. Replace it with a shift, or convert to 32-bit first.</p></div>
    {s.ref(["os/src/memory.h", "os/src/memory.c", "os/linker.ld"])}
    {s.save("Chapter 6: memory map, page allocator and kmalloc")}
    ''', "The multiboot memory map, a bitmap page allocator and a simple kmalloc.")

    # ---------------------------------------------------------------- chapter 7
    s.page("ch7", "Chapter 7: A desktop with windows", f'''
    <p class="eyebrow">Chapter 7 · about 40 minutes</p>
    <h1>A desktop <b>with windows</b></h1>
    <p class="lede">The fun one. A desktop with a top bar, a clock and two windows you can move around, all drawn with text characters, like the first versions of many famous operating systems.</p>
    {DESKTOP.format(label="The desktop: a textured blue background, a top bar, and two windows")}
    <p><small>A shortened sketch of the real thing.</small></p>

    <h2>The <b>idea</b></h2>
    <ul>
    <li>The VGA font (code page 437) has <b>box-drawing characters</b>: <code>0xC9</code> is ╔, <code>0xCD</code> is ═, <code>0xB0</code> is ░… Enough to draw windows.</li>
    <li><b>Double buffering</b>: draw the whole picture in an array first, then copy it to <code>0xB8000</code> in one go. Drawing straight on the screen would flicker.</li>
    <li>An <b>event loop</b>: check for a key without waiting (<code>input_poll</code>), update the state (which window is active, where it is), redraw, and sleep with <code>hlt</code> when there's nothing to do. Redraw a few times a second so the clock moves.</li>
    <li>Draw the inactive window first and the active one last, so it's on top.</li>
    </ul>

    <h2>Do <b>it</b></h2>
    <ol class="steps">
    <li><h3>The desktop</h3>{s.prompt('''
    Chapter 7. Add src/desktop.c with desktop_run(), started by a new shell command "desktop". Draw into a uint16_t buffer the size of the screen, then copy it to VGA memory in one go. Save the screen before and restore it when leaving.

    Draw: a textured background (character 0xB0), a top bar with the OS name on the left and the uptime on the right, a bottom bar with the keys, and two windows with a shadow. Use double box-drawing lines and a cyan title for the active window, single lines for the other. One window shows a welcome text, the other live system info: uptime, memory, free pages and the number of keys pressed. Add keyboard_presses() to keyboard.c for that.

    Keys: Tab switches the active window, arrow keys or WASD move it (keep it on the screen), Esc goes back to the shell. Use input_poll and redraw on every key and 4 times a second, sleep with hlt otherwise. Hide the blinking cursor while the desktop is open.''')}
    {s.code("make run")}<p>Type <code>desktop</code>. Press <kbd>Tab</kbd>, move the windows with the arrow keys, <kbd>Esc</kbd> to go back.</p></li>
    <li><h3>Make it yours</h3><p>Ask for one change at a time: your own colours, a third window (a clock, a notepad, a to-do list), a "start menu" on a key, or a tiny game inside a window. <b>Snake</b> fits nicely: it only needs the arrow keys, the timer and the screen.</p></li>
    </ol>
    <div class="note"><p><b>Using <code>make run-serial</code>?</b> The desktop is drawn on the screen, not sent to the serial port, so you won't see it there. Use <code>make run</code> or <code>make run-text</code>.</p></div>
    <h2>It works <b>when</b></h2>
    <ul class="checks"><li>The clock in the top bar moves by itself.</li><li>Tab and the arrow keys work, and windows stay on the screen.</li><li>Esc brings back the shell exactly as it was.</li></ul>
    {s.ref(["os/src/desktop.c", "os/src/shell.h"])}
    {s.save("Chapter 7: a text-mode desktop with windows")}
    ''', "A text-mode desktop with movable windows, double buffering and an event loop.")

    # ---------------------------------------------------------------- chapter 8
    s.page("ch8", "Chapter 8: Make it yours and share it", f'''
    <p class="eyebrow">Chapter 8 · as long as you like</p>
    <h1>Make it yours <b>and share it</b></h1>
    <p class="lede">You have a working operating system: a boot process, drivers, a crash screen, a shell, a memory allocator and a desktop. Now give it a name, add the feature you want, and show it to the club.</p>

    <h2>Give it <b>a name</b></h2>
    <p>Change <code>OS_NAME</code> in <code>src/os.h</code>, and ask your AI for a new ASCII-art logo with that name.</p>

    <h2>Ideas, <b>easy to hard</b></h2>
    <table>
    <thead><tr><th>Idea</th><th>What you learn</th></tr></thead>
    <tbody>
    <tr><td><b>Themes</b>: a <code>theme</code> command that recolours the shell and the desktop</td><td>VGA colours</td></tr>
    <tr><td><b>Real date and time</b> from the PC's clock chip, in the top bar</td><td>The CMOS RTC (ports 0x70/0x71)</td></tr>
    <tr><td><b>AZERTY</b> keyboard, and a <code>layout</code> command</td><td>Scancodes</td></tr>
    <tr><td><b>A game</b>: snake, pong, or 2048 in a window</td><td>Game loop, timer, randomness</td></tr>
    <tr><td><b>A notepad</b> that keeps notes while the OS runs</td><td><code>kmalloc</code>, strings</td></tr>
    <tr><td><b>Sound</b>: a beep at boot from the PC speaker (run QEMU with <code>-audiodev</code> and <code>-machine pcspk-audiodev=…</code>)</td><td>PIT channel 2</td></tr>
    <tr><td><b>A better heap</b> with <code>kfree</code></td><td>Free lists, fragmentation</td></tr>
    <tr><td><b>Paging</b>: give the kernel its own view of memory</td><td>Page tables, CR3, page faults</td></tr>
    <tr><td><b>Multitasking</b>: two tasks taking turns on the timer</td><td>Context switches, scheduling</td></tr>
    <tr><td><b>Graphics mode</b>: pixels instead of characters</td><td>Framebuffers (bootloaders like GRUB or Limine)</td></tr>
    </tbody></table>
    {s.prompt('''
    I finished the 8 chapters of the tutorial. I want to add: [YOUR IDEA]. First explain how it works on real PC hardware and which parts of my OS need to change. Then break it into 3 to 5 small steps I can test one by one, and do only the first step.''')}
    <p>When you outgrow this, the <a href="https://wiki.osdev.org/Expanded_Main_Page">OSDev wiki</a> is the place real hobby-OS builders learn from. Projects like SerenityOS started exactly where you are now.</p>

    <h2>Put it <b>on GitHub</b></h2>
    <p>With the GitHub CLI (<span class="only-mac"><code>brew install gh</code></span><span class="only-win"><code>sudo apt install gh</code></span>, then <code>gh auth login</code>), in your <code>my-os</code> folder:</p>
    {s.code('gh repo create my-os --public --source . --push')}
    <p>Or create an empty repository on github.com and follow its "push an existing repository" steps. Then take a screenshot of your desktop and add it to your <code>README.md</code>.</p>

    <h2>Show it to <b>the club</b></h2>
    <ul>
    <li>Bring it to a Thursday session and show it. Two minutes is enough: what you added, and what was hard.</li>
    <li>Post your screenshot and repository link in the club's WhatsApp group.</li>
    <li>Want it on the club website? Ask an organizer to add it to the <a href="https://aivancity-tech-club.github.io/showcase">student apps showcase</a>.</li>
    </ul>
    ''', "Ideas to extend your OS, from themes to multitasking, and how to share it.")

    # ---------------------------------------------------------------- help
    s.page("help", "Stuck? Help and glossary", f'''
    <p class="eyebrow">Help</p>
    <h1>Stuck? <b>Start here</b></h1>
    <p class="lede">Almost every problem is in the table below. If not, ask your AI the right way, or ask in the room.</p>

    <h2>Ask your AI <b>the right way</b></h2>
    {s.prompt('''
    I'm on chapter [N] of the build-your-own-OS tutorial (32-bit x86, multiboot, clang + ld.lld, QEMU, no C library: see AGENTS.md).
    I changed: [WHICH FILES, WHAT].
    I ran: [THE COMMAND].
    I expected: [WHAT SHOULD HAPPEN].
    Instead I see: [WHAT HAPPENS, AND THE FULL ERROR OR THE LAST LINES OF OUTPUT].
    Explain what the error means first, then give me the smallest fix.''')}
    <p>The full error matters: paste everything from the first red line. For crashes, paste the panic screen or the output of the <code>-d int,cpu_reset</code> command below.</p>

    <h2>Common <b>problems</b></h2>
    <table>
    <thead><tr><th>You see</th><th>What it means and what to do</th></tr></thead>
    <tbody>
    <tr><td><code>clang: command not found</code> or <code>ld.lld: No such file</code></td><td>The tools aren't installed or not found. Mac: <code>brew install llvm lld</code>. Windows: run the <code>sudo apt install …</code> line from the setup in Ubuntu. Check you are in the Ubuntu window, not PowerShell.</td></tr>
    <tr><td>Errors about <code>i686-elf</code> or <code>ld.lld</code> on a Mac</td><td>Apple's own clang is probably being used. Run <code>brew install llvm lld</code>; the Makefile then finds Homebrew's version by itself.</td></tr>
    <tr><td><code>make: *** No targets specified</code> or <code>No rule to make target</code></td><td>You are not in your OS folder. Run <code>cd ~/my-os</code>.</td></tr>
    <tr><td><code>undefined symbol: memset</code> / <code>memcpy</code></td><td>The compiler uses them for big copies. Write them in <code>src/string.c</code> (chapter 2).</td></tr>
    <tr><td><code>undefined symbol: __udivdi3</code> / <code>__umoddi3</code></td><td>A 64-bit division or <code>%</code>. Use a shift, or 32-bit numbers.</td></tr>
    <tr><td><code>fatal error: 'stdio.h' file not found</code></td><td>There is no C library in a kernel. Use your own <code>kprintf</code>. Only <code>stdint.h</code>, <code>stddef.h</code>, <code>stdbool.h</code> and <code>stdarg.h</code> exist.</td></tr>
    <tr><td>QEMU says <code>Error loading uncompressed kernel without PVH ELF Note</code></td><td>QEMU didn't find the multiboot header. Check <code>.multiboot</code> comes first in <code>linker.ld</code>, the magic number is right, and you built for <code>i686</code> (32-bit).</td></tr>
    <tr><td>QEMU opens and closes right away</td><td>A triple fault (a crash while handling a crash). See below.</td></tr>
    <tr><td>Typing does nothing</td><td>Click inside the QEMU window first. Then check <code>sti</code>, that IRQ 1 is unmasked, and the End Of Interrupt (chapter 4).</td></tr>
    <tr><td>Letters are in the wrong places</td><td>Your keyboard is AZERTY and the table is QWERTY. Expected; see chapter 4's challenge.</td></tr>
    <tr><td>No QEMU window on Windows</td><td>Windows 10 has no window support for Linux apps. Use <code>make run-text</code>. On Windows 11, run <code>wsl --update</code> in PowerShell, then <code>wsl --shutdown</code>, and open Ubuntu again.</td></tr>
    <tr><td>Stuck inside <code>make run-text</code></td><td>Press <kbd>Esc</kbd> then <kbd>2</kbd>, type <code>quit</code>, <kbd>Enter</kbd>. Or close the terminal.</td></tr>
    <tr><td>The mouse is stuck in the QEMU window</td><td>Press <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>G</kbd> (Mac: <kbd>Ctrl</kbd> <kbd>⌥</kbd> <kbd>G</kbd>).</td></tr>
    <tr><td>It worked before and now it's broken</td><td><code>git diff</code> shows what changed since your last save. <code>git restore .</code> goes back to it (and throws away the changes).</td></tr>
    </tbody></table>

    <h3>See why QEMU crashed</h3>
    {s.code("qemu-system-i386 -kernel build/kernel.elf -no-reboot -d int,cpu_reset 2>&1 | tail -40")}
    <p>The last lines show the interrupts just before the reset. <code>v=0d</code> is a general protection fault, <code>v=0e</code> a page fault, <code>v=08</code> a double fault. Paste them to your AI with the files you changed.</p>
    <h3>Find which line crashed</h3>
    <p>Take the <code>eip</code> from the panic screen and ask the toolchain which function it is in:</p>
    {s.code('''"$(brew --prefix llvm)/bin/llvm-addr2line" -f -e build/kernel.elf 0x00101234''', os="mac")}
    {s.code('''addr2line -f -e build/kernel.elf 0x00101234     # if missing: sudo apt install binutils''', os="win")}

    <h2><b>Glossary</b></h2>
    <table><tbody>
    <tr><th>Kernel</th><td>The core of an OS: the code that controls the hardware and runs everything else.</td></tr>
    <tr><th>Bootloader</th><td>The small program that loads the kernel into memory and starts it. Ours is built into QEMU.</td></tr>
    <tr><th>Multiboot</th><td>A standard way for a bootloader to find and start a kernel: a magic number and a few flags.</td></tr>
    <tr><th>QEMU</th><td>A program that pretends to be a whole PC, so your OS can run in a window.</td></tr>
    <tr><th>Freestanding</th><td>C code with no operating system and no C library under it.</td></tr>
    <tr><th>Linker script</th><td>Tells the linker where each part of the program goes in memory.</td></tr>
    <tr><th>Stack</th><td>Memory where C keeps local variables and return addresses. It grows downwards.</td></tr>
    <tr><th>VGA text mode</th><td>The screen as 80 × 25 characters in memory at <code>0xB8000</code>.</td></tr>
    <tr><th>I/O port</th><td>A number used to talk to a device with <code>inb</code>/<code>outb</code>, separate from memory addresses.</td></tr>
    <tr><th>Serial port</th><td>COM1: sends text byte by byte. QEMU connects it to your terminal.</td></tr>
    <tr><th>Interrupt</th><td>A signal that makes the CPU stop and run a handler, then continue.</td></tr>
    <tr><th>Exception</th><td>An interrupt raised by the CPU because code did something wrong (0–31).</td></tr>
    <tr><th>IRQ</th><td>An interrupt request from a device: 0 is the timer, 1 the keyboard.</td></tr>
    <tr><th>GDT</th><td>Global Descriptor Table: memory segments. We set two that cover everything.</td></tr>
    <tr><th>IDT</th><td>Interrupt Descriptor Table: which handler runs for each interrupt.</td></tr>
    <tr><th>PIC</th><td>The chip that collects hardware IRQs and passes them to the CPU.</td></tr>
    <tr><th>PIT</th><td>The timer chip that ticks at a rate we choose.</td></tr>
    <tr><th>Scancode</th><td>The number a keyboard sends for a key's position.</td></tr>
    <tr><th>Page</th><td>A 4 KiB block of memory, the unit the OS hands out.</td></tr>
    <tr><th>Bitmap allocator</th><td>Keeps one bit per page to know which ones are free.</td></tr>
    <tr><th>Heap / kmalloc</th><td>Where small pieces of memory come from when the kernel asks for them.</td></tr>
    <tr><th>Triple fault</th><td>A crash while handling a crash while handling a crash. The CPU resets.</td></tr>
    <tr><th>Vibe coding</th><td>Building by describing what you want to an AI, running the result, and steering it.</td></tr>
    </tbody></table>
    ''', "Common problems when building the OS, how to ask your AI for help, and a glossary.")
