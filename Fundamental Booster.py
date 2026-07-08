print("welcome to the interactive personal data collector!")
name=(input("enter your name"))
age=int(input("enter your age"))
height=float(input("enter your height in meters"))
favourite_number=int(input("enter your favourite number"))
print("Thank you! Here is the information we collected :")
print(f"Name:{name},(Type:{type(name)},Memory Address:{id(name)})")
print(f"Age:{age},(type:{type(age)},Memory Address:{id(age)})")
print(f"Height:{height},(type:{type(height)},Memory Address:{id(height)})")
print(f"Favourite_Number:{favourite_number},(type:{type(favourite_number)},Memory Address:{id(favourite_number)})")
import datetime
year=datetime.datetime.now().year
Birth_date=year-age
print(f"Your birth year is approximately:{Your birth year is ")
print("Thank you for using the Personal Dta Collector. Goodbye!")
