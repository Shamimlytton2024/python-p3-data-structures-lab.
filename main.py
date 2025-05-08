students =["moringa","uon","jkuat","kenya"]
print(students)

students.append("jerry")
print(list (students))
students.remove("uon")
print(list(students))
students.insert(0,"kampala")
print(list(students))
students.sort()
print(list(students))
students.reverse()
print(list(students))



"""
write a program that calculate the age from the birth year
date of birth year =[2000,1994,2005,1985,2010]
"""
#list of birth years
birth_years=[2000,1994,2005,1985,2010]

#get the current year
current_year = 2025

#calculate the age
age=[current_year -year for year in birth_years]

#print the result
for i, year in enumerate(birth_years):
    print(f"year of Birth: {year} age: {age[i]}")


