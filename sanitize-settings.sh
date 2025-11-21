#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd "$ROOT_DIR"

SANITIZER_SCRIPT=".github/scripts/sanitize.py"
DEFAULT_GLOBS=(
  ".configs/**/*.json"
  "mai-advisor-mcp/.configs/**/*.json"
)

TARGETS=()

if [[ $# -gt 0 ]]; then
  TARGETS=("$@")
else
  PATTERN_INPUT=$(printf '%s\n' "${DEFAULT_GLOBS[@]}")
  while IFS= read -r path; do
    [[ -z "$path" ]] && continue
    TARGETS+=("$path")
  done < <(TARGET_PATTERNS="$PATTERN_INPUT" python3 - <<'PY'
import glob
import os

patterns = [line.strip() for line in os.environ["TARGET_PATTERNS"].splitlines() if line.strip()]
seen = set()
for pattern in patterns:
    for path in glob.glob(pattern, recursive=True):
        if path not in seen:
            seen.add(path)
            print(path)
PY
  )
fi

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  printf 'No JSON files matched patterns:\n  - %s\n' "${DEFAULT_GLOBS[@]}"
  exit 0
fi

echo "Sanitizing ${#TARGETS[@]} file(s)..."
python3 "$SANITIZER_SCRIPT" "${TARGETS[@]}"
