import pytest
from prime import prime_no
from odd_even_list import odd_even
from previous_prime import pre_prime
from palindrome  import palindrome1
from gcd2 import gcd
from list_first_last_element import list_element
from fibbonaci import fibo
from next_prime import next_prime
from previous_prime import pre_prime
from radius_circle import radius_circle
from reverse_ip_str import reverse
from sum_odd_even import odd_even
from denomination import denomination
from circle_circumference import circumference_circle

@pytest.mark.parametrize("input,output",
                            [
                                (2, True),
                                (6, False),
                                (3, True),
                                (14, False),
                                (17, True),
                                (20, False)

                            ]
                        )
def test_prime_no(input,output):
    assert prime_no(input) == output

@pytest.mark.parametrize("input,output",
                            [
                               ([1, 2, 3], [1, 3, 2]),
                               ([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7, 2, 4, 6]),
                               ([11, 12 ,13 ,14 ,15 ,16 ,17], [11, 13, 15, 17, 12, 14, 16]),
                               ([21, 22, 23, 24, 25, 26, 27],[21, 23, 25, 27, 22, 24, 26])
                            ]


                        )
def test_odd_even(input, output):
    assert odd_even(input) == output

@pytest.mark.parametrize("input, output",
                            [
                            (11, 7),
                            (15, 13),
                            (7, 5),
                            (21, 19)
                            ]
                        )

def test_pre_prime(input, output):
    assert pre_prime(input) == output

@pytest.mark.parametrize("input, output",
                            [
                            ("mom", True),
                            ("hema", False),
                            ("radar", True),
                            ("push", False),
                            ("level", True )
                            ]
                        )

def test_palindrome1(input, output):
    assert palindrome1(input) == output

@pytest.mark.parametrize("input1,input2,output",
                            [
                            (5, 4, 1),
                            (2, 6, 2),
                            (70, 45, 5),
                            (3, 21, 3),
                            (6, 12, 6)
                            ]
                        )

def test_gcd(input1, input2, output):
    assert gcd(input1, input2) == output

@pytest.mark.parametrize("input, output",
                            [
                            ([1, 2, 3, 4, 5], [1, 5]),
                            ([2, 1, 4 ,6, 9], [2, 9]),
                            ([0, 1, 4 ,6, 9], [0, 9]),
                            ([2, 1, 4 ,6, 100], [2, 100]),
                            ([2000, 1, 4 ,6, 9], [2000, 9]),
                            ]
                        )

def test_list_element(input, output):
    assert list_element(input) == output

@pytest.mark.parametrize("input, output",
                            [
                            (5, 5),
                            (7, 13),
                            (9, 34),
                            (8, 21),
                            (10, 55)
                            ]
                        )

def test_fibo(input,output):
    assert fibo(input) == output


@pytest.mark.parametrize("input,output",
                            [
                            (7, 11),
                            (3, 5),
                            (19, 23),
                            (11, 13),
                            (95, 97),
                            (105, 107)
                            ]
                        )

def test_next_prime(input,output):
    assert next_prime(input) == output


@pytest.mark.parametrize("input,output",
                            [
                            (23, 19),
                            (17, 13),
                            (11, 7),
                            (7, 5),
                            (5, 3),
                            (3, 2)
                            ]
                        )

def test_pre_prime(input, output):
    assert pre_prime(input) == output

@pytest.mark.parametrize("input,output",
                            [
                            (10, 1.78),
                            (7, 1.49),
                            (5, 1.26),
                            (100, 5.64)
                            ]
                        )

def test_radius_circle(input, output):
    assert radius_circle(input) == output

@pytest.mark.parametrize("input,output",
                            [
                            ("Hi Hemachandran", "Hemachandran Hi"),
                            ("How Are You", "You Are How"),
                            ("Good Morning", "Morning Good"),
                            ("good evening", "evening good"),
                            ("Windows 7 is a microsoft product", "product microsoft a is 7 Windows")
                            ]
                        )

def test_reverse(input, output):
    assert reverse(input) == output

@pytest.mark.parametrize("input,output",
                            [
                            ([1, 2 ,3 ,4], [1, 3, 2]),
                            ([3, 4 ,5 ,6 ,7 ,8], [3, 5, 7, 4, 6]),
                            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 7, 9, 2, 4, 6, 8])
                            ]
                        )

def test_odd_even(input, output):
    assert odd_even(input) == output

@pytest.mark.parametrize("input,expected_output",
                            [
                               (10900, [[2000, 5], [500, 1], [200, 2]]),
                               (2900, [[2000, 1], [500, 1], [200, 2]]),
                               (4235, [[2000, 2], [200, 1], [20, 1],[10, 1],[5, 1]])
                            ]
                        )
def test_denomination(input,expected_output):
    assert denomination(input) == expected_output

# @pytest.mark.parametrize("input1,input2,output",
#                             [
#                             ((2000, 3200), (2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,
#                             2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,
#                             2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,
#                             2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,
#                             2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,
#                             2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,
#                             2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,
#                             2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,
#                             2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,
#                             3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,
#                             3199))
#                             ]
#                         )
#
# def test_div_7(input1,input2,output):
#     assert div_7(input1,input2) == output

@pytest.mark.parametrize("input_1,expected_output",
                             [
                               (4, 25.12),
                               (7, 43.96),
                               (14, 87.92),
                               (16, 100.48),
                               (100, 682.00)
                             ]
                        )
def test_circumference_circle(input_1, expected_output):
    assert circumference_circle(input_1) == expected_output
