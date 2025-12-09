#notes on while loops
#while loop = execute some code WHILE some condition remains true
# Given:
num = int(input("Enter a #between 1-10: "))

while num <1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a #between 1-10: "))

print(f"Your number is {num}")

# print("-" * 30)

# food = input("Enter a food you like(q to quit):")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like(q to quit):")

# print("bye")

# food = input("what is your favorite food?")

# while not food == "quit":
#     food_list = []
#     print("I like " + food "too!")

# print("-" * 30)

# age = int(input("Enter your age:"))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age"))

# print(f"You are {age} years old")

# print("-" * 30)

# name = input("Enter your name:")
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name:")
# else:
#     print(f"Hello {name}")

# print("-" * 30)

colors = ["red", "blue", "green", "yellow", "purple"]
index = 0
while index < len(colors):
    if colors [index] == "yellow":
        break    
    print(colors[index])
    index += 1 # incrememnt the index to avoid infinite loop
# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
 