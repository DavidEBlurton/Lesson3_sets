# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink coke"
# 20 --> "drink beer"
# 30 --> "drink whisky"


# our funtion is going to take in a number from a user and is going to return a recommendation on what to drink

def solution(age):
    if age < '14':
        print('Drink toddy')
    elif age <= '18':
        print('Drink Coke')
    elif age <= '21':
        print('Drink Beer')
    else:
        return"Drink Whiskey"