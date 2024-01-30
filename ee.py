name = input('Enter Name: ')
slist = name.split()

initials = ''
for part in slist:
    initials += part[0]

print('Initials:', initials.upper())  
