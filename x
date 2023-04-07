#!/bin/bash
set -euo pipefail

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

case "$extension" in
  pdf)
    atril "$path"
    ;;
  "flac")
    vlc "$path"
    ;;
  @(jpg|png))
    eog "$path"
    ;;
  "pbm")
    gimp "$path"
    ;;
  @(mp4|webm))
    parole "$path"
    ;;
  *)
    echo not implemented >&2
    exit 1
    ;;
esac
