#!/bin/bash
set -euo pipefail

hash zenity

sleep $1
zenity --info --text="$2"
