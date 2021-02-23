temptype = input("Convert from Celsius or Fahrenheit: ").capitalize()
tempnum = input("Enter Temperature: ")
if temptype == "Celsius":
    print((float(tempnum) * 9/5) + 32)
elif temptype == "Fahrenheit":
    print((float(tempnum) - 32) * 5/9)
else:
    print("That temperature type is not valid.")