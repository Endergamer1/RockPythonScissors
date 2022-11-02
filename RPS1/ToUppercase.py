def ToUppercase(x):
    x = str(x).upper()
    return x

Text = input("Enter the Text you wish to convert to Uppercase: ")
Text = ToUppercase(Text)
print("Your Converted input is: " + Text)