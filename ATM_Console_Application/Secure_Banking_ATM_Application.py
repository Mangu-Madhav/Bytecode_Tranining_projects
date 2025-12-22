#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ATM Console Application
balance = 50000           
correct_pin = 2004 
attempts = 1
max_attempts = 3
pin=int(input("Please insert card and enter pin:"))
while(attempts<max_attempts and pin!=correct_pin):
    print("you have left only",max_attempts-attempts,"attempts")
    attempts+=1
    pin=int(input("enter correct pin"))
    print(attempts)
if(attempts==3 and pin!=correct_pin):
    print("YOur Card has blocked")
else:
    print("Access Granted!!!...")
    n=0
    while(n!=5):
        print("\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Change PIN\n5. Exit\nChoose(1-5):")
        n=int(input())
        match(n):
            case 1:
                print("your Balance:",balance)
            case 2:
                withdraw=float(input("enter amount to withdraw"))
                if(withdraw<balance):
                    if(withdraw%100==0):
                        balance=balance-withdraw
                        print("Please collect your Cash\n Your Balance is",balance)
                    else:
                        print("please enter only mulitples of 100 (eg.. 100, 2100, 5000, 6200 etc..)")
                else:
                    print("Insufficient Amount")
            case 3:
                Deposit_amt=float(input("enter the amount to be deposited.."))
                balance=balance+Deposit_amt
                print("your balance is",balance)
            case 4:
                old_pin=int(input("enter old pin"))
                if(old_pin==correct_pin):
                    new_pin=int(input("enter any 4 digit new pin"))
                    n=new_pin
                    c=0
                    while(n>0):
                        n=n//10
                        c+=1
                    if(c==4):
                        correct_pin=new_pin
                        print("New pin Updated..Successfully")
                    else:
                        print("please enter only 4 digit pin")
                else:
                    print("Incorrect old pin..")
    else:
        print("Exiting....")





