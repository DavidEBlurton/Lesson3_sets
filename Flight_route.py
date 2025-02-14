# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. # You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
 #Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

intersect = our_routes.intersection(competitor_routes)
print(intersect)

print(our_routes.difference(competitor_routes))

sym_diff_set = our_routes.symmetric_difference(competitor_routes)
print(sym_diff_set)