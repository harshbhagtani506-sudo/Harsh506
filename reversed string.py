string = input("enter a string:")
reversed_string = string[::-1]
print(reversed_string)
if string == reversed_string:
      print("it is a palindrome")
else:
      print("it is not a palindrome")
