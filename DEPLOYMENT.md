# 📦 WATBOT - PyPI Deployment Guide

## Pre-deployment Checklist

- [x] Package structure created (`watbot/` directory)
- [x] Configuration system implemented
- [x] WhatsApp bot wrapper created
- [x] CLI interface added
- [x] Examples and documentation written
- [x] setup.py configured
- [x] README.md completed
- [ ] Tests written and passing
- [ ] Version number finalized
- [ ] API keys removed from code
- [ ] GitHub repository created

## Project Structure

```
watbot/
├── watbot/                    # Main package
│   ├── __init__.py           # Package initialization
│   ├── config.py             # Configuration management
│   ├── whatsapp_bot.py       # WhatsApp bot wrapper
│   └── cli.py                # Command-line interface
├── examples/                  # Usage examples
│   ├── whatsapp_examples.py  # Python examples
│   └── config_example.json   # Config file example
├── smart_whatsapp_bot.js     # Node.js WhatsApp automation
├── gemini_bot.py             # AI response generator
├── insta_bot.py              # Instagram bot (TODO)
├── setup.py                  # Package configuration
├── requirements.txt          # Python dependencies
├── package.json              # Node.js dependencies
├── MANIFEST.in               # Package files list
├── README.md                 # Main documentation
├── QUICKSTART.md             # Quick start guide
├── LICENSE                   # MIT License
└── test_watbot.py            # Test suite

```

## Steps to Deploy to PyPI

### 1. Test Locally

```bash
# Run tests
python test_watbot.py

# Install in development mode
pip install -e .

# Test the package
python -c "from watbot import WhatsAppBot; print('✅ Import successful')"

# Test CLI
watbot version
```

### 2. Build the Package

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# - dist/watbot-0.1.0-py3-none-any.whl
# - dist/watbot-0.1.0.tar.gz
```

### 3. Test with TestPyPI (Recommended)

```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ watbot

# Test the installation
python -c "from watbot import WhatsAppBot; print('✅ TestPyPI install works')"
```

### 4. Deploy to PyPI

```bash
# Upload to real PyPI
python -m twine upload dist/*

# Enter your PyPI credentials when prompted
# Username: __token__
# Password: pypi-xxx... (your API token)
```

### 5. Verify Installation

```bash
# Install from PyPI
pip install watbot

# Test it
python -c "from watbot import WhatsAppBot; print('✅ PyPI install successful')"

# Test CLI
watbot version
```

## Post-Deployment

### 1. Create GitHub Release

```bash
# Tag the release
git tag -a v0.1.0 -m "Initial release"
git push origin v0.1.0

# Create release on GitHub
# Go to: https://github.com/nithin434/woat/releases/new
# - Tag: v0.1.0
# - Title: WATBOT v0.1.0 - Initial Release
# - Description: Include changelog and features
```

### 2. Update Documentation

- Update README with PyPI install instructions
- Add badges (version, downloads, etc.)
- Update examples to use `pip install watbot`

### 3. Announce

- Post on Reddit (r/Python, r/learnpython)
- Tweet about it
- Share on LinkedIn
- Post on Dev.to

## Version Management

### Semantic Versioning

- **0.1.0** - Initial release (Alpha)
- **0.2.0** - Instagram bot added
- **1.0.0** - Stable release
- **1.1.0** - Minor features
- **1.1.1** - Bug fixes

### Updating Version

Update version in:
1. `watbot/__init__.py` - `__version__`
2. `setup.py` - `version`

```python
# watbot/__init__.py
__version__ = "0.1.0"

# setup.py
setup(
    name="watbot",
    version="0.1.0",
    ...
)
```

## Configuration for PyPI

### PyPI Account Setup

1. Create account: https://pypi.org/account/register/
2. Enable 2FA (required)
3. Create API token: https://pypi.org/manage/account/token/
4. Save token securely

### TestPyPI Account (for testing)

1. Create account: https://test.pypi.org/account/register/
2. Create API token
3. Use for testing before production

### .pypirc Configuration (Optional)

Create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw...
```

## Troubleshooting

### "Package already exists"

Increment version number in `__init__.py` and `setup.py`

### "Invalid credentials"

- Use `__token__` as username
- Use API token (starts with `pypi-`) as password

### "Missing files in package"

Check `MANIFEST.in` and ensure all files are included

### "Import errors after install"

- Check `__init__.py` imports
- Verify all dependencies in `requirements.txt`
- Test with fresh virtual environment

## Best Practices

1. **Always test with TestPyPI first**
2. **Use API tokens, not passwords**
3. **Version numbers can't be reused**
4. **Include all necessary files in MANIFEST.in**
5. **Keep sensitive data out of the package**
6. **Write good documentation**
7. **Respond to issues quickly**
8. **Keep changelog updated**

## Maintenance

### Regular Updates

```bash
# Make changes
git add .
git commit -m "Update: description"
git push

# Update version
# Edit __init__.py and setup.py

# Rebuild
python -m build

# Upload
python -m twine upload dist/*

# Tag release
git tag -a v0.1.1 -m "Bug fixes"
git push origin v0.1.1
```

### Monitoring

- Check PyPI stats: https://pypi.org/project/watbot/
- Monitor GitHub issues
- Respond to user feedback
- Update documentation

## Resources

- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine docs: https://twine.readthedocs.io/
- Setuptools: https://setuptools.pypa.io/

---

## Quick Commands Reference

```bash
# Test locally
pip install -e .
python test_watbot.py

# Build
python -m build

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install watbot

# Test
python -c "from watbot import WhatsAppBot; print('OK')"
watbot version
```

---

Ready to deploy? Start with TestPyPI and work your way up! 🚀
