# Temperature Converter
## About the Project
This temperature converter project is a simple program that converts the temperature, provided via input from the user, from celsius to fahrenheit and vice versa.
## How to Use
This program works using any Python interpreter. The user enters which temperature unit they're using and the temperature itself. After pressing Enter, the user is presented with the converted temperature opposite of what was selected from the first input.
## How it Works
The temptype and tempnum variables both hold input functions that take the temperature type to convert from and the temperature number to convert. After pressing Enter, an if/else statement determines which conversion algorithm to perform based on the temptype value, and prints the result as a floating number.

For error handling, an if/else statement checks if the temptype variable was provided with either "Celsius" or "Fahrenheit" as a value. The try/except statement runs the program if a float number was provided in the tempnum variable.
