# Question 2
import re


def check_password(passwd: str) -> bool:
    """A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    example:
    >>> check_password('I<3ece1779')
    True
    """
    length = len(passwd)
    lower_char = re.findall(r'[a-z]', passwd)
    upper_char = re.findall(r'[A-Z]', passwd)
    digit = re.findall(r'[0-9]', passwd)
    if length >= 6 and len(lower_char) >= 1 and len(upper_char) >= 1 and len(digit) >= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_password("I<3ece1779"))
