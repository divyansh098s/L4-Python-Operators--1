print("Enter Marks Obtained In 4 Subjects : ")
math = int(input("Maths : "))
english = int(input("English : "))
science = int(input("Science : "))
hindi = int(input("Hindi : "))
sum = math + english + science + hindi
print("Sum Of Math , English , Science And Hindi")
perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)