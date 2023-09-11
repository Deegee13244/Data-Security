import src

def main():
    choice = ''
    while choice != '0':
        print('\nPress 0 to Quit')
        print('Press 1 to Encrypt')
        print('Press 2 to Decrypt')
        print('Press 3 to Generate a Key\n')
        choice = input('Enter your choice: ')
        if choice == '0':
            print('Goodbye!')
        elif choice == '1':
            src.Encrypt()
        elif choice == '2':
            src.Decrypt()
        elif choice == '3':
            keyLength = input('Enter key length: ')
            src.KeyGeneration(int(keyLength))
        else:
            print('Error: Please provide valid number option')
    
if __name__ == '__main__':
    main()