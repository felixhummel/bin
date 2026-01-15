#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#       "linkify-it-py",
#       "mistletoe ",
#       "structlog",
# ]
# ///
import sys

from pathlib import Path

import mistletoe
import structlog

log = structlog.get_logger()


if len(sys.argv) < 2:
    log.error(f'Usage: {__file__} PATH...')
    sys.exit(1)


def _replacements():
    # (7, 6), ..., (2, 1)
    pairs = zip(range(6, 0, -1), range(7, 1, -1))
    for a, b in pairs:
        yield f'<h{a}', f'<h{b}'
        yield f'</h{a}', f'</h{b}'


# log.info(list(_replacements()))

print(
    """
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
""".strip()
)

files = []
for x in sys.argv[1:]:
    p = Path(x)
    if not p.is_file():
        log.warning('not a file', path=str(p))
        continue
    files.append(p)

print(
    """
<h1>TOC</h1>
<ol>
""".strip()
)
for f in files:
    print(f'<li><a href="#{f}">{f}</a></li>')
print('</ol>')

for f in files:
    rendered = mistletoe.markdown(f.read_text())
    for a, b in _replacements():
        rendered = rendered.replace(a, b)
    rendered = f'<h1 id="{f}">{f}</h1>\n{rendered}\n\n'
    print(rendered)
print(
    """
    </ol>
</body>
</html>
""".strip()
)
