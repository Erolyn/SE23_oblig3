from src.leap_year import isLeapYear


def test_invalidInput():
    # Invalid input should raise an exception
    try:
        isLeapYear("2022")  # Passing a string as input
        assert False  # This line should not return True
    except TypeError:
        assert True  # Expecting a TypeError to be raised


def test_yearIsDivisibleByFour():
    if 2000 % 4 == 0:
        return True


def test_yearIsDivisibleByFourAndNotByHundred():
    if test_yearIsDivisibleByFour == True:
        if 2000 % 100 != 0:
            return True


def test_yearIsDivisibleByFourhundred():
    if 2000 % 400 == 0:
        return True


def test_isLeapYear2000():
    # 2000 is a leap year, and should therefore return True
    assert isLeapYear(2000) == True


def test_isNotLeapYear1700():
    # 1700 is not a leap year, and should therefore return False
    assert isLeapYear(1700) == False


def test_isNotLeapYear1800():
    # 1800 is not a leap year, and should therefore return False
    assert isLeapYear(1800) == False


def test_isNotLeapYear1900():
    # 1900 is not a leap year, and should therefore return False
    assert isLeapYear(1900) == False


def test_isNotLeapYear2100():
    # 2100 is not a leap year, and should therefore return False
    assert isLeapYear(2100) == False


def test_negativeYear():
    # Negative years should return False
    assert isLeapYear(-2000) == False
    assert isLeapYear(-1800) == False


def test_yearZero():
    assert isLeapYear(0) == False
