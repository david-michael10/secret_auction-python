import art
logo = art.logo

data_dictionary = {}
should_continue = True

while should_continue:
    print(logo)
    name = input("What's your name? ").lower()
    print()
    bid = float(input("What's your bid? $ "))
    print()

    data_dictionary[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print()

    if answer == "no":
        should_continue = False

        person = ""
        highest_bid = 0
        for i in data_dictionary:
            bidders = data_dictionary[i]
            if bidders > highest_bid:
                highest_bid = bidders
                person = i
        print(f"The winner is {person.upper()} with a price of ${highest_bid}")
    else:
        print("\n" * 100)