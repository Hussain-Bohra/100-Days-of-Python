# do while loop Example :-

# 'True' condition means run loop infinite times.
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  # if number is 0 or greater than 0 then exit from loop
  if not number > 0:
  # to exit from loop we use 'break' statement
    break
