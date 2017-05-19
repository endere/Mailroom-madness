"""Test for the mailroom madness code."""


import pytest
PARAMS_TABLE_REPORT = [
        ([{"name": "Mr. Rogers", "total": 5000000, "times_donated": 50, "average": 100000}, {"name": "Mark Zuckerberg", "total": 1, "times_donated": 1, "average": 1}, {"name": "Martha Stewart", "total": 5000, "times_donated": 5, "average": 1000}]),([{"name": "Larry", "total": 1000, "times_donated": 10, "average": 100}, {"name": "Curly", "total": 100, "times_donated": 2, "average": 50}, {"name": "Moe", "total": 49, "times_donated": 7, "average": 7}])

]
PARAMS_TABLE_EMAIL = [
        ({"name": "Mr. Rogers", "amount": 100000}, "We thank you for your generous donation, Mr. Rogers. With this donation of 100000, we can afford to buy new shoes for the orphans and a spoiler for my Ferrari."),
        ({"name": "Mark Zuckerberg", "amount": 1}, "Thank you for deliberately wasting our time, Mark Zuckerberg, with your donation of 1 dollar. With this letter we have included a complimentary vial of orphan tears. I hope you\'re pleased with yourself. Monster."),
        ({"name": "Martha Stewart", "amount": 1000}, "We thank you for your donation, Martha Stewart. The orphans will appreciate your donation of 1000 dollars.")

]

# @pytest.mark.parametrize("n, result", PARAMS_TABLE_REPORT)
# def test_report(n, result):
#     from mailroom import report_function
#     assert report_function(n) == result

@pytest.mark.parametrize("donor, result", PARAMS_TABLE_EMAIL)
def test_email(donor, result):
    from mailroom import write_email_function
    assert write_email_function(donor) == result
