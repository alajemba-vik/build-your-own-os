"""Shared page template and helpers for the tutorial site, in English and French.
The text of the pages is in content_en.py and content_fr.py; build_pages.py runs both."""
import html, textwrap, pathlib

REPO = "https://github.com/alajemba-vik/build-your-own-os"
SITE = "https://alajemba-vik.github.io/build-your-own-os/"
V = "20261126a"

# key, file name, chapter number
PAGES = [("index", "index.html", ""), ("setup-mac", "setup-mac.html", ""), ("setup-windows", "setup-windows.html", ""),
         ("ch1", "chapter-1-boot.html", "1"), ("ch2", "chapter-2-console.html", "2"),
         ("ch3", "chapter-3-interrupts.html", "3"), ("ch4", "chapter-4-keyboard.html", "4"),
         ("ch5", "chapter-5-shell.html", "5"), ("ch6", "chapter-6-memory.html", "6"),
         ("ch7", "chapter-7-desktop.html", "7"), ("ch8", "chapter-8-make-it-yours.html", "8"),
         ("help", "help.html", "")]
GROUPS = [("index",), ("setup-mac", "setup-windows"), ("ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8"), ("help",)]
FILE = {k: f for k, f, _ in PAGES}
NUM = {k: n for k, _, n in PAGES}

T = {
    "en": dict(
        groups=["Start", "Set up", "Build it", "Help"],
        labels={"index": "Welcome", "setup-mac": "On a Mac", "setup-windows": "On Windows",
                "ch1": "Boot and say hello", "ch2": "A real console", "ch3": "Interrupts and crashes",
                "ch4": "Timer and keyboard", "ch5": "A shell", "ch6": "Memory", "ch7": "A desktop with windows",
                "ch8": "Make it yours and share it", "help": "Stuck? Glossary"},
        site="Build your own OS", skip="Skip to the content", chapters="Chapters", mycomputer="My computer",
        pager="Previous and next", done="I finished this part",
        footer=('Made by the <a href="https://aivancity-tech-club.github.io/">aivancity Tech Club</a> for the Thursday build session · '
                f'<a href="{REPO}">Code on GitHub</a> · MIT licence · Found a mistake? <a href="{REPO}/issues">Tell us</a>'),
        other="fr", other_label="FR", other_title="Lire en français",
        ref_default="Peek at the reference solution", ref_hint="open it only when you are stuck",
        ref_body=(f'This is the code from the finished OS in <a href="{REPO}/tree/main/os">os/</a>. Yours does not have to look the same: '
                  'if it works and you understand it, it is right.'),
        save_title="Save <b>your progress</b>",
        save_body="Save a snapshot with Git, so you can always go back if a later step breaks something:",
    ),
    "fr": dict(
        groups=["Commencer", "Installer", "Construire", "Aide"],
        labels={"index": "Bienvenue", "setup-mac": "Sur Mac", "setup-windows": "Sur Windows",
                "ch1": "Démarrer et dire bonjour", "ch2": "Une vraie console", "ch3": "Interruptions et plantages",
                "ch4": "Minuteur et clavier", "ch5": "Un shell", "ch6": "La mémoire", "ch7": "Un bureau avec des fenêtres",
                "ch8": "À vous de jouer, et partagez-le", "help": "Bloqué ? Glossaire"},
        site="Construisez votre OS", skip="Aller au contenu", chapters="Chapitres", mycomputer="Mon ordinateur",
        pager="Précédent et suivant", done="J’ai terminé cette partie",
        footer=('Réalisé par le <a href="https://aivancity-tech-club.github.io/">aivancity Tech Club</a> pour la séance du jeudi · '
                f'<a href="{REPO}">Code sur GitHub</a> · Licence MIT · Une erreur ? <a href="{REPO}/issues">Dites-le-nous</a>'),
        other="en", other_label="EN", other_title="Read in English",
        ref_default="Jeter un œil à la solution de référence", ref_hint="à ouvrir seulement si vous êtes bloqué",
        ref_body=(f'Voici le code de l’OS terminé, dans <a href="{REPO}/tree/main/os">os/</a>. Le vôtre n’a pas besoin d’être identique : '
                  's’il fonctionne et que vous le comprenez, il est juste.'),
        save_title="Enregistrez <b>votre progression</b>",
        save_body="Prenez une photo de votre code avec Git, pour pouvoir revenir en arrière si une étape suivante casse quelque chose :",
    ),
}


