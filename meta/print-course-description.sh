#!/usr/bin/env bash
# Extracts and prints Course Description from meta/syllabus.md
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYLLABUS="$DIR/syllabus.md"

if [[ ! -f "$SYLLABUS" ]]; then
  echo "Error: syllabus.md not found in $DIR"
  exit 1
fi

awk '/^## Course Description/{flag=1; next} /^---/{if(flag) exit} flag' "$SYLLABUS"
