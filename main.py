"""Coffee machine water coffee
1. expresso 50 18 1.5
2. latte 200 24 150 2.5
3. cappuccino 250 24 100 3.0

coin operateed
1 2 5 10 20

report

"""
def check(a,b,c,val):
    if val==1:
        if a-200<0:
            return (a,b,c,0)
        if b-24<0:
            return(a,b,c,0)
        if c-150<0:
            return (a,b,c,0)
        return (a-200,b-24,c-150,1)
    if val==2:
        if a-15<0:
            return (a,b,0)
        if b-18<0:
            return(a,b,0)
        return (a-15,b-18,1)

    if val==3:
        if a-250<0:
            return (a,b,c,0)
        if b-24<0:
            return(a,b,c,0)
        if c-100<0:
            return(a,b,c,0)
        return (a-250,b-24,c-100,1)

a,b,c=1000,1000,1000
cond=True
while cond:

    print("""This is a Coffee Machine
You can choose :
expresso
latte
cappuccino
You can enter:
off - turn off the machine
report - to get details on remaining resources""")
    p=0
    p1=100
    p2=200
    p3=300
    val = input()
    if val=="report":
        print('Water',a,'ml')
        print('Coffee',b,'ml')
        print('Milk',c,'ml')
    elif val=="off":
        print('The machine is turning off')
        cond=False
    else:
        one=int(input('Enter the number of ₹1 coins : ₹'))
        two=int(input('Enter the number of ₹2 coins : ₹'))
        five=int(input('Enter the number of ₹5 coins : ₹'))
        ten=int(input('Enter the number of ₹10 coins : ₹'))
        twenty=int(input('Enter the number of ₹20 coins : ₹'))
        total=one+(two*2)+(five*5)+(ten*10)+(twenty*20)
        if val=="latte":
            coffee="latte"
            a,b,c,chk=check(a,b,c,1)
            if chk==0:
                print('Insufficient quantity 1')
                continue
            p=p2
        elif val=="expresso":
            coffee="expresso"
            a,b,chk=check(a,b,0,2)
            if chk==0:
                print('Insufficient quantity 2')
                continue
            p=p1
        elif val=="cappuccino":
            coffee="cappuccino"
        
            a,b,c,chk=check(a,b,c,3)
            if chk==0:
                print('Insufficient quantity 3')
                continue
            p=p3
        change = total-p

        if change>=0:
            print(f'Here is your ₹ {change}')
            print(f'Here is your {coffee} , Enjoy it !!!')
        else:
            print("Insufficient amount !!!")

