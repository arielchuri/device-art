#!/usr/bin/env bash
# Extracts Course Description from meta/syllabus.md and renders with bat (or glow)
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYLLABUS="$DIR/syllabus.md"

if [[ ! -f "$SYLLABUS" ]]; then
  echo "Error: syllabus.md not found in $DIR"
  exit 1
fi

CONTENT=$(awk '/^## Course Description/{flag=1; next} /^---/{if(flag) exit} flag' "$SYLLABUS")

if command -v bat >/dev/null 2>&1; then
  echo "$CONTENT" | bat --language=markdown --plain --paging=never
elif command -v glow >/dev/null 2>&1; then
  echo "$CONTENT" | glow -
else
  echo "$CONTENT"
fi
