
def menu():
    print("1. sum times")
    print("2. sub times")
    print('3. s convert to h ')
    print('4. h convert to s ')

def sum(x,y):
    result = {}
    result['h']= x['h'] + y['h']
    result['m']= x['m'] + y['m']
    result['s']= x['s'] + y['s']
    if result['s'] >=60 :
        result['m']+= 1
        result['s']-=60

    if result['m'] >=60 :     
        result['m']-=60
        result['h']+=1
    return result

def sub(x,y):
    result = {}
    result['h']= x['h'] - y['h']
    result['m']= x['m'] - y['m']
    result['s']= x['s'] - y['s']
    
    if result['s'] <0 :
        result['s']+=60
        result['m']-=1
    if result['m'] <0 :
        result['m']+=60
        result['h']-=1

    return result

def s_convert_h():
    s=int(input('enter seconde: '))
    result={}
    result['h']= s//3600
    result['m']= (s%3600)//60
    result['s']= (s%3600)%60
    return result

def h_convert_s():
    x = {}
    x['h'] = int(input('enter heure: '))
    x['m'] = int(input('enter minute: '))
    x['s'] = int(input('enter second: '))
    h = int(x['h']) * 3600
    m = int(x['m'])*60
    s = h + m + int(x['s'])
    print(s)

def show(x):
    print(x['h'], ':' ,x['m'], ':' , x['s'])

menu()
ch=int(input("enter your choice: "))

t1  = {'h':2 , 'm':30 , 's':45}
t2 = {'h':3 , 'm':17 , 's':10}

if ch==1: 
    t3 = sum(t1,t2)
    show(t3)

if ch==2:
    t4 = sub(t1,t2)
    show(t4)

if ch==3:
    t5=s_convert_h()
    show(t5)

if ch==4:
    h_convert_s()