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
# - financial_safety() - returns True if they have a job and they have
#       at least $500,000 in save, or if they don't have a job and they
#       at least $800,000 in save. Otherwise, return False
# - retirement() - returns True if age > 65, or if save > $200,000 and
#       age > 60, or if save > $400,000 and age > 55, or if
#       save > $800,000 and age > 50, otherwise False
# - trust_size() - returns save divided by number of siblings
#       Watch out for division by zero errrors
# - afford_pet() - returns True if they have more than $100,000 in check
#       and False otherwise
class Person:
    def __init__(
        self,
        name: str,
        age: int,
        sibl: int,
        check: float,
        save: float,
        pet: bool,
        job: bool,
    ) -> None:
        self._name = name
        self._age = age
        self._siblings = sibl
        self._checking = check
        self._saving = save
        self._has_pet = pet
        self._has_job = job

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old, and has ${self._checking:.2f} in checking and ${self._saving:.2f} in saving."

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        self._name = n

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, a: int) -> None:
        if a >= 0 and a <= 100:
            self._age = a
        else:
            print("Unacceptable age")

    @property
    def siblings(self) -> int:
        return self._siblings

    @siblings.setter
    def siblings(self, s: int) -> None:
        if s >= 0 and s <= 15:
            self._siblings = s
        else:
            print("Unacceptable number of siblings")

    @property
    def checking(self) -> float:
        return self._checking

    @checking.setter
    def checking(self, c: float) -> None:
        if c >= 0.0 and c <= 1000000.0:
            self._checking = c
        else:
            print("Unacceptable checking value")

    @property
    def saving(self) -> float:
        return self._saving

    @saving.setter
    def saving(self, s: float) -> None:
        if s >= 0.0 and s <= 10000000.0:
            self._saving = s
        else:
            print("Unacceptale saving value")

    @property
    def has_pet(self) -> bool:
        return self._has_pet

    @has_pet.setter
    def has_pet(self, p: bool) -> None:
        self._has_pet = p

    @property
    def has_job(self) -> bool:
        return self._has_job

    @has_job.setter
    def has_job(self, j: bool) -> None:
        self._has_job = j

    def birthday(self) -> None:
        self._age += 1

    def family_size(self) -> str:
        if self._siblings > 3:
            return "Large"
        elif self._siblings > 0:
            return "Small"
        else:
            return "Tiny"

    def payday(self) -> float:
        self._checking += 2000.0
        return self._checking

    def make_money(self, f: float) -> float:
        self._checking += f
        return self._checking

    def bills(self) -> float:
        if self._checking > 1500.0:
            self._checking -= 1500.0
        else:
            print("Cannot afford bills")
        return self._checking

    def spend(self, f: float) -> float:
        if self._checking > f:
            self._checking -= f
        else:
            print("Cannot afford to spend")
        return self._checking

    def interest(self, years: int, rate: float) -> float:
        try:
            self._saving *= (1 + rate) ** years
        except OverflowError as ofe:
            print(ofe)
        else:
            return self._saving

    def financial_safety(self) -> bool:
        if self._has_job and save >= 500000.0:
            return True
        elif (not self._has_job) and save >= 800000.0:
            return True
        else:
            return False

    def retirement(self) -> bool:
        if self._age > 65:
            return True
        elif self._age > 60 and save > 200000.0:
            return True
        elif self._age > 55 and save > 400000.0:
            return True
        elif self._age > 50 and save > 800000.0:
            return True
        else:
            return False

    def trust_size(self) -> float:
        try:
            trust = self._saving / self.siblings
        except ZeroDivisionError as zde:
            pass
        else:
            return trust
        return 0.0

    def afford_pet(self) -> bool:
        if self._saving < 100000.0:
            return False
        else:
            return True


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

print(f"There are {len(people):,} people.")
# Go through the list of people and call birthday() on all of them
for person in people:
    person.birthday()

# Find and print the highest age of all people in the list
max = 0
for person in people:
    if person.age > max:
        max = person.age
print(f"The oldest person is {max} years old.")

# Find and print the largest family size of all people
max = 0
for person in people:
    if person.siblings > max:
        max = person.siblings
print(f"The largest family has {max} siblings.")

# Calculate the average family size of all people
sum = 0
for person in people:
    sum += person.siblings
average = sum / len(people)
print(f"The average number of siblings is {average:.2f}.")

# Call a payday() on everyone and make_money(1000)
# Call bills() on everyone and spend(500)
for person in people:
    person.payday()
    person.make_money(1000)
    person.bills()
    person.spend(500)

# Apply 10 years of 2% interest to everyone's save
for person in people:
    person.interest(10, 0.02)

# Find the highest check value of all people in the list, print
# out that person's name and balance. Do the same for save.
max_check = 0.0
max_check_name = ""
max_save = 0.0
max_save_name = ""
for person in people:
    if person.checking > max_check:
        max_check = person.checking
        max_check_name = person.name
    if person.saving > max_save:
        max_save = person.saving
        max_save_name = person.name
print(f"{max_check_name} has the largest checking with ${max_check:,.2f}")
print(f"{max_save_name} has the largest saving with ${max_save:,.2f}")

# Calculate the average check and save values and print them out
sum_check = 0.0
sum_save = 0.0
for person in people:
    sum_check += person.checking
    sum_save += person.saving
average_check = sum_check / len(people)
average_save = sum_save / len(people)
print(f"The average person has ${average_check:,.2f} in checking.")
print(f"The average person has ${average_save:,.2f} in saving.")

# Count how many people are considered both financially safe OR ready
# to retire. Print the result.
count = 0
for person in people:
    if person.financial_safety() or person.retirement():
        count += 1
print(f"{count} people are financially safe or able to retire")

# Calculate the average trust size of all people and print the result
sum = 0.0
for person in people:
    sum += person.trust_size()
average = sum / len(people)
print(f"The average trust size is ${average:,.2f}")

# Count the number of people who either have a pet OR can afford a pet.
# Print the percentage of people that fall into this category
count = 0
for person in people:
    if person.has_pet or person.afford_pet():
        count += 1
print(f"{count / len(people):.2%} of people have a pet or can afford one.")
