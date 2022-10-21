my_file = open("data/people.txt", "r")
content = my_file.read()
peopleinfo = content.split(",")
my_file.close()

# In this project, you are going to program a more in-depth Person class.
# The person will have 6 properties:
# - name - str
# - age - int
# - siblings - int (number of siblings)
# - check - float (amount of money in checking account)
# - save - float (amount of money in savings account)
# - has_pet - bool (do they have a pet?)
# - has_job - bool (do they have a job?)
# Start by setting up an __init__() and __str__() method
# For each of the above properties, set appropriate getter and setter
# methods. Follow the following requirements:
# - age cannot be below 15 or above 100
# - siblings cannot be below 0 or above 15
# - check cannot be below $0 and cannot be above $1,000,000
# - save cannot be below $0 and cannot be above $10,000,000
#
# Give your class the following methods:
# - birthday() - increase the age of the person by 1, no return
# - family_size() - return "large" if siblings > 3, return "small" if
#       siblings <= 3, return "tiny" if siblings == 0
# - payday() - add a standard amount to check, return current check
# - make_money(num: float) -  add num to check, return current check
# - bills() - removes a standard amount from check, return current check
#       Ensure account does not go negative
# - spend(num: float) - remove num from check, return current check
#       Ensure account does not go negative
# - interest(years: int, rate: float) - calculate interest on savings:
#       *= (1 + rate) ** years
#       Check for an overflow error just in case
# - is_financially_safe() - returns True if they have a job and they have
#       at least $500,000 in save, or if they don't have a job and they
#       at least $800,000 in save. Otherwise, return False
# - can_retire() - returns True if age > 65, or if save > $200,000 and
#       age > 60, or if save > $400,000 and age > 55, or if
#       save > $800,000 and age > 50, otherwise False
# - trust_size() - returns save divided by number of siblings.
#       Watch out for division by zero errrors, in which case return 0.0
# - can_afford_pet() - returns True if they have more than $100,000 in check
#       and False otherwise


# This code will create a list called "people" that creates over 6,000
# Person objects and stores them in the list
people = list()
for person in peopleinfo:
    templist = person.split(";")
    name = templist[0]
    age = int(templist[1])
    sibl = int(templist[2])
    check = float(templist[3])
    save = float(templist[4])
    if templist[5] == "True":
        pet = True
    else:
        pet = False
    if templist[6] == "True":
        job = True
    else:
        job = False
    p = Person(name, age, sibl, check, save, pet, job)
    people.append(p)

# Go through the list of people and call birthday() on all of them


# Find and print the highest age of all people in the list


# Find and print the largest family size of all people


# Calculate the average family size of all people


# Call a payday() on everyone and make_money(1000)


# Call bills() on everyone and spend(500)


# Apply 10 years of 2% interest to everyone's save


# Find the highest check value of all people in the list, print
# out that person's name and balance. Do the same for save.


# Calculate the average check and save values and print them out


# Count how many people are considered both financially safe OR ready
# to retire. Print the result.


# Calculate the average trust size of all people and print the result


# Count the number of people who either have a pet OR can afford a pet.
# Print the percentage of people that fall into this category.
