"""Test for the mailroom madness code."""

import pytest


PARAMS_TABLE_PROCESS = [
    ("Greg", 50, {"name": "Greg", "total": 50, "times_donated": 1, "average": 50}),
    ("George", 400, {"name": "George", "total": 4000, "times_donated": 21, "average": 190})


]
PARAMS_TABLE_EMAIL = [
    ({"name": "Mr. Rogers", "amount": 100000}, "We thank you for your generous donation, Mr. Rogers. With this donation of 100000, we can afford to buy new shoes for the orphans and a spoiler for my Ferrari."),
    ({"name": "Mark Zuckerberg", "amount": 1}, "Thank you for deliberately wasting our time, Mark Zuckerberg, with your donation of 1 dollar. With this letter we have included a complimentary vial of orphan tears. I hope you\'re pleased with yourself. Monster."),
    ({"name": "Martha Stewart", "amount": 1000}, "We thank you for your donation, Martha Stewart. The orphans will appreciate your donation of 1000 dollars.")

]


@pytest.mark.parametrize("name, amount, result", PARAMS_TABLE_PROCESS)
def test_process(name, amount, result):
    """This code tests if the processing data is able to correctly take a name and donation amount, and convert it into a dictionary object.
    One test creates a new donor, while the other uses a name that already exists in the system.
    The code, notably, does not need to return anything for the program to function. It uses a return strictly for this test.
    """
    from mailroom import process_person
    assert process_person(name, amount) == result


@pytest.mark.parametrize("donor, result", PARAMS_TABLE_EMAIL)
def test_email(donor, result):
    """This test inputs different names and amounts, and ensures that the email writing code gives the appropriate generated email, based on the amount given."""
    from mailroom import write_email_function
    assert write_email_function(donor) == result
