#!/usr/bin/env bash
# Extracts Learning Outcomes from meta/syllabus.md and renders formatted markdown with glow
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYLLABUS="$DIR/syllabus.md"

if [[ ! -f "$SYLLABUS" ]]; then
  echo "Error: syllabus.md not found in $DIR"
  exit 1
fi

CONTENT=$(awk '/^## Learning Outcomes/{flag=1; next} /^---/{if(flag) exit} flag' "$SYLLABUS")

if command -v glow >/dev/null 2>&1; then
  echo "$CONTENT" | glow -
else
  echo "$CONTENT"
fi
