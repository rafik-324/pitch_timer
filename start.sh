#!/bin/sh
# Startet den Pitch Timer auf 127.0.0.1 und öffnet den Browser.
cd "$(dirname "$0")" || exit 1

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Python wurde nicht gefunden. Bitte Python 3 installieren." >&2
  exit 1
fi

# macOS: Bildschirm wach halten, solange der Server läuft (zusätzlich zur Wake Lock API im Browser)
if command -v caffeinate >/dev/null 2>&1; then
  caffeinate -d -w $$ &
fi

exec "$PYTHON" serve.py "$@"
