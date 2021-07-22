class passwordMG:
    def __init__(self):
        print('WELCOME TO PASSWORD MANAGER')
        self.username = 'user'   //username is 'user'
        self.password = 'user12'  //password is 'user12'

    def login(self):
        def passwordGenerator():
            import random
            min = 3
            max = 12
            k = 'qwertyuioplk123456788jhgfdsazxcvbnm!@#$%&'
            passd = ''.join(random.choice(k) for i in range(min, max))
            print(f'SAFE PASSWORD: {passd}')

        def options():
            while True:
                print('\t1.Save new password')
                print('\t2.View saved passwords')
                print('\t3.Generate new password')
                print('\t4.Quit')

                option = str(input('Please select option: '))
                if option == '1':
                    site = str(input('Enter Site: '))
                    username = str(input('Enter username: '))
                    password = str(input('Enter password: '))

                    def files():
                        with open('SAVED PASSWORDS', 'a') as f:
                            f.write(f'\n{site}')
                            f.write(f'\t{username}')
                            f.write(f'\t{password}')
                            f.close()

                    files()
                    print(f'Your {site} password and username have been saved successfully')
                    break

                elif option == '2':
                    def savedPass():
                        with open('SAVED PASSWORDS', 'r') as q:
                            print('YOUR SAVED PASSWORD')
                            print(F'\t{q.read()}')
                            q.close()

                    savedPass()
                    break
                elif option == '3':
                    passwordGenerator()
                    return 'Thank you!'
                    break

                elif option == '4':
                    break

                else:
                    print('Selected option currently un available')
        while True:
            username = str(input('Enter username(user): '))
            password = str(input('Enter password(user12): '))
            if password == self.password:
                options()
                break
            else:
                print('Login details not recorgnised')

k = passwordMG()
print(k.login())
