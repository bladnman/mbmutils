import unittest

from context import mbmutils
import mbmutils.mu as mu


class FFuncs(unittest.TestCase):
    def test_f_left(self):
        self.assertEqual(mu.f_left("hi:there", ":"), "hi", msg="single delimiter failed")
        self.assertEqual(mu.f_left("hi:there:mom", ":"), "hi", msg="double delimiter failed")
        self.assertEqual(mu.f_left("hi:there::mom", "::"), "hi:there", msg="multi-character delimiter failed")
        self.assertEqual(mu.f_left("hi:there::mom", "bogus"), None, msg="not found failed")
        self.assertEqual(mu.f_left("hi:there::mom", "bogus", "bob"), "bob", msg="not found with default failed")

    def test_f_right(self):
        self.assertEqual(mu.f_right("hi:there", ":"), "there", msg="single delimiter failed")
        self.assertEqual(mu.f_right("hi:there:mom", ":"), "there:mom", msg="double delimiter failed")
        self.assertEqual(mu.f_right("hi:there::mom", "::"), "mom", msg="multi-character delimiter failed")
        self.assertEqual(mu.f_right("hi:there::mom", "bogus"), None, msg="not found failed")
        self.assertEqual(mu.f_right("hi:there::mom", "bogus", "bob"), "bob", msg="not found with default failed")

    def test_f_right_back(self):
        self.assertEqual(mu.f_right_back("hi:there", ":"), "there", msg="single delimiter failed")
        self.assertEqual(mu.f_right_back("hi:there:mom", ":"), "mom", msg="double delimiter failed")
        self.assertEqual(mu.f_right_back("hi:there::mom", "::"), "mom", msg="multi-character delimiter failed")
        self.assertEqual(mu.f_right_back("hi:there::mom", "bogus"), None, msg="not found failed")
        self.assertEqual(mu.f_right_back("hi:there::mom", "bogus", "bob"), "bob", msg="not found with default failed")

    def test_f_left_back(self):
        self.assertEqual(mu.f_left_back("hi:there", ":"), "hi", msg="single delimiter failed")
        self.assertEqual(mu.f_left_back("hi:there:mom", ":"), "hi:there", msg="double delimiter failed")
        self.assertEqual(mu.f_left_back("hi:there::mom", "::"), "hi:there", msg="multi-character delimiter failed")
        self.assertEqual(mu.f_left_back("hi:there::mom", "bogus"), None, msg="not found failed")
        self.assertEqual(mu.f_left_back("hi:there::mom", "bogus", "bob"), "bob", msg="not found with default failed")

    def test_f_between(self):
        self.assertEqual(mu.f_between("hi:t[here]:[mother]", "[", "]"), "here", msg="single delimiter failed")
        self.assertEqual(mu.f_between("hi:there:mother", ":", ":"), "there", msg="same delimiter failed")
        self.assertEqual(mu.f_between("hi@there$mother", "$", "@"), None, msg="out of order delims failed")
        self.assertEqual(mu.f_between("hi:there:mother", "$", "$"), None, msg="not found failed")
        self.assertEqual(mu.f_between("hi:there:mother", "$", "$", "bob"), "bob", msg="not found with default failed")

    def test_f_replace_for(self):
        self.assertEqual("hello funny world", mu.f_replace_for("hello silly world", "silly", "funny"))
        self.assertEqual("hello funny funny world", mu.f_replace_for("hello silly silly world", "silly", "funny"))
        self.assertEqual("hello silly world", mu.f_replace_for("hello silly world", "bogus", "funny"),
                         msg="not found failed")

    def test_list_index_of(self):
        full_list = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(3, mu.list_index_of(full_list, 3))
        self.assertEqual(-1, mu.list_index_of(full_list, 55))
        self.assertEqual(-1, mu.list_index_of(full_list, None))
        self.assertEqual(-1, mu.list_index_of([], 55))
        with self.assertRaises(AttributeError):
            mu.list_index_of(None, 55)  # this lint warning is expected


if __name__ == '__main__':
    unittest.main()
