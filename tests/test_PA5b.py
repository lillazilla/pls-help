import sys
import unittest
from io import StringIO

from PA5b import main

S_NUMS = "Enter a stream of non-negative numbers (negative when finished): "
S_AGAIN = "Do you want to compute another average (y/n)? "


class TestPA5b(unittest.TestCase):

    def _test(self, values, results):
        input_text = "\n".join(values) + "\n"
        expected_output = "".join(
            S_NUMS + f"The average is: {avg}\n" + S_AGAIN
            for avg in results
        )

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

    def test_stop(self):
        self._test(["-1", "n"], ["0.00"])
        self._test(["-1", "N"], ["0.00"])
        self._test(["-1", "y", "-2", "n"], ["0.00", "0.00"])
        self._test(["-1", "y", "-2", "N"], ["0.00", "0.00"])
        self._test(["-1", "Y", "-2", "n"], ["0.00", "0.00"])
        self._test(["-1", "Y", "-2", "N"], ["0.00", "0.00"])

    def test_int_one(self):
        self._test(["1", "2", "3", "-1", "n"], ["2.00"])
        self._test(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "-1", "n"], ["5.50"])
        self._test(["1", "1", "3", "-1", "n"], ["1.67"])

    def test_dec_one(self):
        self._test(["1.1", "1.9", "3", "-1", "n"], ["2.00"])
        self._test(["1.1", "2.2", "3.3", "-1", "n"], ["2.20"])


if __name__ == '__main__':
    unittest.main()