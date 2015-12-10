"""unit test for roman.py """

import roman
import unittest


class KnownValues(unittest.TestCase) :
    known_values = ( (1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX') )

    def test_toRoman(self) :
        for intgr, rmn in self.known_values :
            result = roman.to_roman(intgr)
            self.assertEqual(rmn, result)

    def test_fromRoman(self):
        for intgr, rmn in self.known_values :
            result = roman.from_roman(rmn)
            self.assertEqual(intgr, result)

class ToRomanBad(unittest.TestCase) :
    
    def test_large(self):
        """ to_roman fails with large input than 3999"""
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)

    def test_zero(self):
        """ to_roman fails with input zero """
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

    def test_negative(self):
        """to_roman fails with negative input """
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)

    def test_non_integer(self):
        """to_roman fails with non-integer """
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)

class FromRomanBad(unittest.TestCase) :


    def test_toomany_numerals(self) :
        """ from_roman fails with too many repeated numerals """
        for numerals in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError,\
                              roman.from_roman, numerals)
    def test_repeatd_pairs(self) :
        """from_roman fails with  repeated pairs numerals """
        for numerals in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV') :
            self.assertRaises(roman.InvalidRomanNumeralError,\
                              roman.from_roman, numerals)

    def test_malformed_antecedent(self):
        """from_roman should fail with malformed antecedents"""
        for numerals in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError,\
                            roman.from_roman, numerals)

class SanityCheck(unittest.TestCase) :

    def test_sanity(self) :
        """from_roman(to_roman(n))==n for all n"""
        for intgr in range(1, 4000) :
            numeral = roman.to_roman(intgr)
            result = roman.from_roman(numeral)
            self.assertEqual(intgr, result)

class CaseCheck(unittest.TestCase) :

    def test_to_roman_case(self) :
        """to_roman should always return uppercase """
        for intgr in range(1, 4000) :
            numeral = roman.to_roman(intgr)
            self.assertEqual(numeral, numeral.upper())

    def test_from_roman_case(self) :
        """from_roman should only accept uppercase input"""
        for intgr in range(1, 4000) :
            numeral = roman.to_roman(intgr)
            roman.from_roman(numeral.upper())
            self.assertRaises(roman.InvalidRomanNumeralError,
                              roman.from_roman, numeral.lower())

if __name__ == '__main__' :
    unittest.main()
