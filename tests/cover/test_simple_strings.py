# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from hypothesis import find
from hypothesis.internal.compat import text_type


def test_can_minimize_up_to_zero():
    s = find(text_type, lambda x: len([t for t in x if t <= '0']) >= 10)
    assert s == '0' * 10


def test_minimizes_towards_ascii_zero():
    s = find(text_type, lambda x: any(t < '0' for t in x))
    assert len(s) == 1
    assert ord(s) == ord('0') - 1


def test_can_handle_large_codepoints():
    s = find(text_type, lambda x: x >= '☃')
    assert s == '☃'


def test_will_find_ascii_examples_given_the_chance():
    s = find((text_type, text_type), lambda x: x[0] and (x[0] < x[1]))
    assert s == ('0', '1')
