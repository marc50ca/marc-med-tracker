# Contributing to Marc Med Tracker

Thank you for considering contributing to Marc Med Tracker! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Home Assistant version**
- **Integration version**
- **Description of the issue**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Relevant log entries**
- **Configuration (sanitized)**

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear description** of the enhancement
- **Use case** - why is this needed?
- **Expected behavior**
- **Alternative solutions** you've considered

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

#### Pull Request Guidelines

- Follow the existing code style
- Update documentation as needed
- Add tests if applicable
- Ensure all tests pass
- Keep commits focused and atomic
- Write clear commit messages

## Code Style

### Python Code

- Follow PEP 8 style guide
- Use type hints (modern Python 3.11+ style)
- Add docstrings to all functions and classes
- Use `from __future__ import annotations`
- Keep lines under 100 characters when possible

Example:
```python
from __future__ import annotations

from homeassistant.core import HomeAssistant

async def my_function(hass: HomeAssistant, data: dict[str, Any]) -> bool:
    """Do something useful.
    
    Args:
        hass: Home Assistant instance
        data: Configuration data
        
    Returns:
        True if successful
    """
    # Implementation here
    return True
```

### YAML Files

- Use 2 spaces for indentation
- No tabs
- Keep consistent formatting
- Add comments for complex sections

### Documentation

- Use Markdown format
- Keep lines under 100 characters
- Use code blocks for examples
- Add table of contents for long documents
- Include practical examples

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/marc-med-tracker.git
   cd marc-med-tracker
   ```

2. **Set up Home Assistant dev environment:**
   ```bash
   # Install Home Assistant in dev mode
   pip install homeassistant
   
   # Or use a development container
   # See: https://developers.home-assistant.io/docs/development_environment
   ```

3. **Link integration to test instance:**
   ```bash
   ln -s $(pwd)/marc_med_tracker /path/to/config/custom_components/
   ```

4. **Make your changes**

5. **Test thoroughly:**
   - Test installation
   - Test all services
   - Test automations
   - Test with different configurations
   - Check logs for errors

## Testing Checklist

Before submitting a PR, verify:

- [ ] Integration loads without errors
- [ ] All services work as expected
- [ ] Configuration validation works
- [ ] Sensors update correctly
- [ ] Binary sensors toggle properly
- [ ] Data persists across restarts
- [ ] No errors in logs
- [ ] Documentation updated
- [ ] Examples work

## Documentation Updates

When adding features:

- Update README.md
- Add to relevant guides
- Include automation examples
- Update OVERVIEW.md if adding services
- Add troubleshooting entries if needed

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes

## Questions?

- Open an issue for discussion
- Check existing documentation
- Review closed issues for similar questions

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions
- Help others learn

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
