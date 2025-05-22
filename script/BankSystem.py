# 
# 
# 
# 
# 
# 
from pickle import *
from time import strftime,sleep

layout=('accountnum','password','name','age','income','started','balance','[transaction]')

try:
    with open("bank.dat","rb"):...
except Exception:
    with open("bank.dat","wb")as file:dump(f"{layout}",file)

def str_lst(x):
    x=x.strip("(").strip(")").replace("'","").replace(" ","").split(",")
    x[7]=[x[7][1:-1]]
    return x

def magic(a,money,info):
    x=a[7][0]
    y=f"{x} | {money} {info}"
    a[7]=[y]
    return a

def listmaker():
        main=[]
        with open("bank.dat","rb") as file:
            try:
                while 1:
                    data=load(file)
                    main+=[str_lst(data)]
            except Exception:...
        return main

def passinp(x=0):  
    m=n=o=0
    if x==1:
        user=input("Enter the password:")
        sleep(1)
        return user
    print("Password must only contain [a-b,A-B,0-9] and minimum 7 character")
    user=input("Enter the password: ")
    if len(user)<7:passinp(x)
    user2=list(user)
    for i in user2:
        if 64<ord(i)<91:m=1
        elif 96<ord(i)<123:n=1
        elif 47<ord(i)<58:o=1
    if m==1 and n==1 and o==1:
        sleep(1)
        return user
    print("This password doesnt satisfy the condition, try again\n")
    passinp(x)

def accinp():

    try:
        user=int(input("Enter your 12 digit account number:"))
        if len(str(user))!=12:raise Exception
    except Exception:
        print("Only 12 numbers please")
        accinp()
    return user

def allaccnum():

    with open("bank.dat","rb") as file:
        main=[]
        try:
            while 1:
                num=load(file)
                main+=[str_lst(num)[0]]
        except Exception:...
    return tuple(main)

def accnumgen():   
    from random import randrange
    num=randrange(10**11,(10**12)-1)
    if num in allaccnum():accnumgen()
    return(num)

def open_account(name,age,income):  
    useraccnum=accnumgen()
    print(f"Hello {name.capitalize()}",end=" ") 
    print("You are qualified to open your account here\n")
    sleep(1)
    print(f"Your account number is {useraccnum}\n")
    user=passinp()
    main=(useraccnum,user,name,age,income,
          f"{strftime("%Y/%m/%d_%H:%M:%S")}",0,[])
    with open("bank.dat","ab") as file:dump(f"{main}",file)
    sleep(1)
    print("Account created successfully\n")

def close_account(accountnum,password):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            del main[x]
            m=1
    if m==0:
        sleep(1)
        print(f"Unable to close account {accountnum}\n")
        return None
    print("Are you sure you want to close your account? [y/n]:",end="")
    sleep(3)
    user=input().lower()
    if user=="y" or user=="yes":
        print("Closing account....")
        sleep(2)
        with open("bank.dat","wb") as file:
            for i in main:dump(str(tuple(i)),file) 
            print("Account has be closed permanently\n")
    else:
        print("Account closing cancelled\n")

def balance(accountnum,password):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            m=1
            print(f"Total balance in {accountnum} is {main[x][6]} Rs\n")
            return None
    if m==0:
        sleep(1)
        print(f"Unable to connect with account {accountnum}\n")
        return None

def deposit_money(accountnum,password,money):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            main[x][6]=int(main[x][6])+int(money)
            main[x]=magic(main[x],money,
                          f"_Rs_CR_on_{strftime('%Y/%m/%d_%H:%M:%S')}")
            m=1
    if m==0:
        sleep(1)
        print("Could not find account")
        print(f"Unable to deposit {money} Rs to account {accountnum}\n")
        return None
    with open("bank.dat","wb") as file:
        for i in main:
            i=tuple(i)
            dump(str(i),file)
        print(money,"Rs has been deposited to",accountnum)
    balance(accountnum,password)

