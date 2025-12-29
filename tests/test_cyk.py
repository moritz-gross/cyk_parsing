import unittest

from cyk import cyk_accepts


class TestCYK(unittest.TestCase):
    def test_single_terminal(self) -> None:
        grammar = {"S": ["a"]}
        self.assertTrue(cyk_accepts("a", grammar))
        self.assertFalse(cyk_accepts("b", grammar))

    def test_wikipedia_example(self) -> None:
        grammar = {
            "S": [("A", "B"), ("B", "C")],
            "A": [("B", "A"), "a"],
            "B": [("C", "C"), "b"],
            "C": [("A", "B"), "a"],
        }
        self.assertTrue(cyk_accepts("baaba", grammar))
        self.assertFalse(cyk_accepts("bbaba", grammar))

    def test_an_bn_language(self) -> None:
        grammar = {
            "S": [("A", "B"), ("A", "X")],
            "X": [("S", "B")],
            "A": ["a"],
            "B": ["b"],
        }
        self.assertTrue(cyk_accepts("ab", grammar))
        self.assertTrue(cyk_accepts("aabb", grammar))
        self.assertTrue(cyk_accepts("aaabbb", grammar))
        self.assertFalse(cyk_accepts("aabbb", grammar))

    def test_empty_string(self) -> None:
        grammar = {"S": [""]}
        self.assertTrue(cyk_accepts("", grammar))
        self.assertFalse(cyk_accepts("a", grammar))


if __name__ == "__main__":
    unittest.main()
