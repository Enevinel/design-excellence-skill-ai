#!/usr/bin/env python3
"""Unit tests for check_contrast.py, using only Python standard library."""
import unittest
from check_contrast import assess, contrast_ratio, parse_hex, relative_luminance


class ContrastTests(unittest.TestCase):
    def test_black_white(self):
        self.assertAlmostEqual(contrast_ratio(parse_hex('#000'), parse_hex('#ffffff')), 21)

    def test_same_color(self):
        self.assertAlmostEqual(contrast_ratio(parse_hex('#4a4a4a'), parse_hex('#4a4a4a')), 1)

    def test_wcag_text_border(self):
        self.assertFalse(assess('#777777', '#ffffff', 4.5)['passes'])
        self.assertTrue(assess('#767676', '#ffffff', 4.5)['passes'])

    def test_large_text(self):
        self.assertTrue(assess('#777', '#fff', 3)['passes'])

    def test_short_hex(self):
        self.assertEqual(parse_hex('#aBc'), (170, 187, 204))

    def test_reject_alpha(self):
        with self.assertRaises(ValueError):
            parse_hex('#ffffff80')

    def test_reject_named_color(self):
        with self.assertRaises(ValueError):
            parse_hex('white')

    def test_reject_invalid_threshold(self):
        with self.assertRaises(ValueError):
            assess('#000', '#fff', 22)

    def test_known_luminance(self):
        self.assertAlmostEqual(relative_luminance(parse_hex('#fff')), 1)
        self.assertAlmostEqual(relative_luminance(parse_hex('#000')), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
