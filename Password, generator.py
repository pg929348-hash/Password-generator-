import random
options = ['a', 'b', 'c', 'd', '1', '2', '3', '4', '$', '#', '~', '!']
namaking = 0

while namaking < 6:
    enter = input("\nEnter the number of characters for password: ").strip()
    
    if enter.isdigit():
        length = int(enter)
        if length <= 0:
            print("Length zero se badi honi chahiye!")
            continue
        password_list = []
        for i in range(length):
            password_list.append(random.choice(options))
        generated_password = "".join(password_list)
        print("The password is:", generated_password)
        namaking += 1  
    else:
        print("Invalid entry! Please enter numbers only.")
