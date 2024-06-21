import re 

# batRegex = re.compile(r'(Ha){3,5}?')
# mo1 = batRegex.search('HaHaHaHaHaHa')
# print(mo1.group())


# email = '123456abc@gmail.com'
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+      # username
#     @                      # @ symbol
#     [a-zA-Z0-9.-]+         # domain name
#     (\.[a-zA-Z]{2,4})       # dot-something
#     )''', re.VERBOSE)

# if re.match(emailRegex, email):
#     print('valid')
# else:
#     print('not valid')


password = '12345@ aS'
passwordRegex = re.compile(r'''(
    ^                       # Start of the string
    (?=.*[a-z])             # Ensure the string has at least one lowercase letter
    (?=.*[A-Z])         # Ensure the string has at least one uppercase letter
    (?=.*\d)       # Ensure the string has at least one digit
    .{8,}           # Ensure the string is at least eight characters long 
    $               # End of the string         
    )''', re.VERBOSE)

if re.match(passwordRegex, password):
    print('valid')
else:
    print('not valid')