# Fizz Buzz Game
import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv)-1)

if format(len(sys.argv)-1) == '1':
  try:
    UpperLimit = int(sys.argv[1])
  except ValueError:
      UpperLimit = int(raw_input("Invalid Input -> Please Enter a Number: "))
else:
  try:
    UpperLimit = int(raw_input("Enter Number for Upper Limit of Fizz Buzz Game: "))
  except ValueError:
      UpperLimit = int(raw_input("Invalid Input -> Please Enter a Number: "))
      
print "Fizz Buzz counting up to " + str(UpperLimit)

for x in range (1, UpperLimit+1):
  Result = ''
  if x % 3 == 0:
    Result = "Fizz"
  if x % 5 == 0:
    Result = Result + "Buzz"
  if Result == '':
    Result = str(x)
  print Result

  
  

  