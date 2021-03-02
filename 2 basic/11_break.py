print("Enter a string if its same as the one stored in code the program will stop running")

pas  = 'password'
while True: 
    inp = input("Enter the password : ")
    if inp == pas: 
        print("Correct!")
        print("Access Granted!")
        break

