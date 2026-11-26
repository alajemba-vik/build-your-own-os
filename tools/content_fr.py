"""Texte français des pages du tutoriel (vouvoiement). La version anglaise est content_en.py : gardez les deux alignées.
Les noms de fichiers, les commandes et ce que l'OS affiche restent en anglais (c'est ce que les étudiants verront)."""
from pagekit import REPO, SCREEN, DESKTOP, GET_STARTER


def build(s):
    # ---------------------------------------------------------------- accueil
    s.page("index", "Construisez votre propre système d’exploitation, avec l’IA", f'''
<p class="eyebrow">aivancity Tech Club · séance de construction</p>
<h1>Construisez votre propre <b>système d’exploitation</b></h1>
<p class="lede">D’un écran noir à un shell et à un bureau avec des fenêtres. Écrit de zéro en C, en vibe coding avec l’IA de votre choix, sur Mac ou sur PC Windows. Huit chapitres courts.</p>
<div class="actions">
  <a class="btn btn-primary only-mac" href="setup-mac.html">Installer sur mon Mac →</a>
  <a class="btn btn-primary only-win" href="setup-windows.html">Installer sur mon PC Windows →</a>
  <a class="btn only-mac" href="setup-windows.html">Je suis sous Windows</a>
  <a class="btn only-win" href="setup-mac.html">Je suis sur Mac</a>
</div>
{SCREEN.format(label="Ce que votre OS affiche au démarrage")}
<p><small>Voici ce que l’OS terminé affiche au démarrage. Tout ce qui est à l’écran, c’est du code que vous allez écrire. L’OS parle anglais, comme la plupart des systèmes à leurs débuts : à vous de le traduire si vous le souhaitez.</small></p>

<div class="note thursday">
<p><b>Jeudi 26 novembre, 13 h – 14 h, AIClinic – salle 107.</b></p>
<p><b>Avant de venir (15 minutes) :</b> suivez l’installation pour <a href="setup-mac.html">Mac</a> ou <a href="setup-windows.html">Windows</a> jusqu’à voir « Hello from my own operating system! ». Les téléchargements sont lourds : ne comptez pas sur le Wi-Fi de l’école.<br>
<b>En salle :</b> chapitres 1 à 3, ensemble. <b>Chez vous :</b> chapitres 4 à 8, à votre rythme. Apportez un ordinateur portable et son chargeur.</p>
</div>

<h2>C’est quoi, un <b>système d’exploitation</b> ?</h2>
<p>C’est le programme qui démarre en premier et qui gouverne l’ordinateur : il parle au matériel (écran, clavier, mémoire, minuteur), il décide de ce qui s’exécute et quand, et il offre aux autres programmes une façon simple d’utiliser tout cela. Windows, macOS, Linux, Android et iOS sont des systèmes d’exploitation (OS). En leur cœur se trouve le <b>noyau</b> (kernel), et c’est lui que nous construisons.</p>
<p>Quand vous appuyez sur le bouton d’alimentation, voici ce qui se passe. Vous écrirez les parties en gras :</p>
<div class="chain" aria-label="La chaîne de démarrage"><span>Mise sous tension</span><i>→</i><span>Micrologiciel (BIOS)</span><i>→</i><span>Chargeur d’amorçage</span><i>→</i><span><b>boot.S</b></span><i>→</i><span><b>kernel_main()</b></span><i>→</i><span><b>pilotes</b></span><i>→</i><span><b>votre shell</b></span></div>

<h2>Va-t-il remplacer <b>Windows ou macOS</b> ?</h2>
<p>Non. Votre OS tourne dans <b>QEMU</b>, un programme gratuit qui se fait passer pour un PC entier (un <i>émulateur</i>). Rien ne change sur votre ordinateur, et si votre OS plante, il suffit de fermer la fenêtre. C’est pourtant un vrai OS : le même code pourrait démarrer un vrai PC.</p>
<p>Nous visons le PC Intel 32 bits classique (x86), parce que c’est le mieux documenté et le plus simple pour commencer. Il fonctionne de la même façon sur les Mac Intel, les Mac Apple Silicon (M1–M4) et les PC Windows.</p>

<h2>Comment <b>vibe-coder</b> un OS</h2>
<p>Vous décrivez ce que vous voulez, l’IA écrit le code, et vous l’exécutez, le lisez et la guidez. Un OS s’y prête très bien : l’IA connaît les astuces du matériel, et vous apprenez à quoi sert chacune. Cinq règles pour que cela marche :</p>
<ol class="steps">
<li><b>Donnez le brief à votre IA.</b> Le kit de départ contient <a href="{REPO}/blob/main/starter/AGENTS.md"><code>AGENTS.md</code></a> : les règles du projet (32 bits, pas de bibliothèque C, clang, QEMU…). Les agents de code le lisent tout seuls ; avec une IA de chat, collez-le en premier. Il est en anglais, mais votre IA vous répondra en français si vous lui écrivez en français.</li>
<li><b>Un chapitre, une étape à la fois.</b> Chaque chapitre vous donne un prompt. Ne demandez pas tout l’OS d’un coup : vous obtiendriez quelque chose que vous ne sauriez pas réparer.</li>
<li><b>Demandez pourquoi, pas seulement quoi.</b> Chaque chapitre propose des questions à poser. Si vous ne savez pas expliquer une ligne, demandez jusqu’à ce que vous sachiez.</li>
<li><b>Lancez-le après chaque modification</b> avec <code>make run</code>. Quand ça casse, collez l’erreur complète à l’IA.</li>
<li><b>Enregistrez avec Git</b> quand quelque chose marche. Bloqué ? Chaque chapitre contient le code de référence d’un OS terminé, pour comparer.</li>
</ol>

<h2>Quelle <b>IA</b> ?</h2>
<div class="grid">
<div class="card"><h3>Agents de code</h3><p>Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI. Ils lisent les fichiers de votre dossier et <code>AGENTS.md</code>, modifient le code et peuvent lancer <code>make</code>. Le choix le plus simple.</p></div>
<div class="card"><h3>IA de chat</h3><p>ChatGPT, Claude.ai, Gemini. Collez <code>AGENTS.md</code> au début, puis les fichiers à modifier, et recopiez les réponses dans vos fichiers.</p></div>
<div class="card"><h3>Sans IA ?</h3><p>Ça marche aussi. Chaque chapitre explique l’idée, et le code de référence est entièrement commenté (en anglais). Lisez-le, puis écrivez-le vous-même.</p></div>
</div>

<h2>Les <b>chapitres</b></h2>
<table>
<thead><tr><th>#</th><th>Vous construisez</th><th>Durée</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="chapter-1-boot.html">Démarrer et dire bonjour</a> : le noyau de départ, comment un PC démarre</td><td>20 min</td></tr>
<tr><td>2</td><td><a href="chapter-2-console.html">Une vraie console</a> : défilement, couleurs, <code>kprintf</code>, le port série</td><td>30 min</td></tr>
<tr><td>3</td><td><a href="chapter-3-interrupts.html">Interruptions et plantages</a> : GDT, IDT, un écran de kernel panic</td><td>40 min</td></tr>
<tr><td>4</td><td><a href="chapter-4-keyboard.html">Minuteur et clavier</a> : vos premiers pilotes</td><td>40 min</td></tr>
<tr><td>5</td><td><a href="chapter-5-shell.html">Un shell</a> : des commandes à taper</td><td>30 min</td></tr>
<tr><td>6</td><td><a href="chapter-6-memory.html">La mémoire</a> : trouver la RAM, distribuer des pages</td><td>40 min</td></tr>
<tr><td>7</td><td><a href="chapter-7-desktop.html">Un bureau avec des fenêtres</a> : à déplacer avec les flèches</td><td>40 min</td></tr>
<tr><td>8</td><td><a href="chapter-8-make-it-yours.html">À vous de jouer, et partagez-le</a></td><td>autant que vous voulez</td></tr>
</tbody></table>
<p>L’OS terminé complet se trouve dans le <a href="{REPO}">dépôt GitHub</a> (dossier <code>os/</code>). Chaque modification est compilée et démarrée automatiquement sous Linux et macOS, pour vérifier que les instructions fonctionnent.</p>
''', "Construisez un petit système d’exploitation de zéro, sur macOS ou Windows, en vibe coding avec l’IA de votre choix. Un tutoriel de l’aivancity Tech Club.")

    # ---------------------------------------------------------------- installation Mac
    s.page("setup-mac", "Installer sur Mac", f'''
<p class="eyebrow">Installation · environ 15 minutes</p>
<h1>Préparez <b>votre Mac</b></h1>
<p class="lede">Il vous faut trois choses : les outils de développement d’Apple (Git et make), un compilateur capable de produire du code pour PC (clang et lld, de LLVM), et QEMU pour faire tourner votre OS. Les Mac Intel et Apple Silicon conviennent tous les deux.</p>
<ol class="steps">
<li><h3>Ouvrez le Terminal</h3><p>Appuyez sur <kbd>⌘</kbd> <kbd>Espace</kbd>, tapez <b>Terminal</b>, appuyez sur <kbd>Entrée</kbd>. Collez chaque commande ci-dessous et appuyez sur <kbd>Entrée</kbd>.</p></li>
<li><h3>Installez les outils de développement d’Apple</h3>{s.code("xcode-select --install")}<p>Une fenêtre s’ouvre : cliquez sur <b>Installer</b>. S’il est indiqué qu’ils sont déjà installés, pas de souci : continuez.</p></li>
<li><h3>Installez Homebrew</h3><p>Homebrew installe des outils de développement en une commande. Passez cette étape si <code>brew --version</code> fonctionne déjà.</p>
{s.code('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')}
<p>Il demande le mot de passe de votre Mac (rien ne s’affiche pendant la saisie : c’est normal). <b>À la fin, il affiche « Next steps » avec deux ou trois commandes : lancez-les</b>, puis fermez le Terminal et rouvrez-le.</p></li>
<li><h3>Installez le compilateur et QEMU</h3>{s.code("brew install llvm lld qemu")}<p>Comptez 5 à 10 minutes. <b>llvm</b> fournit <code>clang</code>, le compilateur C, <b>lld</b> l’éditeur de liens qui assemble les morceaux, et <b>qemu</b> le PC émulé.</p></li>
<li><h3>Vérifiez que ça a marché</h3>{s.code('''
"$(brew --prefix llvm)/bin/clang" --version
ls "$(brew --prefix lld)/bin/ld.lld"
qemu-system-i386 --version
''')}<p>Chaque ligne doit afficher une version ou un chemin, et non « command not found » ou « No such file ».</p></li>
<li><h3>Récupérez le kit de départ et lancez-le</h3>{s.code(GET_STARTER)}
<p>Une fenêtre QEMU s’ouvre avec <b>« Hello from my own operating system! »</b>. C’est votre OS. Pour l’arrêter, fermez la fenêtre ou appuyez sur <kbd>Ctrl</kbd> <kbd>C</kbd> dans le Terminal.</p>
<p>La première fois, Git peut vous demander qui vous êtes. Lancez ces commandes avec votre nom et votre e-mail, puis refaites le commit :</p>
{s.code('git config --global user.name "Votre Nom"\\ngit config --global user.email "vous@example.com"')}</li>
<li><h3>Ouvrez-le avec votre IA</h3><p>Ouvrez le dossier <code>my-os</code> dans votre éditeur ou votre outil d’IA. Par exemple :</p>
{s.code('''
code .        # VS Code (avec Copilot), ou : cursor .
claude        # Claude Code, dans le dossier my-os
codex         # Codex CLI, dans le dossier my-os
''')}<p>Vous utilisez plutôt une IA de chat ? Ouvrez <code>my-os/AGENTS.md</code> (ou <a href="{REPO}/blob/main/starter/AGENTS.md">lisez-le sur GitHub</a>), copiez-le en entier et collez-le comme premier message.</p></li>
</ol>
<div class="note"><p><b>« command not found: brew »</b> : vous avez manqué les lignes « Next steps » à la fin de l’installation de Homebrew. Lancez <code>eval "$(/opt/homebrew/bin/brew shellenv)"</code> (Apple Silicon) ou <code>eval "$(/usr/local/bin/brew shellenv)"</code> (Intel), et ajoutez cette ligne à <code>~/.zprofile</code>.</p>
<p><b>La fenêtre QEMU n’apparaît pas</b> : cherchez-la derrière le Terminal ou dans le Dock. Ou lancez <code>make run-text</code> pour voir l’écran dans le Terminal (pour quitter : <kbd>Échap</kbd> puis <kbd>2</kbd>, tapez <code>quit</code>, <kbd>Entrée</kbd>).</p>
<p>D’autres solutions sur la <a href="help.html">page d’aide</a>.</p></div>
''', "Installez clang, lld et QEMU sur macOS avec Homebrew, et démarrez l’OS de départ.")

    # ---------------------------------------------------------------- installation Windows
    s.page("setup-windows", "Installer sur Windows", f'''
<p class="eyebrow">Installation · environ 20 minutes</p>
<h1>Préparez <b>votre PC Windows</b></h1>
<p class="lede">Les outils pour écrire un OS s’utilisent le plus facilement sous Linux, et Windows peut faire tourner Linux grâce à <b>WSL</b> (Windows Subsystem for Linux). Vous installez Ubuntu une fois, puis tout se passe dans son terminal. Windows 11 est l’idéal ; Windows 10 fonctionne aussi.</p>
<ol class="steps">
<li><h3>Installez WSL et Ubuntu</h3><p>Ouvrez le menu Démarrer, tapez <b>PowerShell</b>, faites un clic droit dessus et choisissez <b>Exécuter en tant qu’administrateur</b>. Puis :</p>{s.code("wsl --install")}<p><b>Redémarrez votre PC</b> quand il le demande. Ubuntu s’ouvre tout seul après le redémarrage (sinon, ouvrez <b>Ubuntu</b> depuis le menu Démarrer). Choisissez un nom d’utilisateur et un mot de passe pour Linux. Rien ne s’affiche pendant la saisie du mot de passe : c’est normal. Retenez-le, il vous servira pour <code>sudo</code>.</p></li>
<li><h3>Installez le compilateur et QEMU</h3><p>Dans la fenêtre <b>Ubuntu</b> (pas PowerShell) :</p>{s.code("sudo apt update && sudo apt install -y clang lld make git qemu-system-x86 qemu-system-gui")}<p><b>clang</b> est le compilateur C, <b>lld</b> l’éditeur de liens qui assemble les morceaux, <b>qemu</b> le PC émulé. C’est exactement la commande qu’utilise notre test automatique : elle fonctionne.</p></li>
<li><h3>Vérifiez que ça a marché</h3>{s.code('''
clang --version
ld.lld --version
qemu-system-i386 --version
''')}</li>
<li><h3>Récupérez le kit de départ et lancez-le</h3><p>Restez dans votre dossier personnel Linux (<code>cd ~</code>). Ne travaillez pas dans <code>/mnt/c/…</code> : c’est beaucoup plus lent.</p>{s.code(GET_STARTER)}
<p>Sous Windows 11, une fenêtre QEMU s’ouvre avec <b>« Hello from my own operating system! »</b>. C’est votre OS. Pour l’arrêter, fermez la fenêtre ou appuyez sur <kbd>Ctrl</kbd> <kbd>C</kbd> dans Ubuntu.</p>
<p><b>Pas de fenêtre (Windows 10) ?</b> Lancez <code>make run-text</code> : l’écran de votre OS s’affiche dans la fenêtre Ubuntu. Pour quitter : <kbd>Échap</kbd> puis <kbd>2</kbd>, tapez <code>quit</code>, <kbd>Entrée</kbd>.</p>
<p>La première fois, Git peut vous demander qui vous êtes. Lancez ces commandes avec votre nom et votre e-mail, puis refaites le commit :</p>
{s.code('git config --global user.name "Votre Nom"\\ngit config --global user.email "vous@example.com"')}</li>
<li><h3>Ouvrez-le avec votre IA</h3><p><b>VS Code</b> : installez-le sous Windows avec l’extension <b>WSL</b>, puis dans Ubuntu, dans <code>my-os</code>, lancez <code>code .</code>. Cursor fonctionne de la même façon. Les IA en terminal (Claude Code, Codex, Gemini CLI) s’installent et se lancent <b>dans Ubuntu</b>, dans le dossier <code>my-os</code>.</p>
{s.code('''
code .        # VS Code (avec Copilot) via WSL
claude        # Claude Code, dans le dossier my-os
''')}<p>Vous utilisez plutôt une IA de chat ? Ouvrez <code>my-os/AGENTS.md</code> (dans VS Code, avec <code>cat AGENTS.md</code>, ou <a href="{REPO}/blob/main/starter/AGENTS.md">sur GitHub</a>), copiez-le en entier et collez-le comme premier message.</p></li>
</ol>
<div class="note"><p><b>« Please enable the Virtual Machine Platform » ou erreur 0x80370102</b> : la virtualisation est désactivée. Activez <b>la virtualisation</b> (Intel VT-x / AMD-V / SVM) dans les réglages du BIOS de votre PC, puis relancez <code>wsl --install</code>.</p>
<p><b>wsl --install n’affiche que l’aide</b> : WSL est déjà là. Lancez <code>wsl --install -d Ubuntu</code>, puis <code>wsl --update</code>.</p>
<p>D’autres solutions sur la <a href="help.html">page d’aide</a>.</p></div>
''', "Installez WSL, Ubuntu, clang, lld et QEMU sous Windows, et démarrez l’OS de départ.")

    # ---------------------------------------------------------------- chapitre 1
    s.page("ch1", "Chapitre 1 : Démarrer et dire bonjour", f'''
<p class="eyebrow">Chapitre 1 · environ 20 minutes</p>
<h1>Démarrer et <b>dire bonjour</b></h1>
<p class="lede">Votre kit de départ démarre déjà. Dans ce chapitre, vous découvrez exactement comment, ligne par ligne, avec votre IA, et vous personnalisez le premier écran.</p>

<h2>L’<b>idée</b></h2>
<p>Un PC lance son micrologiciel (le BIOS), qui charge un <b>chargeur d’amorçage</b> (bootloader). Le nôtre est intégré à QEMU : <code>qemu-system-i386 -kernel build/kernel.elf</code>. Il suit une norme appelée <b>Multiboot</b> : il cherche un nombre magique, <code>0x1BADB002</code>, au début de notre fichier, charge le noyau à 1 Mio en mémoire et saute dedans, avec le processeur déjà en mode 32 bits.</p>
<p>À partir de là, tout est à nous :</p>
<ul>
<li><code>src/boot.S</code> (assembleur) contient le nombre magique, prépare une <b>pile</b> (la mémoire dont le C a besoin pour ses variables) et appelle <code>kernel_main</code>.</li>
<li><code>linker.ld</code> indique où chaque morceau du noyau va en mémoire.</li>
<li><code>src/kernel.c</code> écrit à l’écran. En mode texte, l’écran <i>est</i> de la mémoire : 80 × 25 cases à partir de l’adresse <code>0xB8000</code>, 2 octets chacune (le caractère, puis sa couleur). Écrivez là, et des lettres apparaissent.</li>
<li>Le <code>Makefile</code> compile avec <code>--target=i686-elf -ffreestanding</code> : du code pour un PC 32 bits nu, sans système d’exploitation ni bibliothèque C en dessous. Le système d’exploitation, <i>c’est nous</i>.</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>Lancez-le</h3>{s.code("make run")}<p>Vous voyez le message de bienvenue. Fermez QEMU.</p></li>
<li><h3>Faites-le expliquer par votre IA</h3>{s.prompt('''
Lis AGENTS.md et tous les fichiers de ce projet. Explique-moi avec des mots simples ce qui se passe entre le moment où QEMU démarre et celui où « Hello » apparaît à l’écran. Va fichier par fichier : Makefile, linker.ld, src/boot.S, src/kernel.c. Pour boot.S, explique chaque ligne. Réponds en français.''')}
<p>Puis posez des questions sur tout ce que vous ne comprenez pas. De bonnes questions :</p>
<ul><li>Pourquoi la pile commence-t-elle en haut et grandit-elle vers le bas ?</li><li>Que se passerait-il si <code>kernel_main</code> se terminait ?</li><li>Que contient l’octet de couleur <code>0x0B</code> ?</li><li>Pourquoi ne puis-je pas utiliser <code>printf</code> ici ?</li></ul></li>
<li><h3>Personnalisez-le</h3>{s.prompt('''
Change le premier écran : affiche mon nom à la place de « my own operating system », dessine un cadre autour de tout l’écran avec les caractères de dessin de boîtes de la police VGA (code page 437), et utilise au moins trois couleurs. Explique comment fonctionne l’octet de couleur (couleur du texte, couleur du fond). Garde tout dans kernel.c.''')}
{s.code("make run")}</li>
<li><h3>Cassez-le exprès</h3><p>Dans <code>boot.S</code>, remplacez <code>0x1BADB002</code> par un autre nombre et lancez <code>make run</code>. QEMU refuse de le démarrer : pas de nombre magique, pas de démarrage. Remettez-le.</p></li>
</ol>

<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>QEMU affiche votre nom, un cadre et plusieurs couleurs.</li><li>Vous savez dire à quoi servent <code>boot.S</code>, <code>linker.ld</code> et <code>0xB8000</code>.</li></ul>
{s.ref(["starter/src/boot.S", "starter/linker.ld", "starter/src/kernel.c", "starter/Makefile"], "Les fichiers du kit de départ")}
{s.save("Chapitre 1 : mon premier écran")}
''', "Comment un PC démarre, l’en-tête Multiboot, et écrire sur l’écran VGA.")

    # ---------------------------------------------------------------- chapitre 2
    s.page("ch2", "Chapitre 2 : Une vraie console", f'''
<p class="eyebrow">Chapitre 2 · environ 30 minutes</p>
<h1>Une vraie <b>console</b></h1>
<p class="lede">Écrire des lettres à des endroits fixes, on s’en lasse vite. Vous construisez une console comme celle d’un terminal : un curseur, des retours à la ligne, du défilement, des couleurs et votre propre <code>printf</code>. Et une deuxième sortie, le port série, qui s’affiche dans votre terminal et facilite beaucoup le débogage.</p>

<h2>L’<b>idée</b></h2>
<ul>
<li>La console retient une <b>ligne et une colonne</b>. Chaque caractère s’écrit là et fait avancer le curseur. <code>\\n</code> passe à la ligne suivante.</li>
<li>Quand la dernière ligne est pleine, on <b>fait défiler</b> : on recopie chaque ligne une ligne plus haut et on efface celle du bas.</li>
<li>Le curseur clignotant se déplace en parlant à la puce VGA par les <b>ports d’E/S</b> <code>0x3D4</code> et <code>0x3D5</code>. Les ports sont un second espace d’adresses réservé au matériel, utilisé avec les instructions <code>outb</code> et <code>inb</code>.</li>
<li><b>kprintf</b> est notre <code>printf</code> (le k veut dire kernel). Il utilise <code>stdarg.h</code>, que le compilateur nous fournit même sans bibliothèque C.</li>
<li>Le <b>port série</b> (COM1, port <code>0x3F8</code>) envoie les octets un par un. <code>make run</code> le relie à votre terminal : chaque ligne affichée par votre OS y apparaît aussi, et vous pouvez la copier pour votre IA.</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>Construisez la console</h3>{s.prompt('''
Chapitre 2. Crée src/io.h avec les fonctions outb/inb/outw (assembleur en ligne). Puis src/console.c et src/console.h : une console texte sur l’écran VGA avec une position de curseur, retour à la ligne, retour arrière, tabulation, défilement quand l’écran est plein, couleurs (un enum des 16 couleurs VGA) et déplacement du curseur matériel clignotant.

Ajoute src/serial.c pour COM1 (0x3F8), pour que chaque caractère affiché sur la console soit aussi envoyé sur le port série (envoie \\r avant \\n).

Ajoute src/printf.c avec kprintf qui gère %s %c %d %u %x %p %%, une largeur comme %5d, le remplissage par des zéros comme %02u, et l’alignement à gauche comme %-10s. Ajoute aussi un ksnprintf qui écrit dans un tampon. Et src/string.c avec memset, memcpy, memmove, strlen, strcmp, strncmp, car nous n’avons pas de bibliothèque C.

Mets à jour kernel_main pour effacer l’écran, afficher un titre en couleur, quelques lignes avec des nombres (négatifs, hexadécimaux), puis 30 lignes numérotées pour tester le défilement. Laisse les textes affichés par l’OS en anglais.''')}
{s.code("make run")}</li>
<li><h3>Comprenez-la</h3><p>Demandez à votre IA :</p><ul><li>Comment <code>va_list</code> fonctionne-t-il sans bibliothèque C ?</li><li>Pourquoi écrit-on <code>volatile</code> pour la mémoire de l’écran ?</li><li>Pourquoi le compilateur peut-il appeler <code>memset</code> alors que je ne l’ai jamais écrit ?</li></ul></li>
<li><h3>Personnalisez-la</h3><p>Affichez au démarrage un logo en ASCII art, en couleur, avec le nom de votre OS. Demandez-en un à votre IA (moins de 7 lignes et 60 colonnes), et qu’elle échappe les barres obliques inverses.</p></li>
</ol>

<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>Les 30 lignes défilent et les dernières sont visibles.</li><li><code>kprintf("%d %x %05u", -42, 255, 7)</code> affiche <code>-42 ff 00007</code>.</li><li>Le même texte apparaît dans votre terminal (le port série).</li></ul>
<div class="note"><p><b>« undefined symbol: memset »</b> (ou memcpy) : le compilateur s’en sert pour les grosses copies, et nous n’avons pas de bibliothèque C. Vérifiez que <code>string.c</code> existe et qu’il est compilé.</p><p><b>Des symboles bizarres à la place des lettres</b> : chaque case de l’écran vaut <code>caractère | (couleur &lt;&lt; 8)</code>. Vérifiez que le caractère est d’abord converti en <code>uint8_t</code>.</p></div>
{s.ref(["os/src/io.h", "os/src/console.h", "os/src/console.c", "os/src/serial.c", "os/src/printf.c", "os/src/string.c"])}
{s.save("Chapitre 2 : console, kprintf et port série")}
''', "Une console texte VGA avec défilement et couleurs, kprintf et le port série.")

    # ---------------------------------------------------------------- chapitre 3
    s.page("ch3", "Chapitre 3 : Interruptions et plantages", f'''
<p class="eyebrow">Chapitre 3 · environ 40 minutes</p>
<h1>Interruptions <b>et plantages</b></h1>
<p class="lede">Pour l’instant, si votre code fait une erreur, le PC redémarre sans rien dire. Vous apprenez au processeur où aller quand quelque chose se produit, et vous obtenez un vrai écran rouge de <b>kernel panic</b> qui dit ce qui s’est mal passé.</p>

<h2>L’<b>idée</b></h2>
<ul>
<li>Une <b>interruption</b> fait lâcher au processeur ce qu’il fait pour exécuter un gestionnaire (handler), puis y revenir. Certaines viennent du processeur lui-même quand le code se trompe (les <b>exceptions</b> : division par zéro, instruction invalide, défaut de page… numéros 0 à 31). D’autres viennent du matériel, comme le clavier (chapitre 4).</li>
<li>L’<b>IDT</b> (Interrupt Descriptor Table) est une liste de 256 adresses de gestionnaires. On la charge avec l’instruction <code>lidt</code>.</li>
<li>Avant cela, le processeur veut une <b>GDT</b> (Global Descriptor Table) : les anciennes puces x86 découpaient la mémoire en segments. Nous créons deux segments qui couvrent tous les deux les 4 Gio (code en <code>0x08</code>, données en <code>0x10</code>), et nous n’y pensons plus jamais.</li>
<li>Les gestionnaires commencent en assembleur (des <b>stubs</b>) : ils sauvegardent tous les registres, appellent une fonction C avec un pointeur vers eux, puis restaurent tout et exécutent <code>iret</code>. Certaines exceptions empilent un code d’erreur et d’autres non ; les stubs empilent un faux 0 pour que toutes les interruptions se ressemblent.</li>
<li>Si un plantage survient pendant le traitement d’un plantage, le processeur abandonne : c’est une <b>triple faute</b> (triple fault). QEMU s’arrête (nous utilisons <code>-no-reboot</code>).</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>GDT, IDT et écran de panique</h3>{s.prompt('''
Chapitre 3. Ajoute une GDT plate avec trois entrées (nulle, code noyau 0x08, données noyau 0x10, couvrant toutes deux 4 Gio) dans src/gdt.c, chargée par une fonction assembleur gdt_flush dans src/cpu.S qui recharge tous les registres de segment et fait un saut lointain (far jump) pour recharger CS.

Puis une IDT dans src/idt.c avec 48 entrées qui pointent vers des stubs assembleur isr0..isr47 dans cpu.S. Chaque stub empile un faux code d’erreur 0 quand le processeur n’en empile pas (il en empile un pour 8, 10-14, 17, 21, 29, 30), empile son numéro, et saute vers un stub commun qui sauvegarde tous les registres (pushal et les registres de segment), charge le segment de données du noyau et appelle isr_handler(struct regs *r) en C. Mets une table des 48 adresses de stubs dans cpu.S. Définis struct regs dans src/cpu.h, exactement dans l’ordre où les valeurs sont sur la pile.

Reprogramme aussi le PIC pour que les IRQ matérielles 0-15 utilisent les interruptions 32-47, mais garde-les toutes masquées pour l’instant.

Pour les exceptions 0-31, affiche un écran rouge KERNEL PANIC avec le nom de l’exception, le code d’erreur, eip et les registres, puis arrête le processeur pour toujours. Dans kernel_main, affiche des lignes « [ OK ] » après chaque étape.''')}
{s.code("make run")}</li>
<li><h3>Faites-le planter exprès</h3>{s.prompt('''
Ajoute un test temporaire à la fin de kernel_main qui exécute l’instruction ud2 (assembleur en ligne), pour que je voie l’écran de panique. Explique ce que veut dire « Invalid opcode ».''')}<p>Vous devez voir l’écran rouge avec <b>Invalid opcode</b>. Essayez ensuite une division par zéro (demandez à l’IA comment en écrire une que le compilateur ne supprime pas), puis supprimez le test.</p></li>
<li><h3>Comprenez-le</h3><p>Demandez à votre IA : Qu’est-ce que le processeur empile exactement quand une interruption arrive ? Pourquoi <code>struct regs</code> doit-elle correspondre exactement à ce qu’empile le stub ? Qu’est-ce que <code>iret</code> ? Pourquoi faut-il reprogrammer le PIC ?</p></li>
</ol>

<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>Le démarrage affiche <code>[ OK ] GDT</code> et <code>[ OK ] IDT</code>.</li><li><code>ud2</code> donne un écran de panique rouge avec « Invalid opcode », et QEMU reste ouvert.</li></ul>
<div class="note"><p><b>QEMU se ferme dès qu’il démarre</b> : c’est une triple faute. Lancez ceci et collez-en la fin à votre IA : on y voit les dernières interruptions et pourquoi le processeur a redémarré :</p>
{s.code("qemu-system-i386 -kernel build/kernel.elf -no-reboot -d int,cpu_reset 2>&1 | tail -40")}
<p>Les causes habituelles : un stub avec le mauvais réglage de code d’erreur, <code>struct regs</code> dans le mauvais ordre, un <code>__attribute__((packed))</code> oublié sur les structures des tables, ou le saut lointain dans <code>gdt_flush</code>.</p></div>
{s.ref(["os/src/cpu.S", "os/src/cpu.h", "os/src/gdt.c", "os/src/idt.c", "os/src/panic.c"])}
{s.save("Chapitre 3 : GDT, IDT et écran de kernel panic")}
''', "La GDT, l’IDT, les stubs d’interruption en assembleur et un écran de kernel panic.")

    # ---------------------------------------------------------------- chapitre 4
    s.page("ch4", "Chapitre 4 : Minuteur et clavier", f'''
<p class="eyebrow">Chapitre 4 · environ 40 minutes</p>
<h1>Minuteur et <b>clavier</b></h1>
<p class="lede">Vos deux premiers <b>pilotes</b> (drivers). Le minuteur permet à votre OS de compter le temps ; le clavier vous permet de taper. Après ce chapitre, votre OS vous répond.</p>

<h2>L’<b>idée</b></h2>
<ul>
<li>Le matériel lève des <b>IRQ</b> (demandes d’interruption). La puce <b>PIC</b> les rassemble et les transmet au processeur comme interruptions 32–47 (nous les y avons déplacées au chapitre 3). Après chacune, il faut envoyer au PIC un <b>End Of Interrupt</b> (fin d’interruption), sinon il n’en envoie plus jamais.</li>
<li>Le minuteur <b>PIT</b> compte à 1 193 182 Hz. Divisez par 100 et il lève l’IRQ 0 cent fois par seconde. Chacune est un <b>tick</b>.</li>
<li>Le clavier lève l’IRQ 1 à chaque touche appuyée ou relâchée. On lit un <b>scancode</b> sur le port <code>0x60</code> : un numéro qui désigne la position de la touche, pas une lettre. On le transforme en lettre avec une table, et on suit nous-mêmes l’état de Maj.</li>
<li>Les touches attendent dans un petit <b>tampon circulaire</b> (une file qui reboucle) jusqu’à ce que quelqu’un les lise.</li>
<li><code>sti</code> active les interruptions. <code>hlt</code> dort jusqu’à la prochaine interruption : aucun gaspillage de processeur en attendant une touche.</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>Le minuteur</h3>{s.prompt('''
Chapitre 4, partie 1. Ajoute irq_install(irq, handler) dans idt.c : elle enregistre le gestionnaire et démasque cette IRQ dans le PIC. Dans isr_handler, pour les interruptions 32-47, appelle le gestionnaire et envoie l’End Of Interrupt (aux deux PIC pour les IRQ 8-15). Ignore les IRQ parasites 7 et 15.

Puis src/timer.c et timer.h : programme le canal 0 du PIT à 100 Hz, compte les ticks sur l’IRQ 0, et ajoute timer_ticks(), uptime_seconds() et timer_sleep_ms(). Active les interruptions avec sti à la fin de kernel_main, puis affiche le temps écoulé une fois par seconde pour tester.''')}
{s.code("make run")}</li>
<li><h3>Le clavier</h3>{s.prompt('''
Chapitre 4, partie 2. Ajoute src/keyboard.c et keyboard.h : sur l’IRQ 1, lis le scancode sur le port 0x60, ignore les relâchements de touches (sauf pour suivre Maj), traduis le scancode set 1 en caractères avec deux tables pour un clavier QWERTY américain (normal et avec Maj), gère Verr. Maj, et transforme les flèches (préfixe 0xE0) en codes spéciaux KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT. Range les touches dans un tampon circulaire de 64 octets.

Ajoute input_poll(), qui renvoie la touche suivante ou -1, et input_getc(), qui attend une touche avec hlt. Les deux doivent aussi accepter les caractères tapés dans le terminal série (\\r veut dire Entrée, 0x7F veut dire Retour arrière). Remplace le test du temps écoulé par une boucle qui affiche chaque touche que je tape.''')}
{s.code("make run")}<p>Cliquez dans la fenêtre QEMU, puis tapez.</p></li>
<li><h3>Comprenez-le</h3><p>Demandez à votre IA : Que se passe-t-il si j’oublie l’End Of Interrupt ? Pourquoi la variable qui compte les ticks est-elle <code>volatile</code> ? Pourquoi les flèches envoient-elles deux octets ?</p></li>
</ol>
<div class="note idea"><p><b>Sur un clavier AZERTY</b>, les lettres sortent aux places du QWERTY (A donne Q). C’est normal : les scancodes sont des <i>positions</i> de touches. Un joli défi : demandez à votre IA d’ajouter une table AZERTY française et un moyen de basculer de l’une à l’autre.</p></div>
<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>Le démarrage affiche <code>[ OK ] Timer</code> et <code>[ OK ] Keyboard</code>.</li><li>Ce que vous tapez s’affiche, avec des majuscules quand vous maintenez Maj.</li><li>Votre terminal affiche le même texte, et taper dans le terminal fonctionne aussi.</li></ul>
<div class="note"><p><b>Rien ne se passe quand je tape</b> : avez-vous appelé <code>sti</code> ? L’IRQ 1 est-elle démasquée ? Envoyez-vous l’End Of Interrupt après <i>chaque</i> IRQ, y compris celles du minuteur ? Si le minuteur ne marche qu’une fois, c’est l’End Of Interrupt.</p></div>
{s.ref(["os/src/timer.h", "os/src/timer.c", "os/src/keyboard.h", "os/src/keyboard.c", "os/src/idt.c"])}
{s.save("Chapitre 4 : pilotes du minuteur et du clavier")}
''', "Les IRQ, le PIC, le minuteur PIT et un pilote de clavier PS/2.")

    # ---------------------------------------------------------------- chapitre 5
    s.page("ch5", "Chapitre 5 : Un shell", f'''
<p class="eyebrow">Chapitre 5 · environ 30 minutes</p>
<h1>Un <b>shell</b></h1>
<p class="lede">La partie que les gens utilisent vraiment : une invite où vous tapez des commandes et où votre OS répond. Vous avez toutes les pièces ; il ne reste qu’à les assembler.</p>

<h2>L’<b>idée</b></h2>
<p>Un shell est une boucle : <b>afficher une invite → lire une ligne → la découper en une commande et ses arguments → trouver la commande → l’exécuter</b>. Une table de <code>{{nom, texte d’aide, fonction}}</code> rend l’ajout de commandes facile : une ligne chacune.</p>
<p>Éteindre ou redémarrer l’ordinateur, c’est aussi du matériel : QEMU s’éteint quand on écrit <code>0x2000</code> sur le port <code>0x604</code>, et tout PC redémarre quand on envoie <code>0xFE</code> au contrôleur du clavier sur le port <code>0x64</code>.</p>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>Le shell</h3>{s.prompt('''
Chapitre 5. Écris src/shell.c et shell.h avec shell_run() : affiche une invite en couleur avec le nom de l’OS, lis une ligne avec input_getc (gère Retour arrière, ignore les autres touches de contrôle, 127 caractères au maximum, affiche ce qui est tapé), sépare la commande de ses arguments, et cherche-la dans une table de commandes {nom, texte d’aide, fonction}.

Commandes : help (liste toutes les commandes avec leur aide, alignées), clear, echo <texte>, about (nom de l’OS, version, temps écoulé), uptime (hh:mm:ss), color <nom> (change la couleur du texte), reboot (contrôleur du clavier, 0xFE sur le port 0x64), shutdown (outw(0x604, 0x2000) pour QEMU, puis arrêt) et crash (exécute ud2 pour afficher l’écran de panique). Une commande inconnue affiche un court message. Garde les noms des commandes et les messages de l’OS en anglais.

Mets le nom et la version de l’OS dans src/os.h. kernel_main appelle shell_run() après avoir tout préparé.''')}
{s.code("make run")}<p>Tapez <code>help</code>, puis essayez chaque commande.</p></li>
<li><h3>Inventez vos propres commandes</h3><p>Choisissez-en une ou deux, et demandez-les à votre IA une par une :</p>
<ul><li><b>calc 12 * 7</b> : une calculatrice pour les nombres entiers.</li><li><b>Un historique des commandes</b> avec la flèche du haut.</li><li><b>guess</b> : un jeu du nombre mystère, avec les ticks du minuteur comme hasard.</li><li><b>banner hello</b> : du texte en grosses lettres.</li><li><b>time</b> : la vraie date et l’heure, lues dans l’horloge du PC (la RTC du CMOS, ports <code>0x70</code>/<code>0x71</code>).</li></ul></li>
</ol>
<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li><code>help</code> liste vos commandes et chacune fonctionne.</li><li><code>shutdown</code> ferme QEMU ; <code>crash</code> affiche l’écran de panique.</li><li>Vous avez ajouté au moins une commande de votre cru.</li></ul>
{s.ref(["os/src/shell.c", "os/src/os.h", "os/src/kernel.c"])}
{s.save("Chapitre 5 : un shell avec des commandes")}
''', "Un shell avec une table de commandes, le redémarrage et l’arrêt.")

    # ---------------------------------------------------------------- chapitre 6
    s.page("ch6", "Chapitre 6 : La mémoire", f'''
<p class="eyebrow">Chapitre 6 · environ 40 minutes</p>
<h1>La <b>mémoire</b></h1>
<p class="lede">Les programmes ont besoin de mémoire, et c’est l’OS qui la distribue. Vous découvrez combien de RAM a le PC, quelles parties sont libres, et vous écrivez un allocateur qui en distribue des morceaux.</p>

<h2>L’<b>idée</b></h2>
<ul>
<li>Toutes les adresses ne sont pas de la RAM utilisable : le premier mégaoctet contient le BIOS et l’écran, certaines zones appartiennent au matériel, et votre noyau lui-même se trouve à 1 Mio. Le chargeur d’amorçage nous donne une <b>carte de la mémoire</b> : une liste de zones, chacune marquée utilisable (type 1) ou non. <code>boot.S</code> la transmet déjà à <code>kernel_main</code>.</li>
<li>On découpe la mémoire en <b>pages</b> de 4 Kio et on tient un <b>bitmap</b> : un bit par page, 1 = utilisée, 0 = libre. 128 Mio font 32 768 pages : tout le bitmap tient dans 4 Kio.</li>
<li><code>linker.ld</code> définit <code>kernel_end</code>, la première adresse après notre noyau, pour ne jamais distribuer notre propre code.</li>
<li>Pour les petits objets, on ajoute un <b>tas</b> (heap) avec <code>kmalloc</code>. Le plus simple donne juste les octets libres suivants et ne les reprend jamais. Les vrais font mieux : ce peut être votre défi.</li>
<li>Attention : diviser des nombres 64 bits sur un processeur 32 bits demande une bibliothèque d’aide que nous n’avons pas. Utilisez des décalages (<code>&gt;&gt; 12</code> veut dire « diviser par 4096 »).</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>L’allocateur de pages</h3>{s.prompt('''
Chapitre 6. kernel_main reçoit le nombre magique multiboot et un pointeur vers les informations multiboot. Écris src/memory.c et memory.h : définis struct multiboot_info et la structure d’une entrée de la carte mémoire (packed). Dans memory_init : marque toutes les pages comme utilisées, puis libère les pages de chaque zone de type 1 de la carte mémoire (bit 6 des flags ; à défaut de carte, utilise mem_upper), puis marque de nouveau comme utilisés le premier Mio et le noyau (jusqu’au symbole kernel_end de linker.ld). Utilise un bitmap d’un bit par page de 4 Kio, pour 512 Mio au maximum. N’utilise pas de division 64 bits.

Ajoute page_alloc() (renvoie l’adresse d’une page libre, ou 0), page_free(), pages_total() et pages_used(). Ajoute un kmalloc « bump » sur un tas statique de 64 Kio, aligné sur 16 octets. Affiche « [ OK ] Memory: N MiB found » au démarrage, et ajoute les commandes de shell mem (les totaux) et alloc (prend une page et affiche son adresse).''')}
{s.code("make run")}<p>Lancez <code>mem</code>, puis <code>alloc</code> plusieurs fois.</p></li>
<li><h3>Jouez avec</h3><p>Dans le <code>Makefile</code>, remplacez <code>-m 128M</code> par <code>-m 256M</code> et relancez : <code>mem</code> doit suivre. Demandez à votre IA d’ajouter une commande <code>memmap</code> qui liste chaque zone de la carte mémoire avec son type.</p></li>
<li><h3>Comprenez-la</h3><p>Demandez à votre IA : Que contient le premier mégaoctet ? Pourquoi les pages font-elles 4 Kio ? Qu’apporterait la <b>pagination</b> (paging, la prochaine grande étape d’un vrai OS) ?</p></li>
</ol>
<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>Le démarrage affiche environ <code>127 MiB found</code> avec <code>-m 128M</code>.</li><li><code>alloc</code> donne une nouvelle adresse à chaque fois, au-dessus de la fin de votre noyau.</li></ul>
<div class="note"><p><b>« undefined symbol: __udivdi3 »</b> (ou <code>__umoddi3</code>) : une division 64 bits s’est glissée quelque part. Remplacez-la par un décalage, ou convertissez d’abord en 32 bits.</p></div>
{s.ref(["os/src/memory.h", "os/src/memory.c", "os/linker.ld"])}
{s.save("Chapitre 6 : carte mémoire, allocateur de pages et kmalloc")}
''', "La carte mémoire multiboot, un allocateur de pages par bitmap et un kmalloc simple.")

    # ---------------------------------------------------------------- chapitre 7
    s.page("ch7", "Chapitre 7 : Un bureau avec des fenêtres", f'''
<p class="eyebrow">Chapitre 7 · environ 40 minutes</p>
<h1>Un bureau <b>avec des fenêtres</b></h1>
<p class="lede">Le plus amusant. Un bureau avec une barre en haut, une horloge et deux fenêtres que vous pouvez déplacer, le tout dessiné avec des caractères texte, comme les premières versions de nombreux systèmes célèbres.</p>
{DESKTOP.format(label="Le bureau : un fond bleu texturé, une barre en haut et deux fenêtres")}
<p><small>Une esquisse raccourcie du vrai bureau.</small></p>

<h2>L’<b>idée</b></h2>
<ul>
<li>La police VGA (code page 437) a des <b>caractères de dessin de boîtes</b> : <code>0xC9</code> est ╔, <code>0xCD</code> est ═, <code>0xB0</code> est ░… De quoi dessiner des fenêtres.</li>
<li><b>Double tampon</b> (double buffering) : on dessine d’abord toute l’image dans un tableau, puis on la copie d’un coup dans <code>0xB8000</code>. Dessiner directement à l’écran ferait clignoter l’image.</li>
<li>Une <b>boucle d’événements</b> : on regarde s’il y a une touche sans attendre (<code>input_poll</code>), on met à jour l’état (quelle fenêtre est active, où elle se trouve), on redessine, et on dort avec <code>hlt</code> quand il n’y a rien à faire. On redessine quelques fois par seconde pour que l’horloge avance.</li>
<li>On dessine d’abord la fenêtre inactive et la fenêtre active en dernier, pour qu’elle soit au-dessus.</li>
</ul>

<h2>À <b>vous</b></h2>
<ol class="steps">
<li><h3>Le bureau</h3>{s.prompt('''
Chapitre 7. Ajoute src/desktop.c avec desktop_run(), lancée par une nouvelle commande de shell « desktop ». Dessine dans un tampon uint16_t de la taille de l’écran, puis copie-le d’un coup dans la mémoire VGA. Sauvegarde l’écran avant et restaure-le en sortant.

Dessine : un fond texturé (caractère 0xB0), une barre en haut avec le nom de l’OS à gauche et le temps écoulé à droite, une barre en bas avec les touches, et deux fenêtres avec une ombre. Utilise des doubles traits et un titre cyan pour la fenêtre active, des traits simples pour l’autre. Une fenêtre affiche un texte de bienvenue, l’autre des informations système en direct : temps écoulé, mémoire, pages libres et nombre de touches appuyées. Ajoute keyboard_presses() à keyboard.c pour cela.

Touches : Tab change de fenêtre active, les flèches ou WASD la déplacent (en la gardant à l’écran), Échap revient au shell. Utilise input_poll et redessine à chaque touche et 4 fois par seconde, dors avec hlt sinon. Cache le curseur clignotant tant que le bureau est ouvert. Garde les textes affichés par l’OS en anglais.''')}
{s.code("make run")}<p>Tapez <code>desktop</code>. Appuyez sur <kbd>Tab</kbd>, déplacez les fenêtres avec les flèches, <kbd>Échap</kbd> pour revenir.</p></li>
<li><h3>Personnalisez-le</h3><p>Demandez un changement à la fois : vos propres couleurs, une troisième fenêtre (une horloge, un bloc-notes, une liste de tâches), un « menu Démarrer » sur une touche, ou un petit jeu dans une fenêtre. Un <b>snake</b> s’y prête bien : il n’a besoin que des flèches, du minuteur et de l’écran.</p></li>
</ol>
<div class="note"><p><b>Vous utilisez <code>make run-serial</code> ?</b> Le bureau est dessiné à l’écran, pas envoyé sur le port série : vous ne le verrez pas là. Utilisez <code>make run</code> ou <code>make run-text</code>.</p></div>
<h2>Ça marche <b>quand</b></h2>
<ul class="checks"><li>L’horloge de la barre du haut avance toute seule.</li><li>Tab et les flèches fonctionnent, et les fenêtres restent à l’écran.</li><li>Échap ramène le shell exactement comme il était.</li></ul>
{s.ref(["os/src/desktop.c", "os/src/shell.h"])}
{s.save("Chapitre 7 : un bureau en mode texte avec des fenêtres")}
''', "Un bureau en mode texte avec des fenêtres mobiles, un double tampon et une boucle d’événements.")

    # ---------------------------------------------------------------- chapitre 8
    s.page("ch8", "Chapitre 8 : À vous de jouer, et partagez-le", f'''
<p class="eyebrow">Chapitre 8 · autant que vous voulez</p>
<h1>À vous de jouer, <b>et partagez-le</b></h1>
<p class="lede">Vous avez un système d’exploitation qui fonctionne : un démarrage, des pilotes, un écran de plantage, un shell, un allocateur de mémoire et un bureau. Donnez-lui un nom, ajoutez la fonction dont vous rêvez, et montrez-le au club.</p>

<h2>Donnez-lui <b>un nom</b></h2>
<p>Changez <code>OS_NAME</code> dans <code>src/os.h</code>, et demandez à votre IA un nouveau logo en ASCII art avec ce nom.</p>

<h2>Des idées, <b>de la plus facile à la plus dure</b></h2>
<table>
<thead><tr><th>Idée</th><th>Ce que vous apprenez</th></tr></thead>
<tbody>
<tr><td><b>Des thèmes</b> : une commande <code>theme</code> qui recolore le shell et le bureau</td><td>Les couleurs VGA</td></tr>
<tr><td><b>La vraie date et l’heure</b>, lues dans l’horloge du PC, dans la barre du haut</td><td>La RTC du CMOS (ports 0x70/0x71)</td></tr>
<tr><td><b>Un clavier AZERTY</b> et une commande <code>layout</code></td><td>Les scancodes</td></tr>
<tr><td><b>Un OS en français</b> : traduisez les messages et les commandes, avec les accents de la code page 437</td><td>Les jeux de caractères</td></tr>
<tr><td><b>Un jeu</b> : snake, pong ou 2048 dans une fenêtre</td><td>Boucle de jeu, minuteur, hasard</td></tr>
<tr><td><b>Un bloc-notes</b> qui garde des notes tant que l’OS tourne</td><td><code>kmalloc</code>, chaînes de caractères</td></tr>
<tr><td><b>Du son</b> : un bip au démarrage avec le haut-parleur du PC (lancez QEMU avec <code>-audiodev</code> et <code>-machine pcspk-audiodev=…</code>)</td><td>Le canal 2 du PIT</td></tr>
<tr><td><b>Un meilleur tas</b> avec <code>kfree</code></td><td>Listes de blocs libres, fragmentation</td></tr>
<tr><td><b>La pagination</b> : donnez au noyau sa propre vue de la mémoire</td><td>Tables de pages, CR3, défauts de page</td></tr>
<tr><td><b>Le multitâche</b> : deux tâches qui se relaient sur le minuteur</td><td>Changements de contexte, ordonnancement</td></tr>
<tr><td><b>Le mode graphique</b> : des pixels au lieu de caractères</td><td>Framebuffers (chargeurs comme GRUB ou Limine)</td></tr>
</tbody></table>
{s.prompt('''
J’ai terminé les 8 chapitres du tutoriel. Je veux ajouter : [VOTRE IDÉE]. Explique d’abord comment cela fonctionne sur le vrai matériel d’un PC et quelles parties de mon OS doivent changer. Puis découpe le travail en 3 à 5 petites étapes que je peux tester une par une, et ne fais que la première.''')}
<p>Quand vous serez allé plus loin que ce tutoriel, le <a href="https://wiki.osdev.org/Expanded_Main_Page">wiki OSDev</a> (en anglais) est l’endroit où les vrais créateurs d’OS amateurs apprennent. Des projets comme SerenityOS ont commencé exactement là où vous en êtes.</p>

<h2>Mettez-le <b>sur GitHub</b></h2>
<p>Avec la CLI GitHub (<span class="only-mac"><code>brew install gh</code></span><span class="only-win"><code>sudo apt install gh</code></span>, puis <code>gh auth login</code>), dans votre dossier <code>my-os</code> :</p>
{s.code('gh repo create my-os --public --source . --push')}
<p>Ou créez un dépôt vide sur github.com et suivez ses étapes « push an existing repository ». Puis faites une capture d’écran de votre bureau et ajoutez-la à votre <code>README.md</code>.</p>

<h2>Montrez-le <b>au club</b></h2>
<ul>
<li>Apportez-le à une séance du jeudi et montrez-le. Deux minutes suffisent : ce que vous avez ajouté, et ce qui a été difficile.</li>
<li>Postez votre capture d’écran et le lien de votre dépôt dans le groupe WhatsApp du club.</li>
<li>Vous voulez le voir sur le site du club ? Demandez à un organisateur de l’ajouter à la <a href="https://aivancity-tech-club.github.io/showcase">vitrine des applications des étudiants</a>.</li>
</ul>
''', "Des idées pour enrichir votre OS, des thèmes au multitâche, et comment le partager.")

    # ---------------------------------------------------------------- aide
    s.page("help", "Bloqué ? Aide et glossaire", f'''
<p class="eyebrow">Aide</p>
<h1>Bloqué ? <b>Commencez ici</b></h1>
<p class="lede">Presque tous les problèmes sont dans le tableau ci-dessous. Sinon, posez la question à votre IA de la bonne façon, ou demandez en salle.</p>

<h2>Demandez à votre IA <b>de la bonne façon</b></h2>
{s.prompt('''
Je suis au chapitre [N] du tutoriel « Construisez votre OS » (x86 32 bits, multiboot, clang + ld.lld, QEMU, pas de bibliothèque C : voir AGENTS.md).
J’ai modifié : [QUELS FICHIERS, QUOI].
J’ai lancé : [LA COMMANDE].
Je m’attendais à : [CE QUI DEVRAIT SE PASSER].
À la place, je vois : [CE QUI SE PASSE, AVEC L’ERREUR COMPLÈTE OU LES DERNIÈRES LIGNES AFFICHÉES].
Explique d’abord ce que veut dire l’erreur, puis donne-moi la plus petite correction possible.''')}
<p>L’erreur complète compte : collez tout, à partir de la première ligne en rouge. Pour les plantages, collez l’écran de panique ou la sortie de la commande <code>-d int,cpu_reset</code> ci-dessous.</p>

<h2>Problèmes <b>fréquents</b></h2>
<table>
<thead><tr><th>Vous voyez</th><th>Ce que cela veut dire et que faire</th></tr></thead>
<tbody>
<tr><td><code>clang: command not found</code> ou <code>ld.lld: No such file</code></td><td>Les outils ne sont pas installés ou pas trouvés. Mac : <code>brew install llvm lld</code>. Windows : lancez dans Ubuntu la ligne <code>sudo apt install …</code> de l’installation. Vérifiez que vous êtes bien dans la fenêtre Ubuntu, pas dans PowerShell.</td></tr>
<tr><td>Des erreurs sur <code>i686-elf</code> ou <code>ld.lld</code> sur Mac</td><td>C’est probablement le clang d’Apple qui est utilisé. Lancez <code>brew install llvm lld</code> ; le Makefile trouvera alors tout seul la version de Homebrew.</td></tr>
<tr><td><code>make: *** No targets specified</code> ou <code>No rule to make target</code></td><td>Vous n’êtes pas dans le dossier de votre OS. Lancez <code>cd ~/my-os</code>.</td></tr>
<tr><td><code>undefined symbol: memset</code> / <code>memcpy</code></td><td>Le compilateur s’en sert pour les grosses copies. Écrivez-les dans <code>src/string.c</code> (chapitre 2).</td></tr>
<tr><td><code>undefined symbol: __udivdi3</code> / <code>__umoddi3</code></td><td>Une division ou un <code>%</code> sur 64 bits. Utilisez un décalage, ou des nombres 32 bits.</td></tr>
<tr><td><code>fatal error: 'stdio.h' file not found</code></td><td>Il n’y a pas de bibliothèque C dans un noyau. Utilisez votre propre <code>kprintf</code>. Seuls <code>stdint.h</code>, <code>stddef.h</code>, <code>stdbool.h</code> et <code>stdarg.h</code> existent.</td></tr>
<tr><td>QEMU affiche <code>Error loading uncompressed kernel without PVH ELF Note</code></td><td>QEMU n’a pas trouvé l’en-tête multiboot. Vérifiez que <code>.multiboot</code> vient en premier dans <code>linker.ld</code>, que le nombre magique est juste et que vous avez compilé pour <code>i686</code> (32 bits).</td></tr>
<tr><td>QEMU s’ouvre et se ferme aussitôt</td><td>Une triple faute (un plantage pendant le traitement d’un plantage). Voir plus bas.</td></tr>
<tr><td>Taper ne fait rien</td><td>Cliquez d’abord dans la fenêtre QEMU. Puis vérifiez <code>sti</code>, que l’IRQ 1 est démasquée, et l’End Of Interrupt (chapitre 4).</td></tr>
<tr><td>Les lettres ne sont pas à leur place</td><td>Votre clavier est en AZERTY et la table est en QWERTY. C’est normal ; voir le défi du chapitre 4.</td></tr>
<tr><td>Pas de fenêtre QEMU sous Windows</td><td>Windows 10 ne sait pas afficher les fenêtres des applications Linux. Utilisez <code>make run-text</code>. Sous Windows 11, lancez <code>wsl --update</code> dans PowerShell, puis <code>wsl --shutdown</code>, et rouvrez Ubuntu.</td></tr>
<tr><td>Coincé dans <code>make run-text</code></td><td>Appuyez sur <kbd>Échap</kbd> puis <kbd>2</kbd>, tapez <code>quit</code>, <kbd>Entrée</kbd>. Ou fermez le terminal.</td></tr>
<tr><td>La souris est bloquée dans la fenêtre QEMU</td><td>Appuyez sur <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>G</kbd> (Mac : <kbd>Ctrl</kbd> <kbd>⌥</kbd> <kbd>G</kbd>).</td></tr>
<tr><td>Ça marchait avant et maintenant c’est cassé</td><td><code>git diff</code> montre ce qui a changé depuis votre dernier enregistrement. <code>git restore .</code> y revient (et jette les modifications).</td></tr>
</tbody></table>

<h3>Voir pourquoi QEMU a planté</h3>
{s.code("qemu-system-i386 -kernel build/kernel.elf -no-reboot -d int,cpu_reset 2>&1 | tail -40")}
<p>Les dernières lignes montrent les interruptions juste avant le redémarrage. <code>v=0d</code> est une faute de protection générale, <code>v=0e</code> un défaut de page, <code>v=08</code> une double faute. Collez-les à votre IA avec les fichiers que vous avez modifiés.</p>
<h3>Trouver la ligne qui a planté</h3>
<p>Prenez l’<code>eip</code> de l’écran de panique et demandez aux outils dans quelle fonction il se trouve :</p>
{s.code('''"$(brew --prefix llvm)/bin/llvm-addr2line" -f -e build/kernel.elf 0x00101234''', os="mac")}
{s.code('''addr2line -f -e build/kernel.elf 0x00101234     # s’il manque : sudo apt install binutils''', os="win")}

<h2><b>Glossaire</b></h2>
<table><tbody>
<tr><th>Noyau (kernel)</th><td>Le cœur d’un OS : le code qui contrôle le matériel et fait tourner tout le reste.</td></tr>
<tr><th>Chargeur d’amorçage</th><td>Le petit programme (bootloader) qui charge le noyau en mémoire et le démarre. Le nôtre est intégré à QEMU.</td></tr>
<tr><th>Multiboot</th><td>Une façon standard pour un chargeur de trouver et démarrer un noyau : un nombre magique et quelques options.</td></tr>
<tr><th>QEMU</th><td>Un programme qui se fait passer pour un PC entier, pour que votre OS tourne dans une fenêtre.</td></tr>
<tr><th>Freestanding</th><td>Du code C sans système d’exploitation ni bibliothèque C en dessous.</td></tr>
<tr><th>Script de l’éditeur de liens</th><td>Indique à l’éditeur de liens (linker) où chaque partie du programme va en mémoire.</td></tr>
<tr><th>Pile (stack)</th><td>La mémoire où le C garde les variables locales et les adresses de retour. Elle grandit vers le bas.</td></tr>
<tr><th>Mode texte VGA</th><td>L’écran vu comme 80 × 25 caractères en mémoire, à <code>0xB8000</code>.</td></tr>
<tr><th>Port d’E/S</th><td>Un numéro pour parler à un périphérique avec <code>inb</code>/<code>outb</code>, distinct des adresses mémoire.</td></tr>
<tr><th>Port série</th><td>COM1 : envoie du texte octet par octet. QEMU le relie à votre terminal.</td></tr>
<tr><th>Interruption</th><td>Un signal qui fait s’arrêter le processeur pour exécuter un gestionnaire, puis continuer.</td></tr>
<tr><th>Exception</th><td>Une interruption levée par le processeur parce que le code a fait une erreur (0–31).</td></tr>
<tr><th>IRQ</th><td>Une demande d’interruption venant d’un périphérique : 0 est le minuteur, 1 le clavier.</td></tr>
<tr><th>GDT</th><td>Global Descriptor Table : les segments de mémoire. Nous en définissons deux qui couvrent tout.</td></tr>
<tr><th>IDT</th><td>Interrupt Descriptor Table : quel gestionnaire s’exécute pour chaque interruption.</td></tr>
<tr><th>PIC</th><td>La puce qui rassemble les IRQ du matériel et les transmet au processeur.</td></tr>
<tr><th>PIT</th><td>La puce minuteur qui bat au rythme que nous choisissons.</td></tr>
<tr><th>Scancode</th><td>Le numéro qu’envoie un clavier pour la position d’une touche.</td></tr>
<tr><th>Page</th><td>Un bloc de 4 Kio de mémoire, l’unité que l’OS distribue.</td></tr>
<tr><th>Allocateur par bitmap</th><td>Garde un bit par page pour savoir lesquelles sont libres.</td></tr>
<tr><th>Tas / kmalloc</th><td>D’où viennent les petits morceaux de mémoire quand le noyau en demande.</td></tr>
<tr><th>Triple faute</th><td>Un plantage pendant le traitement d’un plantage pendant le traitement d’un plantage. Le processeur redémarre.</td></tr>
<tr><th>Vibe coding</th><td>Construire en décrivant ce que l’on veut à une IA, en exécutant le résultat et en la guidant.</td></tr>
</tbody></table>
''', "Les problèmes fréquents en construisant l’OS, comment demander de l’aide à votre IA, et un glossaire.")
