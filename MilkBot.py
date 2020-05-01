import time
print("Welcome to the 2020 milk survey!")
time.sleep(1)
print("What is your name")

name=input("Name: ")
time.sleep(1)
print(f"Do you like milk {name}? (Y/N)")

answer=input("Answer: ")
original_answer=answer.upper()
while answer.upper()!="Y" or answer.upper()!="YES":
    if answer.upper()=="Y" or answer.upper()=="YES":
        break
    else:
        print('Sorry! thats not the right answer.')
        time.sleep(1)
        print(f'{name}, I think you know the right answer')
        time.sleep(1)
        print(f'Listen to your heart, {name}')
        time.sleep(1)
        print("Do you like milk? (Y/N)")
        time.sleep(1)
        print("ANSWER PROPERLY THIS TIME!")
        answer=input("Answer: ")
    
print('Thank you for taking the 2020 milk survey!')
if original_answer=="Y" or original_answer=="YES": 
    print("")
else:
    time.sleep(2)
    print(f'Remember this for next time, {name}')

time.sleep(2)

print("We're don't care about the survey, we care more that you like milk")
