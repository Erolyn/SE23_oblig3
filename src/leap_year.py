def isLeapYear(year):
    if not isinstance(year, int):
        raise TypeError("The year must be an integer.")
    # The Gregorian calendar does not operate in negative years
    # or year 0, but rather 1 BC and 1 AD
    if year <= 0:
        return False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
