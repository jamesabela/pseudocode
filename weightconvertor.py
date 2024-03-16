def convert_pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453592
    return kilograms

weight = float(input("Enter weight: "))

unit = input("Is the weight in (K)g or (P)ounds? ").upper()

if unit == "P":
    weight = convert_pounds_to_kilograms(weight)
    print(f"Weight in kilograms: {weight}")
elif unit == "K":
    print(f"Weight in kilograms: {weight}")
else:
    print("Invalid unit")
