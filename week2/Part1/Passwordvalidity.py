# Question 2

def check_password(passwd: str) -> bool:
    """A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    example:
    >>> check_password('I<3ece1779')
    True
    """