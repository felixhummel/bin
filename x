#!/bin/bash
set -euo pipefail

# DEPRECATED
# It is better set sane XDG defaults, e.g. for HTML files:
#     xdg-mime query filetype /tmp/index.html
#     xdg-mime query default text/html
#     xdg-mime default firefox.desktop text/html
#     xdg-mime default org.gnome.eog.desktop image/jpeg image/png

# https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Pattern-Matching
# @(patternlist) matches one of the patterns
shopt -s extglob

path="$1"

if [[ -d "$path" ]]; then
  thunar "$path"
  exit 0
fi

# https://stackoverflow.com/a/965072/241240
filename=$(basename -- "$path")  # without path
extension="${filename##*.}"

shopt -s nocasematch
case "$extension" in
  "pbm")
    gimp "$path"
    ;;
  svg)
    firefox "$path"
    ;;
  *)
    xdg-open "$path"
    ;;
esac
