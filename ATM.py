import random, time

def CheckDigit(value):
        return (value.isdigit());

def transaction():
    global balance
    print("""
to check your balance press 1
to Withdraw press 2  
to Deposit press 3
to quit press 4""")
    Option = (input('Select Option: '))
    if CheckDigit(Option):
        if Option == '1':
            print('Balance', balance, '$')
            another()

        elif Option == '2':
            print('Balance', balance,'$')
            Withdraw = int(input('Enter Withdrawal amount '))
            if Withdraw > 0 and Withdraw<=balance:
                balance = (balance - Withdraw)
                print('new balance is  ', balance, '$')
                another()
            elif Withdraw > balance:
                print('Your balance is not sufficient ')
                another()
            else:
                print('None withdraw made')
                another()
        elif Option == '3':
            print('Balance', balance, '$')
            Deposit = int(input('Enter deposit amount '))
            if Deposit > 0:
                balance = (balance + Deposit)
                print('new balance is ', balance, '$')
                another()
            else:
                print('None deposit made')
            another()
        elif Option == '4':
            exit('Thank you for using ATM')

        else:
            print('try again')
            transaction()
    else:
        print('try again')
        transaction()
    return;
def another():
    answer = input('Would you like to make another transaction y/n?: ')
    if answer == 'y':
        transaction()
    elif answer=='Y':
        transaction()
    else:
        exit("Thank you for using ATM")
    return ;
def start():
    attempts = 0
    while attempts < 3:
        pincode = input('Enter PIN code: ')
        if CheckDigit(pincode):
            if pincode == '1234':
                print('Access granted')
                transaction()
                break
            else:
                if (attempts == 2):
                    exit('The card has been retained')
                    break
                else:
                    print('Access denied.Try again')
                    attempts += 1
        else:
            print('Error,try again')
    return ;
balance = random.randint(100, 1000)
print('welcome')
time.sleep(0.5)
start()


