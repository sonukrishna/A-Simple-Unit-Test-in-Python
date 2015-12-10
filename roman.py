import re

class RomanError(Exception) :
    pass

class OutOfRangeError(RomanError) :
    pass

class NotIntegerError(RomanError) :
    pass

class InvalidRomanNumeralError(RomanError) :
    pass

# Define digit mapping

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(n) :
    """convert integer to roman numeral """
    if not (0 < n < 4000) :
        raise OutOfRangeError, "number out of range"
    if int(n) <> n:
        raise NotIntegerError, "non-integers not allowed"
    result = ""
    for numeral, intgr in roman_numeral_map :
        while n>= intgr :
            result += numeral
            n -= intgr

    return result

roman_numeral_pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
def from_roman(rmn) :
    """convert roman numerals to numbers"""
    pass
    if not re.search(roman_numeral_pattern, rmn):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % rmn
    result = 0
    index = 0
    for numeral, intgr in roman_numeral_map :
        while rmn[index : index + len(numeral)] == numeral :
            result += intgr
            index += len(numeral)
    return result


