def menu():
    print("1: sum")
    print("2: sub")
    print("3: mul")

def sum(m,n):
    result={}
    result['a']= m['a'] + n['a']
    result['b']= m['b'] + n['b']
    return result

def mul(m,n):
    result = {}
    result['a']= m['a'] * n['a']
    result['b']= m['a'] * n['b']
    result['c']= m['b'] * n['a']
    result['d']= m['b'] * n['b']
    result['c'] += result['b']
    print(result['a'],'+',result['c'],'i +',result['d'],'i*i')

def sub(m,n):
    result={}
    result['a']= m['a'] - n['a']
    result['b']= m['b'] - n['b']
    if result['b']==0 :
        print(result['a'])
    else:
        if m['b']>n['b']:
            print(result['a'] ,'+', result['b'], 'i')
        elif m['b']<n['b']:
            print(result['a'] , result['b'], 'i')
def show(m):
    print(m['a'] ,'+', m['b'] ,'i')  

# a+bi
x = {'a':3 , 'b':10}
y = {'a':1 , 'b':7}

menu()
ch=int(input("your choice: "))

if ch==1:
    b1=sum(x,y)
    show(b1)

if ch==2:
    sub(x,y)    

if ch==3:
    mul(x,y)    