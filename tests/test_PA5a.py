import sys
import unittest
from io import StringIO

from PA5a import main


def _letter(lines):
    return "\n" + "\n".join(lines) + "\n\n"


L_BLANK = _letter([""])

L_D = _letter([
    "*******",
    "*     *",
    "*     *",
    " *   * ",
    "  ***  ",
])

L_E = _letter([
    "*******",
    "*  *  *",
    "*  *  *",
    "*  *  *",
    "*  *  *",
])

L_H = _letter([
    "*******",
    "   *   ",
    "   *   ",
    "   *   ",
    "*******",
])

L_L = _letter([
    "*******",
    "*      ",
    "*      ",
    "*      ",
    "*      ",
])

L_O = _letter([
    "*******",
    "*     *",
    "*     *",
    "*     *",
    "*******",
])

L_R = _letter([
    "*******",
    "   *  *",
    "  **  *",
    " * ****",
    "*      ",
])

L_W = _letter([
    "*******",
    "*      ",
    "****   ",
    "*      ",
    "*******",
])


class TestPA5a(unittest.TestCase):

    def _test(self, message, result):
        input_text = message + "\n"
        expected_output = "Input message: " + result

        old_stdin, old_stdout = sys.stdin, sys.stdout
        sys.stdin = StringIO(input_text)
        sys.stdout = StringIO()

        try:
            main()
        except SystemExit:
            pass
        finally:
            actual_output = sys.stdout.getvalue()
            sys.stdin, sys.stdout = old_stdin, old_stdout

        self.assertEqual(expected_output, actual_output)

    def test_empty(self):
        self._test("a", "")
        self._test("b", "")
        self._test("c", "")
        self._test("f", "")
        self._test("g", "")
        self._test("i", "")
        self._test("j", "")
        self._test("k", "")
        self._test("m", "")
        self._test("n", "")
        self._test("p", "")
        self._test("q", "")
        self._test("s", "")
        self._test("t", "")
        self._test("u", "")
        self._test("v", "")
        self._test("x", "")
        self._test("y", "")
        self._test("z", "")
        self._test("!", "")
        self._test(".", "")
        self._test("?", "")
        self._test("abcfgijkmnpqstuvxyz!.?", "")

    def test_blank(self):
        self._test(" ", L_BLANK)
        self._test("  ", L_BLANK + L_BLANK)

    def test_letter_lower(self):
        self._test("d", L_D)
        self._test("dd", L_D + L_D)

        self._test("e", L_E)
        self._test("ee", L_E + L_E)

        self._test("h", L_H)
        self._test("hh", L_H + L_H)

        self._test("l", L_L)
        self._test("ll", L_L + L_L)

        self._test("o", L_O)
        self._test("oo", L_O + L_O)

        self._test("r", L_R)
        self._test("rr", L_R + L_R)

        self._test("w", L_W)
        self._test("ww", L_W + L_W)

    def test_hello_world(self):
        self._test(
            "Hello World!",
            L_H + L_E + L_L + L_L + L_O + L_BLANK + L_W + L_O + L_R + L_L + L_D,
        )


if __name__ == '__main__':
    unittest.main()