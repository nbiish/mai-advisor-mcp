# GitHub Actions Workflows

This directory contains automated workflows for the MAI Advisor MCP project.

## Workflows

### 1. Auto-Sanitize Secrets (`auto-sanitize.yml`)
**Triggers:** Push/PR to main, dev, staging branches when `.configs/**/*.json` files change

**Purpose:** Automatically sanitizes API keys and sensitive paths from settings.json files before they're committed.

**What it does:**
- Scans `mai-advisor-mcp/.configs/` for settings.json files
- Replaces API keys with placeholders:
  - `BRAVE_API_KEY` → `YOUR_BRAVE_API_KEY_HERE`
  - `TAVILY_API_KEY` → `YOUR_TAVILY_API_KEY_HERE`
- Replaces absolute paths with generic placeholders
- Auto-commits sanitized files if secrets are found
- Comments on PRs when sanitization occurs

### 2. Pre-Commit Secret Detection (`detect-secrets.yml`)
**Triggers:** Push/PR to main, dev, staging branches

**Purpose:** Prevents secrets from being committed to the repository.

**What it does:**
- Runs TruffleHog OSS to detect verified secrets
- Runs Gitleaks for comprehensive secret scanning
- Checks for custom patterns:
  - Brave API keys (BSA...)
  - Tavily API keys (tvly-...)
  - Personal filesystem paths
  - Embedded API keys in URLs
- Blocks PRs if secrets are detected
- Comments on PRs with remediation steps

### 3. Secret Scanning Legacy (`secret-scan.yml`)
**Triggers:** Manual only (workflow_dispatch)

**Purpose:** Reference implementation, can be deleted.

**Note:** This workflow is replaced by `detect-secrets.yml` and `auto-sanitize.yml`.

## Local Development

### Before Committing Configuration Files

Run the sanitization script locally:

```bash
./sanitize-settings.sh
```

This will:
1. Backup your settings.json files
2. Remove API keys and personal paths
3. Show what changed so you can review
4. Prepare files for safe commit

### Setting Up Your Configuration

1. Copy the template:
   ```bash
   cp mai-advisor-mcp/.configs/MCP/settings.json.template \
      mai-advisor-mcp/.configs/MCP/settings.json
   ```

2. Add your API keys and paths to the local file

3. **Never commit the file with real secrets** - run `./sanitize-settings.sh` first

### Required Secrets

These workflows use GitHub's default `GITHUB_TOKEN` which is automatically provided. No additional secrets configuration is needed.

## How to Use

### Automatic Protection
The workflows run automatically on push/PR, so you're protected by default.

### Manual Sanitization
If you accidentally commit secrets:

1. Run locally:
   ```bash
   ./sanitize-settings.sh
   git add mai-advisor-mcp/.configs/
   git commit -m "🔒 chore: sanitize settings.json"
   git push
   ```

2. Or let the auto-sanitize workflow handle it (it will commit to your PR automatically)

### Checking Workflow Status

- View workflow runs: Repository → Actions tab
- Check PR comments for secret detection notices
- Review auto-sanitization commits (marked with `[skip ci]`)

## File Structure

```
.github/
├── workflows/
│   ├── auto-sanitize.yml      # Auto-sanitize on commit
│   ├── detect-secrets.yml     # Pre-commit detection
│   └── secret-scan.yml        # Legacy (manual only)
└── README.md                  # This file

mai-advisor-mcp/
└── .configs/
    └── MCP/
        ├── settings.json.template  # Safe template
        └── settings.json          # Your local config (gitignored)
```

## Customization

### Adding New Secret Patterns

Edit `detect-secrets.yml`:

```yaml
PATTERNS=(
  "BSA[a-zA-Z0-9]{27}"
  "tvly-[a-zA-Z0-9-]{30,}"
  "YOUR_NEW_PATTERN_HERE"
)
```

### Changing Monitored Paths

Edit the `paths:` section in workflow triggers:

```yaml
paths:
  - 'mai-advisor-mcp/.configs/**/*.json'
  - 'other/path/**/*.json'  # Add more paths
```

## Troubleshooting

**Workflow not running?**
- Check that you're pushing to main/dev/staging branches
- Verify file changes are in monitored paths

**Secrets still being committed?**
- Run `./sanitize-settings.sh` manually before committing
- Check that patterns in `detect-secrets.yml` match your secret format

**Auto-sanitize not committing?**
- Verify repository permissions allow GitHub Actions to push
- Check workflow logs in Actions tab

## Security Best Practices

1. ✅ **DO** use the template for sharing configurations
2. ✅ **DO** keep real API keys only in local settings.json
3. ✅ **DO** run sanitize script before committing
4. ✅ **DO** use environment variables for production secrets
5. ❌ **DON'T** commit real API keys or tokens
6. ❌ **DON'T** share absolute filesystem paths
7. ❌ **DON'T** disable secret scanning workflows