class Site:
    def __init__(self, lang, root_dir):
        self.lang = lang
        self.t = T[lang]
        self.root = "" if lang == "en" else "../"          # path from this language's pages to the repository root
        self.out = root_dir if lang == "en" else root_dir / lang
        self.out.mkdir(exist_ok=True)

    @staticmethod
    def code(text, label=None, os=None):
        cls = {"mac": " only-mac", "win": " only-win"}.get(os, "")
        lab = f'<span class="label">{html.escape(label)}</span>' if label else ""
        return f'<div class="code{cls}">{lab}<pre>{html.escape(textwrap.dedent(text).strip())}</pre></div>'

    @staticmethod
    def prompt(text):
        paras = [p.strip() for p in textwrap.dedent(text).strip().split("\n\n")]
        return '<div class="prompt">' + "".join(f"<p>{html.escape(p)}</p>" for p in paras) + "</div>"

    def ref(self, files, what=None):
        t = self.t
        return (f'<details class="ref" data-files="{" ".join(files)}"><summary>{what or t["ref_default"]} ({t["ref_hint"]})</summary>'
                f'<p>{t["ref_body"]}</p></details>')

    def save(self, msg):
        return f'<h2>{self.t["save_title"]}</h2>\n<p>{self.t["save_body"]}</p>\n{self.code(f"git add -A && git commit -m {chr(34)}{msg}{chr(34)}")}'

    def page(self, key, title, body, desc):
        t, r = self.t, self.root
        order = [k for k, _, _ in PAGES]
        idx = order.index(key)
        prev = order[idx - 1] if idx > 0 else None
        nxt = order[idx + 1] if idx + 1 < len(order) else None
        nav = ""
        for name, keys in zip(t["groups"], GROUPS):
            nav += f"<h2>{name}</h2><ol>"
            for k in keys:
                cur = ' aria-current="page"' if k == key else ""
                nav += f'<li><a href="{FILE[k]}" data-page="{k}"{cur}><span class="num">{NUM[k]}</span>{t["labels"][k]}<span class="tick"></span></a></li>'
            nav += "</ol>"
        pager = f'<nav class="pager" aria-label="{t["pager"]}">'
        pager += f'<a class="btn" href="{FILE[prev]}">← {t["labels"][prev]}</a>' if prev else "<span></span>"
        pager += f'<a class="btn btn-primary" href="{FILE[nxt]}">{t["labels"][nxt]} →</a>' if nxt else ""
        pager += "</nav>"
        done = f'<label class="done"><input type="checkbox"> {t["done"]}</label>' if key.startswith(("ch", "setup")) else ""
        en_url, fr_url = SITE + FILE[key].replace("index.html", ""), SITE + "fr/" + FILE[key].replace("index.html", "")
        other_href = (f"fr/{FILE[key]}" if self.lang == "en" else f"../{FILE[key]}")
        full = f"{html.escape(title)} · {t['site']}"
        doc = f'''<!doctype html>
<html lang="{self.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{html.escape(desc)}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Figtree:wght@400;600;700;800&family=Google+Sans+Code:wght@400;600&family=Instrument+Serif:ital@1&display=swap">
<link rel="stylesheet" href="{r}assets/site.css?v={V}">
</head>
<body data-page="{key}" data-root="{r}">
<a class="skip" href="#main">{t["skip"]}</a>
<header class="top">
  <button class="btn menu-btn" type="button" aria-expanded="false" aria-controls="side">{t["chapters"]}</button>
  <a class="brand" href="index.html"><span class="chip-os">OS</span> {t["site"]} <span class="long">· aivancity Tech Club</span></a>
  <span class="spacer"></span>
  <a class="lang-switch" href="{other_href}" hreflang="{t["other"]}" lang="{t["other"]}" title="{t["other_title"]}" data-lang="{t["other"]}">{t["other_label"]}</a>
  <div class="os-switch" role="group" aria-label="{t["mycomputer"]}">
    <button type="button" data-os="mac" aria-pressed="false">macOS</button>
    <button type="button" data-os="win" aria-pressed="false">Windows</button>
  </div>
</header>
<div class="wrap">
<nav class="side" id="side" aria-label="{t["chapters"]}">{nav}</nav>
<main id="main">
{body}
{done}
{pager}
</main>
</div>
<footer>{t["footer"]}</footer>
<script src="{r}assets/site.js?v={V}"></script>
</body>
</html>
'''
        (self.out / FILE[key]).write_text(doc)


