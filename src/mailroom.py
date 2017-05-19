

def main():


def write_email_function(donor):
    if donor['amount'] > 10000:
        return "We thank you for your generous donation, {0}. With this donation of {1}, we can afford to buy new shoes for the orphans and a spoiler for my Ferrari.".format(donor['name'],donor['amount'])
    elif donor['amount'] == 1:
        return "Thank you for deliberately wasting our time, {0}, with your donation of 1 dollar. With this letter we have included a complimentary vial of orphan tears. I hope you\'re pleased with yourself. Monster.".format(donor['name'])
    else: 
        return "We thank you for your donation, {0}. The orphans will appreciate your donation of {1} dollars.".format(donor['name'],donor['amount'])

if __name__ == "__main__":
    main()