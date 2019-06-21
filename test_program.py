import pytest

from largest_num import largest
from radius import radius
from gcd import gcd
from lcd import lcd

@pytest.mark.parametrize("input_1,input_2,input_3,exact_output",
                              [
                                 ( 5, 2, 3, 5),
                                 (1, 10, 7, 10),
                                 (9, 5, 3, 9)
                              ]
                        )
def test_largest(input_1,input_2,input_3,exact_output):
    assert largest(input_1,input_2,input_3) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                                [
                                (25, 2.82),
                                (28, 2.99),
                                (30, 3.09),
                                (35, 3.34),
                                (50, 3.99)
                                ]

                        )
def test_radius(input_1,exact_output):
    assert radius(input_1) == exact_output

@pytest.mark.parametrize("input_1,input_2,exact_output",
                            [
                            (8, 16, 8),
                            (24, 16, 8),
                            (33, 33, 33)
                            ]
                        )
def test_gcd(input_1,input_2,exact_output):
    assert gcd(input_1, input_2) == exact_output

@pytest.mark.parametrize("input_1,input_2,exact_output",
                            [
                            (65, 10, 130),
                            (50, 11, 550),
                            (7, 7, 7)
                            ]
                        )
def test_lcd(input_1,input_2,exact_output):
    assert lcd(input_1, input_2) == exact_output
