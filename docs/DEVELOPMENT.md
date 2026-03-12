# Developer Setup Guide

## Prerequisites

- Python 3.11 or later
- Git
- Home Assistant (for testing)
- Code editor (VS Code recommended)

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/marc-med-tracker.git
cd marc-med-tracker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
make install
# Or manually:
pip install -r requirements.txt
```

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_calculations.py -v
```

### Code Formatting

```bash
# Format code automatically
make format

# Check formatting without changing
make lint
```

### Validation

```bash
# Validate manifest and services
make validate
```

## Testing in Home Assistant

### Method 1: Symlink (Recommended for Development)

```bash
# Link to your HA config
ln -s $(pwd)/marc_med_tracker /path/to/config/custom_components/
```

### Method 2: Copy Files

```bash
cp -r marc_med_tracker /path/to/config/custom_components/
```

### Restart and Check Logs

```bash
# Restart Home Assistant
ha core restart

# Watch logs
ha core logs -f | grep marc_med_tracker
```

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/my-new-feature
```

### 2. Make Your Changes

- Edit code in `marc_med_tracker/`
- Update documentation in `docs/`
- Add examples in `examples/`
- Write tests in `tests/`

### 3. Test Your Changes

```bash
# Run tests
make test

# Validate code
make validate

# Format code
make format
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add my new feature"
```

### 5. Push and Create PR

```bash
git push origin feature/my-new-feature
# Then create a Pull Request on GitHub
```

## Project Structure

```
marc-med-tracker/
├── marc_med_tracker/       # Integration source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── examples/               # Example configurations
├── scripts/                # Utility scripts
└── .github/                # GitHub configs
```

## Common Tasks

### Adding a New Service

1. Add handler in `marc_med_tracker/__init__.py`
2. Add service definition in `marc_med_tracker/services.yaml`
3. Update `README.md` with usage
4. Add automation examples
5. Write tests

### Updating Documentation

1. Edit relevant file in `docs/`
2. Update `README.md` if needed
3. Add entry to `CHANGELOG.md`

### Creating a Release

1. Update version in `marc_med_tracker/manifest.json`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create and push tag:
```bash
git tag v2.0.1
git push origin v2.0.1
```
5. GitHub Actions will create the release

## Debugging Tips

### Enable Debug Logging

```yaml
# configuration.yaml
logger:
  default: info
  logs:
    custom_components.marc_med_tracker: debug
```

### Common Issues

**Integration won't load:**
- Check logs for syntax errors
- Validate manifest: `make validate`
- Ensure all required files present

**Services not appearing:**
- Check `services.yaml` syntax
- Restart Home Assistant
- Check logs for registration errors

**Sensors not updating:**
- Verify state_class and device_class
- Check sensor update logic
- Look for exceptions in logs

## Code Style Guide

### Python

- Use type hints
- Follow PEP 8
- Maximum line length: 100 characters
- Use `from __future__ import annotations`

Example:
```python
from __future__ import annotations

from homeassistant.core import HomeAssistant

async def my_function(hass: HomeAssistant, data: dict[str, Any]) -> bool:
    """Do something useful."""
    return True
```

### Documentation

- Use Markdown
- Include code examples
- Keep lines under 100 characters
- Add table of contents for long docs

## Testing Guidelines

### Test Coverage

Aim for:
- Unit tests for calculations
- Integration tests for services
- Validation tests for config

### Writing Tests

```python
def test_feature():
    """Test my feature."""
    # Arrange
    input_data = {...}
    
    # Act
    result = my_function(input_data)
    
    # Assert
    assert result == expected_value
```

## Resources

- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [Integration Development](https://developers.home-assistant.io/docs/creating_component_index/)
- [Code Style](https://developers.home-assistant.io/docs/development_guidelines/)

## Getting Help

- Check existing issues
- Ask in discussions
- Join Home Assistant Discord
- Review closed PRs for examples

## License

By contributing, you agree to license your work under the MIT License.
