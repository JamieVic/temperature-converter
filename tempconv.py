temptype = input("Convert from Celsius or Fahrenheit: ").capitalize()
if temptype == "Celsius" or temptype == "Fahrenheit":
    tempnum = input("Enter Temperature: ")
    try:
        if temptype == "Celsius":
            print((float(tempnum) * 9/5) + 32)
        elif temptype == "Fahrenheit":
            print((float(tempnum) - 32) * 5/9)
    except:
        print("Invalid character entered.")
else:
    print("Invalid temperature type entered.")