SCREEN = '''<pre class="screen" aria-label="{label}"><span class="c">  __  __        ___  ____
 |  \\/  |_   _ / _ \\/ ___|
 | |\\/| | | | | | | \\___ \\
 | |  | | |_| | |_| |___) |
 |_|  |_|\\__, |\\___/|____/
         |___/   </span><span class="w">Welcome to MyOS 0.1</span>

<span class="g">[ OK ]</span> GDT: memory segments loaded
<span class="g">[ OK ]</span> IDT: interrupt handlers installed
<span class="g">[ OK ]</span> Timer: ticking 100 times a second
<span class="g">[ OK ]</span> Keyboard: ready
<span class="g">[ OK ]</span> Memory: 127 MiB found

Type help to see what you can do.
<span class="c">MyOS&gt;</span> about
MyOS 0.1: a tiny operating system for 32-bit x86 PCs.
Written in C, from scratch, with no help from Windows, macOS or Linux.
<span class="c">MyOS&gt;</span> _</pre>'''

DESKTOP = '''<pre class="screen" aria-label="{label}"><span style="background:#aaa;color:#000"> MyOS Desktop                                                    up 00:02:14 </span>
<span style="color:#0aa;background:#00a">░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</span>
<span style="color:#0aa;background:#00a">░░░░</span><span style="background:#aaa;color:#000">╔════════════<span style="background:#0aa"> Welcome </span>═════════════╗</span><span style="color:#0aa;background:#00a">░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</span>
<span style="color:#0aa;background:#00a">░░░░</span><span style="background:#aaa;color:#000">║ Hello! This desktop runs on      ║</span><span style="background:#000"> </span><span style="color:#0aa;background:#00a">░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</span>
<span style="color:#0aa;background:#00a">░░░░</span><span style="background:#aaa;color:#000">║ MyOS 0.1, an OS you built        ║</span><span style="background:#000"> </span><span style="color:#0aa;background:#00a">░░░░░</span><span style="background:#aaa;color:#000">┌─────────── System ──────────┐</span><span style="color:#0aa;background:#00a">░░</span>
<span style="color:#0aa;background:#00a">░░░░</span><span style="background:#aaa;color:#000">╚══════════════════════════════════╝</span><span style="background:#000"> </span><span style="color:#0aa;background:#00a">░░░░░</span><span style="background:#aaa;color:#000">│ Uptime    00:02:14          │</span><span style="color:#0aa;background:#00a">░░</span>
<span style="background:#aaa;color:#000"> Tab: next window   Arrows or WASD: move it   Esc: back to the shell           </span></pre>'''

GET_STARTER = '''
cd ~
git clone https://github.com/alajemba-vik/build-your-own-os.git
cp -R build-your-own-os/starter my-os
cd my-os
git init && git add -A && git commit -m "Start from the starter"
make run
'''
