temptype = input("Convert from Celsius or Fahrenheit: ").lower()
if temptype == "celsius" or temptype == "fahrenheit":
    tempnum = float(input("Enter Temperature: "))
    try:
        if temptype == "celsius":
            print((tempnum * 9/5) + 32)
        elif temptype == "fahrenheit":
            print((tempnum - 32) * 5/9)
    except:
        print("Invalid character entered.")
else:
    print("Invalid temperature type entered.")
