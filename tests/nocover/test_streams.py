# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from itertools import islice

from hypothesis import given, assume
from hypothesis.specifiers import streaming
from hypothesis.internal.compat import integer_types


@given(streaming(int))
def test_can_adaptively_assume_about_streams(xs):
    for i in islice(xs, 200):
        assume(i >= 0)


@given(streaming(int))
def test_streams_are_arbitrarily_long(ss):
    for i in islice(ss, 100):
        assert isinstance(i, integer_types)
