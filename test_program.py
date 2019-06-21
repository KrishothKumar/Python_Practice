import pytest

from largest_num import largest
from radius import radius
from gcd import gcd
from lcd import lcd
from number_type import prime
from next_prime import nex_prime
from previous_prime import previous_prime
from word_reverse import string_reverse
from palindrome import palindrome
from list_sum import sums
from list_larg import largest_list
from list_odd_even import find
from list_fist_last import first_last_element


@pytest.mark.parametrize("input_1, input_2, input_3, exact_output",
                              [
                                 (5, 2, 3, 5),
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

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            (2, True),
                            (3, True),
                            (4, False)
                            ]
                        )
def test_prime(input_1,exact_output):
    assert prime(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            (2, 3),
                            (11, 13),
                            (14, 17)
                            ]
                        )
def test_nex_prime(input_1,exact_output):
    assert nex_prime(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            (0, None),
                            (3, 2),
                            (4, 3),
                            (10, 9)
                            ]
                        )
def test_previous_prime(input_1,exact_output):
    assert previous_prime(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            ("Pradeep loves swetha", "swetha loves Pradeep"),
                            ("but she don't know's it", "it know's don't she but"),
                            ("pradeep loves pallavi", "pallavi loves pradeep"),
                            ("but she love another fellow", "fellow another love she but")
                            ]
                        )
def test_string_reverse(input_1,exact_output):
    assert string_reverse(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            ("mom", True),
                            ("DAD", True),
                            ("bad", False),
                            ("NUN", True),
                            ]
                        )
def test_palindrome(input_1,exact_output):
    assert palindrome(input_1)==exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            ([0,1,2,3,4,5,6,7,8,9,10], (30,25)),
                            ([3,1,10,2,8,5,7,9,6,4,0], (30,25)),
                            ([25,23,22,40], (62,48))
                            ]
                        )
def test_sums(input_1,exact_output):
    assert sums(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            ([0,1,2,3,4,5,6,7,8,9,10], [1,3,5,7,9,0,2,4,6,8,10]),
                            ([3,1,10,2,8,5,7,9,6,4,0], [3,1,5,7,9,10,2,8,6,4,0]),
                            ([25,23,22,40], [25,23,22,40])
                            ]
                        )
def test_find(input_1,exact_output):
    assert find(input_1) == exact_output

@pytest.mark.parametrize("input_1,exact_output",
                            [
                            ([0,1,2,3,4,5,6,7,8,9,10], (0,10)),
                            ([3,1,10,2,8,5,7,9,6,4,0], (0,10)),
                            ([25,23,22,40], (22,40))
                            ]
                        )
def test_first_last_element(input_1,exact_output):
    assert first_last_element(input_1) == exact_output
