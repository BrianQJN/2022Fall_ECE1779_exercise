# Question 1
# A library charges overdue fees for a borrowed book using the following fee schedule:
#                       less than 4 days late: 1 dollar per day
#                       4 to 6 days late: 2 dollars per day (for all days, including the first 3 days)
#                       more than 6 days late: 3 dollars per day (for all days, including the first 6 days)
#
# Borrowers of books are in one of these age groups: CHILD, ADULT, or SENIOR. A CHILD gets charged only half of the fees and a SENIOR gets charged only one quarter of the fees.
# An ADULT pays the full fee.
#
# Complete the following function according to the description above and the docstring below.


CHILD = 'child'
ADULT = 'adult'
SENIOR = 'senior'


def overdue_fees(days_late: int, age_group: str) -> float:
    """Return the fees for a book that is days_late days late for a borrower
    in the age group age_group.

    >>> overdue_fees(2, SENIOR) # 2 days late, SENIOR borrower
    0.5
    >>> overdue_fees(5, ADULT) # 5 days late, ADULT borrower
    10
    """

    if 0 <= days_late < 4:
        fees = 1 * days_late
    elif 4 <= days_late <= 6:
        fees = 2 * days_late
    elif days_late > 6:
        fees = 3 * days_late
    else:
        print("The days of late should greater than 0")
        fees = 0

    if fees == 0:
        final_fees = 0
    else:
        if age_group == CHILD:
            final_fees = fees / 2
        elif age_group == ADULT:
            final_fees = fees
        elif age_group == SENIOR:
            final_fees = fees / 4
        else:
            print("The age group is not in child, adult or senior, re-input")
            final_fees = 0

    return final_fees


if __name__ == "__main__":
    print(overdue_fees(2, SENIOR))
    print(overdue_fees(5, ADULT))
