#Weight Converter (lbs to kg and vice versa)

weight=int(input('''
What is your weight (enter number)

Weight: '''))

quantifier=str(input('''
(K)g or (l)bs? : '''))

if quantifier=='K' or quantifier=='k' or quantifier=='Kg' or quantifier=='KG' or quantifier=="kg":
    convert=weight*1.45359237
    convert=round(convert,2)
    convert=str(convert)
    print(f"\nYour weight (converted to lbs) is {convert} lbs.")
elif quantifier=="l" or quantifier=="L" or quantifier=="lbs" or quantifier=="LBS":
    convert=weight*0.45359237
    convert=round(convert,2)
    convert=str(convert)
    print(f"\nYour weight (converted to Kgs) is {convert} Kgs.")
else:
    print("\nInvalid input, please try again.")
