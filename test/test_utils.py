'''A set of tests for functions in util.py'''

import os
import sys

import pytest

test_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(test_path + '/../src')
import util


@pytest.mark.parametrize('number,correct_output',
                         [(1, 2),
                          (-1, 0),
                          ])
def test_add_one(number, correct_output):
    assert correct_output == util.add_one(number)
