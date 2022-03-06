#Create functions that calculate average BMR needs for an Individual
def averagebmr():
    subject = {}
    curious = True
    name = input("What is your name? > ")
    ##regular expressions import re
    ## re.match()   this to make sure string input not int
    subject["Name"] = subject.get("Name", name)
    while curious == True:
        gender = input('Are you male or female? > ')
        gender = gender.lower()
        if gender == "male" and "female":
            subject["Gender"] = subject.get("Gender", gender)
            curious = False

        else:
            print("Please enter male or female ")

    while curious == False:
        weight = input('How much do you weight in Lbs? > ')
        try:
            curious = True
            weight = int(weight)
            weight = weight / 2.2
            subject["Weight"] = subject.get("Weight", weight)

        except ValueError:
            print("Please enter your weight in Lbs with digits")

    while curious == True:
        height = input("How tall are you in inches? > ")
        try:
            height = int(height)
            height = height * 2.54
            subject["Height"] = subject.get("Height", height)
            curious = False
        except:
            print("Please enter your height in inches with digits")

    while curious == False:
        age = input("How many years old are you? > ")
        try:
            age = int(age)
            subject["Age"] = subject.get("Age", age)
            curious = True
        except:
            print("Please enter your age in with digits")

    if subject["Gender"] == "female":
        bmr = (10* subject["Weight"]) + (6.25 * subject["Height"]) - (5 * subject["Age"]) - 161
        subject["BMR"] = subject.get("BMR", bmr)

    elif subject["Gender"] == "male":
        bmr = (10* subject["Weight"]) + (6.25 * subject["Height"]) - (5 * subject["Age"]) + 5
        bmr = int(bmr)
        subject["BMR"] = subject.get("BMR", bmr)
    return subject

#Helper function for caloric needs
def deficit(goal):
    weeks = int(input("How many weeks would you like to accomplish this in? > "))
    days = weeks * 7
    return (goal * 3500)/ days


#Create functions that calculates estimate caloric needs based off BMR and goal
def goalneeds(bmr):
    question = True
    while question == True:
        desire = input("Would you like to lose weight, gain muscle, or improve body composition? > ")
        desire = desire.lower()

        if desire == "lose weight":
            question = False
            goal = input("How many pounds would you like to lose? > ")
            goal = float(goal)
            caloricgoal = deficit(goal)
            dailyintake = bmr["BMR"] - caloricgoal
            goal = int(goal)
            caloricgoal = int(caloricgoal)
            dailyintake = int(dailyintake)
            return print(f"To reach your weight lost of {goal}Lbs in time you will need a deficit of {caloricgoal} Calories a day. You will consume {dailyintake} Calories a day\n")

        elif desire == "gain muscle":
            question = False
            goal = input("How many pounds would you like to add? > ")
            goal = float(goal)
            caloricgoal = deficit(goal)
            dailyintake = bmr["BMR"] + caloricgoal
            goal = int(goal)
            caloricgoal = int(caloricgoal)
            dailyintake = int(dailyintake)
            return print(f"To reach your muscle gain of {goal} in time you will need a surplus of {caloricgoal} Calories a day. You will consume {dailyintake} Calories a day\n")

        elif desire == 'improve body composition':
            question = False
            dailyintake = bmr["BMR']"]
            return print(f"To maintain your body weight you will consume {dailyintake} Calories a day\n")

        else:
            print("Please enter lose weight, gain muscle, or improve body composition")
bmr = averagebmr()
print("\nGreat! We are almost there. Just a few more questions.\n")
goalneeds(bmr)


###next step is to take inputs percentages for marcos to get grams/marco/day





#Set each individual as an Object
#class individual():
#    def __init__(self, name, bmr, goal):
#        self.name = name
#        self.bmr = bmr
#        self.goal = goal
