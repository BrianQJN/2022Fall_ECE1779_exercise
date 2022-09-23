# Question 3
# You have been asked to write a function that supplies the "reverse lookup" name for the person associated with a phone number.
# This means that given a phone number, you get the name of the person
# who is registered with that phone number. Write this function using parallel lists.


from typing import List

def reverse_lookup_lists(phone_num: str, phone_numbers: List[str],
                         names: List[str]) -> str:
    """This function receives a phone number phone_num, and two lists: a list
    of phone numbers phone_numbers and a list of names names.  These lists are
    parallel lists, so the name in position 0 of the names list is
    associated with the phone number in position 0 of the phone_numbers
    list, and so on.

    Return the name associated with phone_num according to phone_numbers
    and names, or an empty string if there is no match.

    Precondition: len(phone_numbers) == len(names)

    >>> reverse_lookup_lists('416-555-6543', ['416-555-3498', \
        '647-555-9812', '416-555-6543', '905-555-6681'], ['John A. Macdonald', \
        'Louis Riel', 'Canoe Head', 'Tim Horton'])
    'Canoe Head'
    """