def withdraw_money(accountnum,password,money):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            main[x][6]=int(main[x][6])-int(money)
            if int(main[x][6]) <=0:
                print("Insufficent balance")
                return None
            main[x]=magic(main[x],money,
                          f"_Rs_DR_on_{strftime('%Y/%m/%d_%H:%M:%S')}")
            m=1
    if m==0:
        sleep(1)
        print("Could not find account")
        print(f"Unable to withdraw {money}Rs from account {accountnum}\n")
        return None
    with open("bank.dat","wb") as file:
        for i in main:
            i=tuple(i)
            dump(str(i),file)
        print(money,"Rs has been withdrawed from",accountnum)
    balance(accountnum=accountnum,password=password)

def last_transaction(accountnum,password):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            m=1
            main=main[x][7][0].split("|")
            main=main[-1].split("_")
            print(f"Last transaction of account {accountnum} was of",end=" ")
            for i in main:print(i,end=" ")
            print("\n")
            return None
    if m==0:  
        sleep(1) 
        print(f"Unable to connect with account {accountnum}\n")
        return None

def all_transactions(accountnum,password):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            main=main[x][7][0].split("|")
            main=main[1:]
            for count,i in enumerate(main):
                i=i.replace("_"," ")
                print(f"{count+1}: {i}")
            balance(accountnum,password)
            m=1
            return None
    if m==0:
        sleep(1)
        print(f"Unable to connect with account {accountnum}\n")
        return None

def user_details(accountnum,password):
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            print(list(layout[2:6]))
            print(main[x][2:6])
            all_transactions(accountnum,password)
            m=1
            return None
    if m==0:
        sleep(1)
        print(f"Unable to connect with account {accountnum}\n")
        return None

def change_password(accountnum,oldpass,newpass):   
    main=listmaker()
    m=0
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(oldpass):
            main[x][1]=newpass
            m=1
    if m==0:
        sleep(1)
        print(f"Unable to change password of of account {accountnum}\n")
        return None
    with open("bank.dat","wb") as file:
        for i in main:
            i=tuple(i)
            dump(str(i),file)
        print("Change successful\n")


def transfer(accountnum,password,receiver,money):
    if accountnum==receiver:
        print("You cant transfer money to yourself")
        return None
    main=listmaker()
    for x,y in enumerate(main):
        if y[0]==str(accountnum) and y[1]==str(password):
            main[x][6]=int(main[x][6])-int(money)
            if int(main[x][6]) <=0:
                print("Insufficent balance")
                return None
            a=x
            break
    try:
        if a:...
    except Exception:
        sleep(1)
        print(f"Could not connect to user account\n")
        return None  
    for x,y in enumerate(main):
        if y[0]==str(receiver):
            main[a]=magic(main[a],money,
            f"_Rs_TR_to_{receiver}_on_{strftime('%Y/%m/%d_%H:%M:%S')}")
            main[x][6]=int(main[x][6])+int(money)  
            main[x]=magic(main[x],money,
            f"_Rs_RE_from_{accountnum}_on_{strftime('%Y/%m/%d_%H:%M:%S')}")
            m=x
            break     
    try:
        if m:...
    except Exception:
        sleep(1)
        print(f"Reciever account not found\n")
        return None  
    with open("bank.dat","wb") as file:
        for i in main:
            i=tuple(i)
            dump(str(i),file)
        print(money,"Rs has been transfered from",accountnum,"to",receiver)
    balance(accountnum=accountnum,password=password)

