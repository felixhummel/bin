#!/usr/bin/env python
# encoding: utf-8

# pip install linkify-it-py mistletoe structlog
import sys

from pathlib import Path

import mistletoe
import structlog

log = structlog.get_logger()


def _replacements():
    # (7, 6), ..., (2, 1)
    pairs = zip(range(6,0,-1), range(7,1,-1))
    for a, b in pairs:
        yield f'<h{a}', f'<h{b}'
        yield f'</h{a}', f'</h{b}'

# log.info(list(_replacements()))

print("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>md</title>
    <link rel="stylesheet" type="text/css" href="https://www.felixhummel.de/css/bamboo.css">
    <style type="text/css" media="screen">
      .felix-md h1 {
        font-size: 1rem;
        border-left: 1em solid;
        padding-left: 0.3em;
      }
    </style>
</head>
<body class="felix-md">
""".strip())

files = [Path(x) for x in sys.argv[1:]]

print("""
<h1>TOC</h1>
<ol>
""".strip())
for f in files:
    print(f'<li><a href="#{f.name}">{f.name}</a></li>')
print("</ol>")

for f in files:
    rendered = mistletoe.markdown(f.read_text())
    for a, b in _replacements():
        rendered = rendered.replace(a, b)
    rendered = f'<h1 id="{f.name}">{f.name}</h1>\n{rendered}\n\n'
    print(rendered)
print("""
    </ol>
</body>
</html>
""".strip())
