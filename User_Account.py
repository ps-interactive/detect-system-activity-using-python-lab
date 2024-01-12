from datetime import date
# Get a list of current users

with open ('/etc/passwd','r') as file:
    Current_users = []
    for line in file:
        line = (line.split(':')[0])
        Current_users.append(line)
print(Current_users)

# Get a list of known_good users

with open ('Known_users.txt','r') as file:
    Known_users = []
    for user in file:
        user = user.strip()
        Known_users.append(user)
print(Known_users)

# Unverified users

Unknown_Users = []

for user in Current_users:
    if user not in Known_users:
        Unknown_Users.append(user)
print(Unknown_Users)

# Write to log file

if Unknown_Users != []:
    file1 = open('security.log', 'a')
    alert = 'There is a new user on the account '
    today = date.today()
    str_date = str(today) + '\n'
    Malicious_Users = str(Unknown_Users) + ' '
    file1.write(alert)
    file1.write(Malicious_Users)
    file1.write(str_date)
    file1.close()

# chmod 777 security.log
