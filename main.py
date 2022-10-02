from hello import BankAccount

b1 = BankAccount()

balance = int(input('Print balance: '))
b1.set_balance(balance)

check = True

while check:
    print(f"1: deposit\n2: withdraw\n3: quit")
    choose = int(input('Choose the operation 1 or 2: '))
    if choose == 1:
        deposit = int(input("Deposit: "))
        b1.deposit(deposit)
    if choose == 1:
        withdraw = int(input("Withdraw: "))
        b1.withdraw(withdraw)
    if choose == 3:
        check = False
print(f"Balance = {b1.get_balance()}")
    
