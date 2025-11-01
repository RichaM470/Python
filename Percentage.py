print("Enter Marks Obtained in 4 subjects: ")
maths=int(input("maths:"))
english=int(input("english:"))
science=int(input("science:"))
economics=int(input("economics:"))
sum=maths+english+science+economics
print("sum of maths,english,science and economics")
perc=(sum/400)*100
print(end="Percentage Mark = ")
print(perc)