def account_graph(accnum,password):
    import matplotlib.pyplot as plt 
    main=[]
    for x,i in enumerate(listmaker()):
        if i[0]==str(accnum) and i[1]==str(password):
            creation=i[5].replace("_"," ")
            main+=i[7][0].split("|")
            m=1
    try:m
    except Exception:
        print("Could not connect to account")
        return None
    main=main[1:]
    for x,i in enumerate(main):
        m="-"
        temp=main[x].split("_")
        if temp[2] in ["CR","RE"]:m="+"    
        main[x]=[temp[0],m,f"{temp[-2]} {temp[-1]}" ]      
    y_axix=[0]
    x_axix=[creation]
    temp=0
    for x,i in enumerate(main):
        if i[1]in"+":
            y_axix+=[temp+int(i[0])]
            temp=temp+int(i[0])
        else:
            y_axix+=[temp-int(i[0])]
            temp=temp-int(i[0])
        x_axix+=[i[2]]
    plt.plot(x_axix,y_axix,linewidth=3,marker="o",linestyle="dotted",label="Amount")
    plt.xlabel("Date and Time")
    plt.ylabel("Balance")
    plt.title(f"Balance in account {accnum}")
    plt.xticks(rotation=90)
    plt.legend(loc="upper left")
    plt.show()

def show_all(password="hide"):
    main=listmaker()
    sleep(1)
    if password.lower()=="hide":
        for count,i in enumerate(main):
            print(f"{count}: [{i[0]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}, {i[6]}]")
        print("\n")
    else:
        for count,i in enumerate(main):
            print(f"{count}: {i[:-1]}")
        print("\n")

def bank(): 
    print("""
1: To open new account, needs name, age and income.
2: To close account, needs account number and password.
3: To deposit money in account, needs account number, password and amount.
4: To withdraw money from account, needs account number, password and amount.
5: To check balance, needs account number and password.
6: To last transaction, needs account number and password.
7: To check all transactions, needs account number and password.
8: To to see detail of a user, needs account number and password.
9: To change password, needs account number, old password and new password.
10: To transfer money, needs account number, password, receiver account number and amount.
11: To see statement in form of graph, needs account number, password.
12: To show all the account in bank.
anything: To restart.     
    """)
        
    user=input("[1-10] or exit:").lower()

    if user=="1":
        name=input("Enter your name:").capitalize().replace(" ","_")
        age=input("Enter your age:")
        income=input("Enter your income:")
        try:
            if int(age) <18 or int(income)<5000:
                print("You arent not qualified to open your account here")
                bank()
        except Exception:
            print("Only digits please")
            bank()
        open_account(name,age,income) 

    elif user=="2":
        accnum=accinp()
        password=passinp(1)
        close_account(accnum,password)

    elif user=="3":
        accnum=accinp()
        password=passinp(1)
        try:
            amount=int(input("Enter amount:"))
        except Exception:
            print("Only digits please")
            bank()
        deposit_money(accnum,password,amount)

    elif user=="4":
        accnum=accinp()
        password=passinp(1)
        try:
            amount=int(input("Enter amount:"))
        except Exception:
            print("Only digits please")
            bank()
        withdraw_money(accnum,password,amount)

    elif user=="5":
        accnum=accinp()
        password=passinp(1)
        balance(accnum,password)

    elif user=="6":
        accnum=accinp()
        password=passinp(1)
        last_transaction(accnum,password)

    elif user=="7":
        accnum=accinp()
        password=passinp(1)
        all_transactions(accnum,password)

    elif user=="8":
        accnum=accinp()
        password=passinp(1)
        user_details(accnum,password)

    elif user=="9":
        accnum=accinp()
        oldpass=passinp(1)
        newpass=passinp()
        change_password(accnum,oldpass,newpass)
    
    elif user=="10":
        accnum=accinp()
        password=passinp(1)
        reciever=accinp()
        try:
            amount=int(input("Enter amount:"))
        except Exception:
            print("Only digits please")
            bank()
        transfer(accnum,password,reciever,amount)

    elif user=="11":
        accnum=accinp()
        password=passinp(1)
        account_graph(accnum,password)

    elif user=="12":
        show_all(password="")

    elif user=="exit" or user=="e":
        print("Thank you for using our service")
        exit()

    else:bank()

    bank()

bank()