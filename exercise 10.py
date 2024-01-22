# make a def function
def combine(bracket_one, bracket_two):
    # make an variable with empty bracket
    new_bracket = []

    # for loop for bracket_one
    for number in bracket_one:
        if number % 2 != 0:
            new_bracket.append(number)
        
    # for loop for bracket_two
    for number in bracket_two:
        if number % 2 == 0:
            new_bracket.append(number)
    # return to new_bracket
    return new_bracket

# copy the given bracket 
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


