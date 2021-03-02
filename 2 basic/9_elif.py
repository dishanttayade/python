print("If the number you enter is same as the number stored in code you'll see 'Correct!' or the difference otherwise")

num = 45
numin = int(input("Enter the number : "))
if num < numin:
    print("You entered a number ",numin-num," more than it")
elif num > numin:
    print("You entered a number ",num-numin," less than it")
else : 
    print("Correct!")