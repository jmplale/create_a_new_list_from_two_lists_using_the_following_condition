# make a def function
def combine(bracket_one, bracket_two):
    # make an variable with empty bracket
    new_bracket = []

    # for loop for num_one
    for number in bracket_one:
        if number % 2 != 0:
            new_bracket.append(number)