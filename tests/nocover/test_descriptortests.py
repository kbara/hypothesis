# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

from random import Random
from decimal import Decimal
from fractions import Fraction
from collections import OrderedDict, namedtuple

from hypothesis import strategy
from tests.common.basic import Bitfields, BoringBitfields, \
    simplify_bitfield
from hypothesis.specifiers import just, one_of, strings, streaming, \
    dictionary, sampled_from, integers_from, floats_in_range, \
    integers_in_range
from tests.common.specifiers import Descriptor
from hypothesis.strategytests import TemplatesFor, strategy_test_suite
from hypothesis.internal.compat import text_type, binary_type
from hypothesis.searchstrategy.basic import basic_strategy
from hypothesis.searchstrategy.narytree import NAryTree

TestIntegerRange = strategy_test_suite(integers_in_range(0, 5))
TestGiantIntegerRange = strategy_test_suite(
    integers_in_range(-(2 ** 129), 2 ** 129)
)
TestFloatRange = strategy_test_suite(floats_in_range(0.5, 10))
TestSampled10 = strategy_test_suite(sampled_from(elements=list(range(10))))
TestSampled1 = strategy_test_suite(sampled_from(elements=(1,)))
TestSampled2 = strategy_test_suite(sampled_from(elements=(1, 2)))

TestIntegersFrom = strategy_test_suite(integers_from(13))

TestOneOf = strategy_test_suite(one_of((int, int, bool)))
TestOneOfSameType = strategy_test_suite(
    one_of((integers_in_range(1, 10), integers_in_range(8, 15)))
)
TestRandom = strategy_test_suite(Random)
TestInts = strategy_test_suite(int)
TestBoolLists = strategy_test_suite([bool])
TestDictionaries = strategy_test_suite(dictionary((int, int), bool))
TestOrderedDictionaries = strategy_test_suite(
    dictionary(int, int, OrderedDict)
)
TestString = strategy_test_suite(text_type)
BinaryString = strategy_test_suite(binary_type)
TestIntBool = strategy_test_suite((int, bool))
TestFloats = strategy_test_suite(float)
TestComplex = strategy_test_suite(complex)
TestJust = strategy_test_suite(just('hi'))
TestTemplates = strategy_test_suite(TemplatesFor({int}))

TestEmptyString = strategy_test_suite(strings(alphabet=''))
TestSingleString = strategy_test_suite(strings(alphabet='a'))
TestManyString = strategy_test_suite(strings(alphabet='abcdef☃'))

Stuff = namedtuple('Stuff', ('a', 'b'))
TestNamedTuple = strategy_test_suite(Stuff(int, int))

TestTrees = strategy_test_suite(NAryTree(int, int, int))

TestMixedSets = strategy_test_suite({int, bool, float})
TestFrozenSets = strategy_test_suite(frozenset({bool}))

TestNestedSets = strategy_test_suite(frozenset({frozenset({complex})}))

TestMisc1 = strategy_test_suite({(2, -374): frozenset({None})})
TestMisc2 = strategy_test_suite({b'': frozenset({int})})
TestMisc3 = strategy_test_suite(({type(None), str},),)

TestEmptyTuple = strategy_test_suite(())
TestEmptyList = strategy_test_suite([])
TestEmptySet = strategy_test_suite(set())
TestEmptyFrozenSet = strategy_test_suite(frozenset())
TestEmptyDict = strategy_test_suite({})

TestDecimal = strategy_test_suite(Decimal)
TestFraction = strategy_test_suite(Fraction)

TestDescriptor = strategy_test_suite(Descriptor)

TestNonEmptyLists = strategy_test_suite(
    strategy([int]).filter(lambda x: x)
)


TestConstantLists = strategy_test_suite(
    strategy(int).flatmap(lambda i: [just(i)])
)

TestOrderedPairs = strategy_test_suite(
    strategy(integers_in_range(1, 200)).flatmap(
        lambda e: (integers_in_range(0, e - 1), just(e))
    )
)

TestMappedSampling = strategy_test_suite(
    strategy([int]).filter(bool).flatmap(sampled_from)
)

TestManyFlatmaps = strategy_test_suite(
    strategy(int)
    .flatmap(integers_from)
    .flatmap(integers_from)
    .flatmap(integers_from)
    .flatmap(integers_from)
)

TestIntStreams = strategy_test_suite(streaming(int))
TestStreamLists = strategy_test_suite(streaming(int))
TestIntStreamStreams = strategy_test_suite(streaming(streaming(int)))


TestBoringBitfieldsClass = strategy_test_suite(BoringBitfields)
TestBitfieldsClass = strategy_test_suite(Bitfields)
TestBitfieldsInstance = strategy_test_suite(Bitfields())


TestBitfields = strategy_test_suite([
    basic_strategy(
        generate=lambda r, p: r.getrandbits(128),
        simplify=simplify_bitfield,
        copy=lambda x: x,
    )
])

TestBitfieldsSet = strategy_test_suite({
    basic_strategy(
        generate=lambda r, p: r.getrandbits(128),
        simplify=simplify_bitfield,
        copy=lambda x: x,
    )
})


TestBitfield = strategy_test_suite(
    basic_strategy(
        generate=lambda r, p: r.getrandbits(128),
        simplify=simplify_bitfield,
        copy=lambda x: x,
    )
)

TestBitfieldJustGenerate = strategy_test_suite(
    basic_strategy(
        generate=lambda r, p: r.getrandbits(128),
    )
)


TestBitfieldWithParameter = strategy_test_suite(
    basic_strategy(
        parameter=lambda r: r.getrandbits(128),
        generate=lambda r, p: r.getrandbits(128) & p,
    )
)


def test_repr_has_specifier_in_it():
    suite = TestComplex(
        'test_can_round_trip_through_the_database')
    assert repr(suite) == 'strategy_test_suite(complex)'
