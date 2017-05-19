"""Test for the mailroom madness code."""


import pytest

donors = [{"name": "George", "total": 3600, "times_donated": 20, "average": 180}]
"""This is here to test the process function for when there is already a name in the donors list."""


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
    from mailroom import process_person
    assert process_person(name, amount) == result

@pytest.mark.parametrize("donor, result", PARAMS_TABLE_EMAIL)
def test_email(donor, result):
    from mailroom import write_email_function
    assert write_email_function(donor) == result
