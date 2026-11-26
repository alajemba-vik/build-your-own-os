#!/usr/bin/env python3
"""Writes the tutorial's HTML pages, in English (repository root) and French (fr/).
Edit the text in tools/content_en.py and tools/content_fr.py (the page template is in tools/pagekit.py),
then run from the repository root:  python3 tools/build_pages.py
The generated pages are committed; GitHub Pages serves them as they are (no build step on the server)."""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pagekit import Site, PAGES
import content_en, content_fr

OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
content_en.build(Site("en", OUT))
content_fr.build(Site("fr", OUT))
print("pages written:", len(PAGES), "in English,", len(PAGES), "in French (fr/)")
