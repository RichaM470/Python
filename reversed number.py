num= int(input("Enter a number:"))
rev = 0
num = abs(num)

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)