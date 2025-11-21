#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd "$ROOT_DIR"

SANITIZER_SCRIPT=".github/scripts/sanitize.py"
DEFAULT_GLOB=".configs/**/*.json"

TARGETS=()

if [[ $# -gt 0 ]]; then
  TARGETS=("$@")
else
  while IFS= read -r path; do
    [[ -z "$path" ]] && continue
    TARGETS+=("$path")
  done < <(python3 - <<'PY'
import glob
for path in glob.glob(".configs/**/*.json", recursive=True):
    print(path)
PY
  )
fi

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "No JSON files matched pattern: ${DEFAULT_GLOB}"
  exit 0
fi

echo "Sanitizing ${#TARGETS[@]} file(s)..."
python3 "$SANITIZER_SCRIPT" "${TARGETS[@]}"
