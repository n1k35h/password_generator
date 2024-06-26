import random       # import random module to get random data output

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@£$%^&*(),.?' # Random character will be picked from this value to create a random password

num = int(input('\nHow many Passwords do you want to generate? ')) # This will give the user the number of password that they want to generate e.g: 7 passwords - so computer will randomly output 7 different passwords

len = int(input('\nEnter the Character length of the Password? ')) # This will output the length of the password e.g: 9 characters long 

print('\nHere are your automated Password: \n')

# This is the for loop to generate random password until the number of password and lengths have been met
for pwd in range(num):
    password = ''
    for c in range(len):
        password += random.choice(chars)
    print(password)
    print('\n')