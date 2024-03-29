from unittest import TestCase
import jinja2


class MathTest(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_mul(self):
        self.assertEqual(2 * 5, 10)


class StringTest(TestCase):
    def test_stringcase(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Bar'.isupper())


if __name__ == '__main__':
    unittest.main()
