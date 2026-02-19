#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-}"
VISIBILITY="${2:-public}"

if ! command -v git >/dev/null 2>&1; then
  echo "git not found. Please install git and try again." >&2
  exit 1
fi

if [ -z "$REPO_NAME" ]; then
  read -p "Enter GitHub repo name (e.g. pcl_agent): " REPO_NAME
fi

git init
git add -A
git commit -m "chore: initial commit for $REPO_NAME" || echo "No changes to commit or commit failed."

if command -v gh >/dev/null 2>&1; then
  if [ "$VISIBILITY" = "public" ]; then
    gh repo create "$REPO_NAME" --public --source=. --remote=origin --push --confirm
  else
    gh repo create "$REPO_NAME" --private --source=. --remote=origin --push --confirm
  fi
  echo "Repository created and pushed."
else
  echo "gh CLI not found. Create a repo on GitHub and run:" >&2
  echo "  git branch -M main"
  echo "  git remote add origin https://github.com/<your-username>/$REPO_NAME.git"
  echo "  git push -u origin main"
fi
