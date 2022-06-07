"""
Source: Project ihttps://www.freecodecamp.org/news/python-projects-junior-developers/
Project : Odd or even

Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know.

Example:

Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?  

"""

# welcome message
print("Welcome to Odd or Even!\nEnter a number to check, or 'end' to finish\n")

# set the running variable to on
running_active = True

while running_active:
  number = input('Please enter a number: ')

  #End program if 'end' entered
  if number.lower() == 'end':
    print('thank you for playing')
    running_active = False
  else:

    #Check the input type and only passing integer type
    try:
      val = int(number)
    
    except ValueError:
      print('Sorry but you did not enter an integer, please try again\n')

    #The bulk of the code runs if no error detected 
    else:
      
    #Set the input type to integer for check if it is odd or even
      number = int(number)
      
      #check if input number is odd or even using modulo
      if (number % 2) == 0:
        print(str(number) + " is even\n")
      #elif used to make odd/even check well defined
      elif (number % 2) == 1:
        print(str(number) + " is odd\n")
