# 01 Exercise: Python Variables

# Q1. Calculate age using birth year and current year
birth_year = 2001
current_year = 2024
age = current_year - birth_year 
print("My age:", age)

# Q2. Store and print full name using first and last name
first_name = "Rohit"
last_name = "Karthick"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# --------------------------------------

# 02 Exercise: Numbers in Python

# Q1. Calculate the total area of a football field
field_length = 92 
field_width = 48.8 
total_area = field_length * field_width
print(f"The total area of the football field is {round(total_area, 1)} square meters.")

# Q2. Calculate change after purchasing 9 packets of chips
packets = 9
total_cost = round(packets * 1.49, 1)
change = 20 - total_cost
print(f"The shopkeeper will give me back {change} dollars.")

# Q3. Calculate total cost to replace tiles in a square bathroom
tile_length = 5.5
tile_area = round(pow(tile_length, 2), 2)
cost_per_sqft = 500
total_cost = cost_per_sqft * tile_area
print(f"The total cost to replace all tiles: {total_cost} Rs")

# Q4. Print the binary representation of the number 17
num = 17 
binary_representation = format(num, 'b')
print(f"Binary value of 17 is {binary_representation}")

# --------------------------------------


