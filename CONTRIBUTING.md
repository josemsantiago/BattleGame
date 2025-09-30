# Contributing to BattleGame - Dragonic Battle

Thank you for your interest in contributing to the BattleGame project! This guide outlines the process for contributing to this Python-based turn-based RPG battle game.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Development Setup

### Prerequisites
- Python 3.6 or higher
- Git for version control

### Getting Started
1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/BattleGame.git`
3. Navigate to the project directory: `cd BattleGame`
4. Test the game: `python3 battlagame.py`

## Development Workflow

### Making Changes
1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes following the coding standards below
3. Write tests for your changes
4. Ensure all tests pass: `python3 test_battlegame.py`
5. Test the game manually to ensure functionality
6. Commit your changes with descriptive messages
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Coding Standards

### Python Style Guidelines
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Include docstrings for all classes and functions
- Maintain consistent indentation (4 spaces)
- Keep functions focused and single-purpose

### Code Quality
- Write unit tests for all new functionality
- Test edge cases and error conditions
- Use meaningful test names
- Handle user input validation gracefully
- Ensure game balance when modifying stats

### Game Design Principles
- Maintain turn-based combat mechanics
- Preserve game balance between character races
- Keep user interface simple and intuitive
- Ensure fair and engaging gameplay

## Testing

### Running Tests
```bash
# Run all tests
python3 test_battlegame.py

# Manual testing
python3 battlagame.py
```

### Writing Tests
- Test all new game features
- Include edge cases for user input
- Test game balance and mechanics
- Verify error handling
- Test the complete game flow

## Types of Contributions

### Welcome Contributions
- Bug fixes and improvements
- New character races or abilities
- Enhanced combat mechanics
- Improved user interface
- Performance optimizations
- Documentation improvements
- Additional game features (items, spells, etc.)

### Game Balance Changes
- Discuss balance changes in issues first
- Provide reasoning for stat modifications
- Test thoroughly with various scenarios
- Consider impact on overall gameplay

## Feature Requests

### Suggesting New Features
- Open an issue to discuss the feature
- Explain the use case and benefit
- Consider implementation complexity
- Ensure it fits the game's design philosophy

### Examples of Potential Features
- Multiple enemy types
- Character progression/leveling
- Equipment system
- Special abilities or spells
- Save/load game functionality
- Enhanced battle animations

## Reporting Issues

### Bug Reports
- Use the GitHub issue tracker
- Include steps to reproduce the bug
- Provide expected vs actual behavior
- Include Python version and OS information
- Include any error messages

### Feature Requests
- Describe the feature clearly
- Explain why it would improve the game
- Consider backward compatibility
- Suggest implementation approach

## Code Structure

### Current Architecture
- `battlagame.py` - Main game logic and entry point
- `test_battlegame.py` - Comprehensive test suite
- Character classes with distinct attributes
- Turn-based combat system
- Input validation and error handling

### Adding New Features
- Follow existing code patterns
- Maintain separation of concerns
- Update tests for new functionality
- Update documentation as needed

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions/classes
- Include usage examples for new features
- Update this CONTRIBUTING.md if process changes

## Recognition

Contributors will be acknowledged in:
- GitHub contributor list
- Project README
- Release notes for significant contributions

## Questions and Support

- Open an issue for questions about the codebase
- Tag maintainers for urgent matters
- Check existing issues before creating new ones

## Game Design Philosophy

This project aims to:
- Demonstrate Python fundamentals through game development
- Provide an engaging yet simple gaming experience
- Maintain clean, readable, and educational code
- Balance simplicity with entertainment value

Thank you for contributing to BattleGame!