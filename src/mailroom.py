import os

donors = [{"name": "Mr. Rogers", "total": 5000000, "times_donated": 50, "average": 100000}, {"name": "Mark Zuckerberg", "total": 1, "times_donated": 1, "average": 1}, {"name": "Martha Stewart", "total": 5000, "times_donated": 5, "average": 1000}, {"name": "Larry", "total": 1000, "times_donated": 10, "average": 100}, {"name": "Curly", "total": 100, "times_donated": 2, "average": 50}, {"name": "Moe", "total": 49, "times_donated": 7, "average": 7}]


def main():
    response = raw_input('What would you like to do? You may type thank you, quit, or report: ')
    if response.lower() == 'thank you':
        thank_you_function()
        print(write_email_function('test'))
    elif response.lower() == 'report':
        report_function(donors)
        main()
    elif response.lower() == 'quit':
        os._exit(0)
    else:
        print('I did not understand that command.')
        main()


def thank_you_function():
    logic = "stuff"
#def report_function():

def write_email_function(donor):
    if donor['amount'] > 10000:
        return "We thank you for your generous donation, {0}. With this donation of {1}, we can afford to buy new shoes for the orphans and a spoiler for my Ferrari.".format(donor['name'],donor['amount'])
    elif donor['amount'] == 1:
        return "Thank you for deliberately wasting our time, {0}, with your donation of 1 dollar. With this letter we have included a complimentary vial of orphan tears. I hope you\'re pleased with yourself. Monster.".format(donor['name'])
    else: 
        return "We thank you for your donation, {0}. The orphans will appreciate your donation of {1} dollars.".format(donor['name'],donor['amount'])



if __name__ == "__main__":
    main()