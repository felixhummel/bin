#!/usr/bin/env python
# encoding: utf-8
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

# log.info(list(_replacements()))

files = [Path(x) for x in sys.argv[1:]]
for f in files:
    rendered = mistletoe.markdown(f.read_text())
    for a, b in _replacements():
        rendered = rendered.replace(a, b)
    rendered = f'<h1>{f.name}</h1>\n{rendered}\n\n'
    print(rendered)
