def sum(x,y):
    result={}
    result['s']= x['s'] * y['m'] + y['s'] * x['m']
    result['m']= x['m'] * y['m']
    return result

def mul(x,y):
    result={}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result

def sub(x,y):
    result={}
    result['s'] = x['s'] * y['m'] - y['s'] * x['m']
    result['m'] = x['m'] * y['m']
    return result

def div(x,y):
    result={}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result

def show(x):
    print(x['s'] ,'/', x['m'])

a = {'s':2 , 'm':3}
b = {'s':4 , 'm':7}

c=sum(a,b)
print("sum: ")
show(c)

d=mul(a,b)
print("mul: ")
show(d)

e=sub(a,b)
print("sub: ")
show(e)

f=div(a,b)
print("div: ")
show(f)