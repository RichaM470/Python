print("--- Alphabet Checker Program")

ch=input("Enter a character:")

print("\nYou enetered:",ch)

if len(ch) !=1:
    print("Error: Please enter exactly one character.")
else:
    ascii_value=ord(ch)
    print("ASCII value of the character:", ascii_value)

if (ascii_value >=65 and ascii_value <=90):
    print(f"{ch} is an alphabet (Uppercase Letter).")
elif(ascii_value>=97 and ascii_value<=122):
    print(f"{ch} is and alphabet (Lowercase Letter).")
else:
    print(f"{ch} is NOT an alphabet")

print("\n=== Program Finished ===")