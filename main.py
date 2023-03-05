#print("hello  "+" you")
#print("hello" + " "+"world")
#  fix code below

# print("Day 1 - String Manipulation")
# print("Sting Concatination is done with the"+"sign.")
# print('e.g. print("Hello""+"world")')
# print(("New lines can be created with a backlash and n."))


# Exercise ----> BMI Calculator!!!!!!


# height=input("enter your height in m:")
# weight=input("enter your weight in kg: ")

# height_in_float= float(height)
# weight_in_float=float(weight)
# bmi=weight_in_float/height_in_float**2

# bmi_in_integer=int(bmi)
# print(bmi_in_integer)



#YOUR WEEKS IN LIFE

age=input("what is your current age? \n")

type(age)

age_in_int=int(age)
years_remaining=90-age_in_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12

message=f"you have{days_remaining}days,{weeks_remaining}weeks,{months_remaining}months"
print(message)