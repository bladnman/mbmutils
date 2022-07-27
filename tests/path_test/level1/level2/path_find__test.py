import os
import sys
import unittest

from context import mbmutils
import mbmutils.mu as mu


class FolderPathTestCase(unittest.TestCase):
    def test_folder_find_above(self):
        res = mu.find_folder_path("test_path_level1")
        expected = "tests/path_test/level1/test_path_level1/"
        self.assertIn(expected, res)

    def test_folder_find_above_part2(self):
        res = mu.find_folder_path("/test_path_level1")
        expected = "tests/path_test/level1/test_path_level1/"
        self.assertIn(expected, res)

    def test_folder_find_above_part3(self):
        res = mu.find_folder_path("test_path_level1/")
        expected = "tests/path_test/level1/test_path_level1/"
        self.assertIn(expected, res)

    def test_folder_find_above_part4(self):
        res = mu.find_folder_path("/test_path_level1/")
        expected = "tests/path_test/level1/test_path_level1/"
        self.assertIn(expected, res)

    def test_folder_find_above_part5(self):
        res = mu.find_folder_path("level1/test_path_level1/")
        expected = "tests/path_test/level1/test_path_level1/"
        self.assertIn(expected, res)

    def test_folder_find_locally(self):
        res = mu.find_folder_path("test_path_level2")
        expected = "tests/path_test/level1/level2/test_path_level2/"
        self.assertIn(expected, res)


class FilePathTestCase(unittest.TestCase):

    def test_file_find_above(self):
        res = mu.find_file_path("test_path_root/test_file.md")
        expected = "tests/path_test/test_path_root/test_file.md"
        self.assertIn(expected, res)

    def test_file_find_locally(self):
        res = mu.find_file_path("test_path_level2/test_file.md")
        expected = "ests/path_test/level1/level2/test_path_level2/test_file.md"
        self.assertIn(expected, res)


if __name__ == '__main__':
    unittest.main()
