#!/usr/bin/env python3

import io
import sys
import pytest
from sequences import print_fibonacci


class TestPrintFibonacci:
    '''Test cases for print_fibonacci function'''

    @pytest.mark.parametrize("length, expected", [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ])
    def test_print_fibonacci(self, length, expected):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        result = print_fibonacci(length)
        sys.stdout = sys.__stdout__
        assert result == expected
