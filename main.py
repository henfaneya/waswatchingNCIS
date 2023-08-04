print("This program converts miles to kilometers.")
print()

def miles_to_kilometers(miles):
    kilometers = miles * 1.609
    print(miles, "mile(s) is", kilometers, "kilometers.")

def convert():
    try:
        number_of_miles = int(input("Enter the number of miles driven: "))

        miles_to_kilometers(number_of_miles)

    except:
        print("That's not a number. Try again.")
        print()
        convert()

convert()