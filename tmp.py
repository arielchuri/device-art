name = input("Enter user name: ")
age = input("Enter user age: ")
zodiac_signs = ["Mouse", "Ox", "Tiger", "Rabbit", "Dragon" , "Snake", "Horse", "Sheep", "Monkey", "Chicken", "Dog", "Pig"]
# Check if input is an integer
try:
    age_int = int(age) #checking if age is an integer
    print(f"{name} is {age} years old.") #typing out name is blank years old.
    # Extra credit: Estimated birth year
    yob = 2026 - age_int
    print(f"{name} was born around {yob}.")
    #Extra extra credit: Calculate Chinese zodiac sign (birth year zodiac)
    anchor_yob = 1900 #always start at year 1900, mouse.
    zodiac_index = (yob - 1900) % 12 #calculates index of user's zodiac.
    print (zodiac_signs[zodiac_index]) #types user's zodiac from array above.
except ValueError:
    print("Error: Please enter a whole number.")
