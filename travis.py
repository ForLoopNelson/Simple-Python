known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry' ]

while True:
    print('Hi! My name is Travis')
    name = input('What is your name?: ').strip().capitalize()

    if name in known_users:
        print('Hello {}! And welcome'.format(name))
        remove = input('Would you like to removed from the system (y/n)?: ').lower().strip()

        if remove == 'y':
            known_users.remove(name)
            print('You have been removed.')
        elif remove == 'n' :
            print("Good. We don't want you to leave!")
        
    else:
        print("Hmmmm I don't think I have met you yet {}".format(name))
        add_me = input('Would you like to be added to the system (y/n)?: ').lower().strip()

        if add_me == 'y':
            known_users.append(name)
            print('You have been added to the system {}.'.format(name))
            print(known_users)
        elif add_me == "n" :
            sign_off = input("No worries, would you like to exit (y/n)?: ").strip().lower()

        if sign_off == 'y':
            exit()
        elif sign_off == 'n' :
            continue
        
            
            
            
            
            
        
