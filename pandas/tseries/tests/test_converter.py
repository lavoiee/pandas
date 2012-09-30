from datetime import datetime, time, timedelta
import sys
import os
import unittest

import nose

import numpy as np

import pandas.tseries.converter as converter

def test_timtetonum_accepts_unicode():
    assert(converter.time2num("00:01")==converter.time2num(u"00:01"))

class TestDateTimeConverter(unittest.TestCase):

    def setUp(self):
        self.dtc = converter.DatetimeConverter()

    def test_convert_accepts_unicode(self):
        r1 = self.dtc.convert("12:22",None,None)
        r2 = self.dtc.convert(u"12:22",None,None)
        assert(r1==r2), "DatetimeConverter.convert should accept unicode"

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],
                   exit=False)
