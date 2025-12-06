# Version Management

This project uses semantic versioning (MAJOR.MINOR.PATCH).

## Current Version

See the `VERSION` file or check the footer of the website.

## Bumping Version

Use the `bump_version.py` script to automatically update version numbers:

### Patch Release (Bug fixes)
```bash
python bump_version.py patch
# 1.0.0 → 1.0.1
```

### Minor Release (New features, backwards compatible)
```bash
python bump_version.py minor
# 1.0.0 → 1.1.0
```

### Major Release (Breaking changes)
```bash
python bump_version.py major
# 1.0.0 → 2.0.0
```

### Dry Run (Preview without making changes)
```bash
python bump_version.py patch --dry-run
```

## What Gets Updated

The script automatically updates:
1. `VERSION` file - The source of truth for version number
2. `Lessons/index.njk` - The version displayed in the website footer
3. Last updated date in the footer

## Workflow

```bash
# Make your changes
git add .
git commit -m "feat: Add new feature"

# Bump version (e.g., minor release)
python bump_version.py minor

# The script will tell you the next steps:
git add VERSION Lessons/index.njk
git commit -m "chore: Bump version to 1.1.0"
git push origin main
```

## Version History

- **v1.0.0** (2025-12-06) - Initial release with JWT authentication system
