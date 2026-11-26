# Instructions for AI assistants working on this repository

This repository is the **Build your own OS, with AI** tutorial of the aivancity Tech Club:
the website (GitHub Pages, https://alajemba-vik.github.io/build-your-own-os/), the starter kit and the finished reference OS.

> **Are you a student building your OS?** This is not your file. Copy `starter/` to your own folder
> (see the setup pages): it contains `starter/AGENTS.md`, the brief your AI should read.

## What's where
| Path | What it is | How to change it |
|---|---|---|
| `starter/` | What students copy to begin: a kernel that boots and says hello, `Makefile`, `linker.ld`, and `AGENTS.md` (the brief for the student's AI) | Keep it at the "end of chapter 1" stage. Same `Makefile` and `linker.ld` as `os/` |
| `os/` | The finished reference OS: all 8 chapters (32-bit x86, Multiboot 1, freestanding C, clang + ld.lld, QEMU) | Code shown on the chapter pages is loaded from here at runtime, so a change here changes the site |
| `tools/build_pages.py`, `tools/pagekit.py`, `tools/content_en.py`, `tools/content_fr.py` | Write every tutorial page in English (root) and French (`fr/`). `pagekit.py` is the page template, the `content_*.py` files hold the text | **Edit the text there, never the generated `.html` files**, then run `python3 tools/build_pages.py` and commit both |
| `assets/site.css`, `assets/site.js` | Styles and behaviour (Mac/Windows switch, copy buttons, reference code loader, progress) | Bump `V` in `tools/pagekit.py` after changing them, then rebuild the pages |
| `tools/boot-test.sh` | Boots `os/` or `starter/` in QEMU with no window, types shell commands on the serial port, checks the answers | Update the expected strings if you change what the OS prints |
| `.github/workflows/build.yml` | Builds and boots both kernels on Ubuntu (same as the Windows/WSL guide) and macOS (same as the Mac guide) | Keep its install commands identical to the setup pages |

## Rules
- **No build step on the site**: plain HTML, CSS and JS, served as they are. No framework, no npm, no tracking. `.nojekyll` stays.
- **The OS stays simple**: 32-bit i686, Multiboot 1 loaded by `qemu-system-i386 -kernel`, no GRUB, no ISO, no C library, no 64-bit division, no floating point. Every `.c`/`.S` in `src/` is built automatically.
- **Chapters, prompts and code must agree.** If you change `os/`, check that the chapter's "Ask your AI" prompt, its checks and `tools/boot-test.sh` still match.
- **Test before pushing**: `make -C starter && make -C os && tools/boot-test.sh starter && tools/boot-test.sh os` (needs clang, ld.lld and QEMU: see the setup pages). Open the pages with `python3 -m http.server` and check the Mac and Windows views, light and dark, and a phone width.
- **Writing style**: short, plain, friendly sentences for students who may be new to C. Explain each new word once. Install commands must be copy-pasteable and must match CI.
- **The site is in English and French.** English pages are at the root, French ones in `fr/` with the same file names. Change both `tools/content_en.py` and `tools/content_fr.py` together. French uses "vous". Prompts are in French, but code, commands and what the OS prints stay in English.
