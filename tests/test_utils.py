import doctest
import unittest

from dffr import utils


def test_doctest_suit():
    test_suit = unittest.TestSuite()
    test_suit.addTest(doctest.DocTestSuite(utils))
    result = unittest.TextTestRunner(verbosity=2).run(test_suit)

    assert not result.failures
