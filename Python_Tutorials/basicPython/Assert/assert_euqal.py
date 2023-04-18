# assertEqual()
# when we have only 2 parameters we can use assert to check whether both are same or not. e.g.
import unittest


class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        name1 = "geeks"
        name2 = "gfg"
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(name1, name2, message)


if __name__ == '__main__':
    unittest.main()


