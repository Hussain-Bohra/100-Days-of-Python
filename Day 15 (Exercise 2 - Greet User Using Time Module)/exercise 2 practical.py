# Exercise 2 Program :-

name = input("Please Enter Your Name: ").title()
mytime = int(input("Enter Time(Only Hours) in 24 Hour Format: "))
print()

if (mytime >= 00 and mytime < 12):
    print("Good Morning,",name)

elif(mytime >= 12 and mytime < 17):
    print("Good Afternoon,",name)

elif(mytime >= 17 and mytime < 22):
    print("Good Evening,",name)

elif(mytime >= 22 and mytime <= 24):
    print("Good Night,",name)

else:
    print(mytime,"is Not a Valid Time,",name)
