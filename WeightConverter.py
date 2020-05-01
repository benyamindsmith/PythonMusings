weight=int(input('''
What is your weight (enter number)
Weight: '''))

quantifier=str(input('''
(K)g or (l)bs? : '''))

if quantifier.upper()=='K'  or quantifier.upper()=='KG':
    convert=weight*1.45359237
    convert=round(convert,2)
    convert=str(convert)
    print(f"\nYour weight (converted to lbs) is {convert} lbs.")
elif quantifier.upper()=="L" or quantifier.upper()=="LB" or quantifier.upper=="LBS":
    convert=weight*0.45359237
    convert=round(convert,2)
    convert=str(convert)
    print(f"\nYour weight (converted to Kgs) is {convert} Kgs.")
else:
    print("\nInvalid input, please try again.")
