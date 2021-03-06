# 1
# Storing first name in lowercase letters into a variable
fname = "Jeff"


# 2
# Storing last name in uppercase letters into a variable
lname = "Bezos"


# 3
# Printing first name in uppercase and last name in lowercase letters
print("Hello,",fname.upper(),lname.lower())


# 4
# Printing two newlines
print("\n\n")



# 5
# Storing first name and last name together into a variable
fullname = fname + " " + lname


# 6
# Printing only last name from the variable in step 5 using 
# string slicing and index() method
print(fullname[fullname.index(' ')+1:])


# 7
# Replacing last name from the variable in step 5 with the given message and printing it
fullname = fullname[:fullname.index(' ')+1] + lname + ", Walsh College Student"
print(fullname)


# 8
# Printing the given quatation message
print('"Technology is nothing. What is important is that you have a faith in people, that theyre basically good and smart, and if you give them tools, they will do wonderful things with them- Steve Jobs"')


# 9
# Stroing two decimal numbers into two variables
num1 = 5.0
num2 = 3.0


# 10
# Storing the sum, difference, product, and division of num1 and num2 
# into four variables
add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2


# 11
# Printing sum using string concatenation method
print(str(num1) + " plus " + str(num2) + " equals " + str(add))
# Printing difference using comma concatenation method
print(num1,"minus",num2,"equals",sub)
# Printing product using string format() method
print("{} multiplied by {} equals {}".format(num1, num2, mult))
# Printing division using f-string method
print(f"{num1} divided by{num2} equals {div}")


# 12
# Storing square root of variable mult into a variable and printing it
sq_root = round(mult ** (1/2), 2)
print(f"The square root of {mult} equals {sq_root:.2f}")


# 13
# Storing month name and day into two variables
month = "October"
day = 28


# 14
# Printing month and day using percentail(%) printing method
print("\t\tToday is day %d of the month of %s." % (day, month))

