print("Welcome to Sunshine Cinema")
age=int(input("Enter your age:"))
if age<5:
    print("You get a free ticket! (Kids under 5 are free!)")
elif age>=5 and age<=12:
    print("Child Ticket Price:£4.99")
elif age>=13 and age<=18:
    print("Teen Ticket Price:£6.99")
elif age>=19 and age<=60:
    print("Adult Ticket Price:£8.99")
else:
    print("Senior Citizen Ticket Price:£5.00 (Discount applied)")

print("\nAvailable Show Timings:")
print("1. Morning Show - 10AM")
print("2. Afternoon Show - 2PM")
print("3. Evening Show - 6PM")
choice = int(input("Choose your show timing (1/2/3)"))

if choice==1:
    print("You selected the Morning Show")
elif choice==2:
    print("You selected the Afternoon Show")
elif choice==3:
    print("You selected the Evening Show")
else:
    print("Invalid choice! Please select a valid show time.")

print("\n Booking Complete! Enjoy your movie")


                                    