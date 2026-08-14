# Bank Account Program

This is a simple Python program to manage a bank account. 
thsi  is a explaination of how it works

## What this code does

I made a class called `BankAccount` , a class is like a blueprint  it tells Python what a bank account should have (owner name, balance) and what it can do (deposit, withdraw, show balance)

## Step by step workflow

### 1. Creating the account
```python
account = BankAccount('Tejal', 5000)
```
This line creates a new account for `Tejal` with  balance `5000` as aobject.

Behind the code , the `__init__` method runs automatically nand saves the details for self of account 
```python
def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
```

### 2. Depositing money
```python
account.deposit(1500)
```
This calls the `deposit` method which simply adds the amount to the balance
```python
def deposit(self, amount):
    self.balance += amount
```
So balance becomes `5000 + 1500 = 6500`.

### 3. Withdrawing money
```python
account.withdraw(1000)
```
This calls `withdraw` which first checks if there is enough balance:
```python
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
    else:
        print("Insufficient balance")
```
Since `1000` is less than `6500` it goes through. Balance becomes `6500 - 1000 = 5500`

- If someone tries to withdraw more money than the balance it won't allow it 
- it will prints `"Insufficient balance"` 

### 4. Showing the balance
```python
account.show_balance()    #method
```
This just prints the current balance:
```python
def show_balance(self):
    print(f"Balance is :{self.balance}")
```
Output: `Balance is :5500`
