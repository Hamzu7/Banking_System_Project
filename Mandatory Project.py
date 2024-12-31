#!/usr/bin/env python
# coding: utf-8

# In[35]:


def create_account():
    name = input("Enter account holder's name: ").strip()
    account = {
        "name": name,
        "balance": 0.0,
        "transaction": []
    }
    print(f"Account created successfully for {name} with a balance of {account['balance']}")
    return account


# In[37]:


def deposit(account):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        account['balance'] += amount
        account['transaction'].append(f"Deposit: ${amount}")
        print(f"${amount} deposited successfully! New balance: ${account['balance']}")
    else:
        print("Deposit amount must be positive.")


# In[38]:


def withdraw(account):
    amount = float(input("Enter withdrawal amount: "))
    if amount > 0:
        if account['balance'] >= amount:
            account['balance'] -= amount
            account['transaction'].append(f"Withdrawal: ${amount}")
            print(f"${amount} withdrawn successfully! New balance: ${account['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Withdrawal amount must be positive.")


# In[39]:


def check_balance(account):
    print(f"Current balance: ${account['balance']}")


# In[40]:


def print_statement(account):
    print(f"Transaction statement for {account['name']}:")
    if account['transaction']:
        for transaction in account['transaction']:
            print(transaction)
        print(f"Final balance: ${account['balance']}")
    else:
        print("No transactions available.")


# In[ ]:


def main():
    print("Welcome to the Banking System")
    account = create_account()

    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Print Transaction Statement")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            deposit(account)
        elif choice == '2':
            withdraw(account)
        elif choice == '3':
            check_balance(account)
        elif choice == '4':
            print_statement(account)
        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

