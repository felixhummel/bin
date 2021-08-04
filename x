#!/bin/bash
set -euo pipefail

path="$1"

if [[ -d "$path" ]]; then
  thunar "$path"
  exit 0
fi

# https://stackoverflow.com/a/965072/241240
filename=$(basename -- "$path")  # without path
extension="${filename##*.}"

case "$extension" in
  "flac")
    vlc "$path"
    ;;
  "*")
    echo not implemented >&2
    exit 1
    ;;
esac
