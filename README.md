# BattleGame - Dragonic Battle

A turn-based console RPG battle game where players choose from different character races to fight against a powerful dragon enemy.

## Overview

This Python fundamentals project demonstrates core programming concepts through an engaging fantasy battle game. Players select from four unique character races, each with distinct stats and abilities, then engage in automatic turn-based combat against a formidable dragon opponent.

## Features

### Character Selection
Choose from four distinct character races:
- **Wizard**: Glass cannon (150 damage, 70 health) - High risk, high reward
- **Elf**: Balanced warrior (100 damage, 100 health) - Well-rounded choice
- **Human**: Tank build (20 damage, 150 health) - High survivability
- **Orc**: Powerful warrior (95 damage, 150 health) - Strong and durable

### Combat System
- **Turn-based mechanics**: Alternating attacks between player and dragon
- **Dragon enemy**: 300 HP, 50 damage per attack
- **Real-time health tracking**: Live display of both combatants' health
- **Victory conditions**: Battle continues until one combatant reaches 0 HP

### Game Features
- **Custom character naming**: Personalize your chosen race
- **Replay system**: Play multiple rounds without restarting
- **Exit functionality**: Clean exit available at any prompt
- **Input validation**: Error handling for invalid selections

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Usage

1. Run the game:
   ```bash
   python battlagame.py
   ```

2. Follow the prompts to:
   - Select your character race (by number or name)
   - Enter your character's name
   - Watch the automatic battle unfold
   - Choose to play again or exit

## Technical Implementation

### Programming Concepts Demonstrated
- **Variables and data types**: Character stats and game state
- **Conditional statements**: Race selection and game flow logic
- **Loops**: Game replay system and input validation
- **String manipulation**: User input processing and formatting
- **User input handling**: Robust input validation with error messages

### Code Structure
```python
# Global variables for character stats
wizard_damage, wizard_health = 150, 70
elf_damage, elf_health = 100, 100
human_damage, human_health = 20, 150
orc_damage, orc_health = 95, 150

# Dragon stats
dragon_health, dragon_damage = 300, 50
```

## Game Mechanics

### Battle Flow
1. Player and dragon alternate attacks
2. Damage is calculated and applied automatically
3. Health totals are displayed after each round
4. Battle continues until one combatant is defeated
5. Victory/defeat message is displayed

### Character Strategy
- **Wizard**: High damage but low health - aim for quick victories
- **Elf**: Balanced approach suitable for new players
- **Human**: Tank strategy - outlast the dragon with superior health
- **Orc**: Strong warrior with good damage and survivability

## Learning Objectives

This project demonstrates:
- Basic Python syntax and structure
- Control flow with loops and conditionals
- User input handling and validation
- String formatting and manipulation
- Game logic implementation
- Error handling and user experience design

## Educational Context

Created as a Python Fundamentals Week 1 assignment, this project provides hands-on experience with:
- Variables and data types
- Conditional logic
- Loop structures
- User interaction
- Basic game development concepts

## Future Enhancements

Potential improvements could include:
- Multiple enemy types with varying difficulties
- Character leveling and progression system
- Special abilities and magic spells
- Inventory system with weapons and armor
- Save/load game functionality
- Graphical user interface

## Author

José Santiago Echevarria
Created: May 13, 2023
Python Fundamentals Assignment
