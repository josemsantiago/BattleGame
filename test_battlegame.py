#!/usr/bin/env python3
"""
Test suite for BattleGame
Tests core game mechanics and functions
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
import battlagame


class TestBattleGame(unittest.TestCase):
    """Test cases for BattleGame functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.valid_characters = ["wizard", "elf", "human", "orc"]

    def test_character_stats(self):
        """Test that character stats are properly configured."""
        self.assertIn("wizard", battlagame.CHARACTERS)
        self.assertIn("elf", battlagame.CHARACTERS)
        self.assertIn("human", battlagame.CHARACTERS)
        self.assertIn("orc", battlagame.CHARACTERS)

        # Test that each character has required stats
        for char_type in self.valid_characters:
            char = battlagame.CHARACTERS[char_type]
            self.assertIn("name", char)
            self.assertIn("damage", char)
            self.assertIn("hp", char)
            self.assertGreater(char["damage"], 0)
            self.assertGreater(char["hp"], 0)

    def test_dragon_stats(self):
        """Test dragon configuration."""
        self.assertEqual(battlagame.DRAGON_HP, 300)
        self.assertEqual(battlagame.DRAGON_DAMAGE, 50)

    @patch('builtins.input', side_effect=['1'])
    def test_get_character_choice_valid(self, mock_input):
        """Test valid character selection."""
        result = battlagame.get_character_choice()
        self.assertEqual(result, "wizard")

    @patch('builtins.input', side_effect=['wizard'])
    def test_get_character_choice_by_name(self, mock_input):
        """Test character selection by name."""
        result = battlagame.get_character_choice()
        self.assertEqual(result, "wizard")

    @patch('builtins.input', side_effect=['exit'])
    def test_get_character_choice_exit(self, mock_input):
        """Test exiting during character selection."""
        result = battlagame.get_character_choice()
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['TestHero'])
    def test_get_character_name_valid(self, mock_input):
        """Test valid character naming."""
        result = battlagame.get_character_name()
        self.assertEqual(result, "TestHero")

    @patch('builtins.input', side_effect=[''])
    def test_get_character_name_empty(self, mock_input):
        """Test empty character name defaults to 'Unnamed Hero'."""
        result = battlagame.get_character_name()
        self.assertEqual(result, "Unnamed Hero")

    @patch('builtins.input', side_effect=['exit'])
    def test_get_character_name_exit(self, mock_input):
        """Test exiting during character naming."""
        result = battlagame.get_character_name()
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['yes'])
    def test_get_replay_choice_yes(self, mock_input):
        """Test replay choice - yes."""
        result = battlagame.get_replay_choice()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['no'])
    def test_get_replay_choice_no(self, mock_input):
        """Test replay choice - no."""
        result = battlagame.get_replay_choice()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['invalid', 'yes'])
    def test_get_replay_choice_invalid_then_valid(self, mock_input):
        """Test replay choice with invalid input followed by valid."""
        result = battlagame.get_replay_choice()
        self.assertTrue(result)

    def test_battle_wizard_vs_dragon(self):
        """Test battle mechanics with wizard character."""
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            result = battlagame.battle("wizard", "TestWizard")
            # Wizard should win (150 damage vs 300 HP = 2 hits to kill dragon)
            # Dragon does 50 damage per hit, hits twice = 100 damage vs 70 HP wizard
            # But wizard attacks first, so wizard wins in 2 turns before taking lethal damage
            self.assertTrue(result)
        finally:
            sys.stdout = sys.__stdout__

    def test_battle_human_vs_dragon(self):
        """Test battle mechanics with human character."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            result = battlagame.battle("human", "TestHuman")
            # Human should lose (20 damage vs 300 HP = 15 hits, Dragon does 50*15=750 damage vs 150 HP)
            self.assertFalse(result)
        finally:
            sys.stdout = sys.__stdout__

    def test_character_data_integrity(self):
        """Test that character stats are reasonable and balanced."""
        for char_type, stats in battlagame.CHARACTERS.items():
            # All characters should have reasonable HP (between 50-200)
            self.assertGreaterEqual(stats["hp"], 50)
            self.assertLessEqual(stats["hp"], 200)

            # All characters should have reasonable damage (between 10-200)
            self.assertGreaterEqual(stats["damage"], 10)
            self.assertLessEqual(stats["damage"], 200)

            # Character names should be non-empty strings
            self.assertIsInstance(stats["name"], str)
            self.assertGreater(len(stats["name"]), 0)


class TestBattleGameIntegration(unittest.TestCase):
    """Integration tests for complete game flow."""

    @patch('builtins.input', side_effect=['1', 'TestHero', 'no'])
    def test_complete_game_flow(self, mock_input):
        """Test a complete game flow from start to finish."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            battlagame.main()
            output = captured_output.getvalue()
            self.assertIn("Thanks for playing!", output)
        finally:
            sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=['exit'])
    def test_early_exit(self, mock_input):
        """Test exiting the game early."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            battlagame.main()
            output = captured_output.getvalue()
            self.assertIn("Thanks for playing!", output)
        finally:
            sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()