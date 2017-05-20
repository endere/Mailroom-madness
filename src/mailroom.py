"""This is mailroom madness code that takes input from the user, and outputs thank you messages for donors. It also holds data on all past donors, and can preview them when prompted."""
import os

donors = [{"name": "Mr. Rogers", "total": 5000000, "times_donated": 50, "average": 100000}, {"name": "Mark Zuckerberg", "total": 1, "times_donated": 1, "average": 1}, {"name": "Martha Stewart", "total": 5000, "times_donated": 5, "average": 1000}, {"name": "Larry", "total": 1000, "times_donated": 10, "average": 100}, {"name": "Curly", "total": 100, "times_donated": 2, "average": 50}, {"name": "Moe", "total": 49, "times_donated": 7, "average": 7},{"name": "George", "total": 3600, "times_donated": 20, "average": 180}]


def main():  # pragma: no cover
    """Create a menu prompt that displays three options for the user, and call functions accordingly."""
    response = raw_input('What would you like to do? You may type thank you, quit, or report: ')
    if response.lower() == 'thank you':
        get_name()
        main()
    elif response.lower() == 'report':
        report_function(donors)
        main()
    elif response.lower() == 'quit':
        os._exit(0)
    else:
        print('I did not understand that command.')
        main()


def get_name():  # pragma: no cover
    """Ask user for name, then pass it to the get_amount function."""
    name = raw_input('Please input donor name, or type list, or return: ')
    if name.lower() == 'list':
        print([person['name'] for person in donors])
        get_name()
    if name.lower() == 'return':
        main()
    else:
        get_amount(name)
    return


def get_amount(name):  # pragma: no cover
    """Ask for an amount donated, then pass bot hthe amout and name to the processing function."""
    amount = raw_input('Please input amount donated, or return: ')
    if amount.lower() == 'return':
        main()
    elif amount.isdigit() is False:
        print("not a number")
        get_amount(name)
    else:
        process_person(name, int(amount))
    return


def process_person(name, amount):
    """Check if the name is already used. If not, it creates a new set of information for this person. If it is, it updates the person\'s information.
    Either way, the code then passes a name and amount dictionary to the write email function, and prints it.
    """
    if name not in [person['name'] for person in donors]:
        this_donor = {"name": name, "total": amount, "times_donated": 1, "average": amount}
        donors.append(this_donor)
    else:
        this_donor = [person for person in donors if person['name'] == name][0]
        this_donor['total'] += amount
        this_donor['times_donated'] += 1
        this_donor['average'] = round(this_donor['total'] / this_donor['times_donated'])
    print(write_email_function({"name": name, "amount": amount}))
    return this_donor


def write_email_function(donor):
    """Write an email to the donor based on the amount they donated."""
    if donor['amount'] > 10000:
        return "We thank you for your generous donation, {0}. With this donation of {1}, we can afford to buy new shoes for the orphans and a spoiler for my Ferrari.".format(donor['name'],donor['amount'])
    elif donor['amount'] == 1:
        return "Thank you for deliberately wasting our time, {0}, with your donation of 1 dollar. With this letter we have included a complimentary vial of orphan tears. I hope you\'re pleased with yourself. Monster.".format(donor['name'])
    else:
        return "We thank you for your donation, {0}. The orphans will appreciate your donation of {1} dollars.".format(donor['name'],donor['amount'])


def report_function(donors):  # pragma: no cover
    """Print a list of donors, sorted by amount total donated.
    While this code does not receive inputs from the user, it still does not need to be tested, as it does not create or change any new information. Its job is simply to print existing information to the terminal.
    """
    new_list = sorted(donors, key=lambda x: x['total'], reverse = True)
    for person in new_list:
        print(person['name'], 'total: ', person['total'], 'times donated: ', person['times_donated'], 'average: ',person['average'] )


if __name__ == "__main__":
    main()
