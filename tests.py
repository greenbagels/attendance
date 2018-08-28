#!/usr/bin/env python3

import os
import re
import unittest


class ReadmeTests(unittest.TestCase):
    """Unit tests for README.md"""
    
    def test_readme_file_exists(self):
        self.assertTrue(os.path.exists('README.md'))
        
    def test_readme_matches_regexp(self):
        with open('README.md') as fh:
            contents = fh.read()

        self.assertTrue(
            re.match(
                '(.*)It has been \d+ day(s?) since I missed a class(.*)',
                contents
            )
        )


if __name__ == '__main__':
    unittest.main()
