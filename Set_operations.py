# 2. Set Operations in Data Analysis
# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.

#Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
#Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}

print(customer_ids)
set_list = set(customer_ids)
print(set_list)

customer_ids = list(set_list)
print(customer_ids)