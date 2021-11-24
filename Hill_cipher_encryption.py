import math
import numpy

def convert_cipher(text1, keyarray):
   text='abcdefghijklmnopqrstuvwxyz'
   ll1=[]
   for i in text1:
       ll1.append(text.index(i))
   num=numpy.array(ll1)
   result=numpy.dot(keyarray, num)
   return result%26    

print('\nStep: 1')   
plain=input('Enter your plain text: ')
key=input('Enter your key: ')
text='abcdefghijklmnopqrstuvwxyz'
cipher=''
leng=math.floor(math.sqrt(len(key)))
if (math.sqrt(len(key))-leng) == 0:
    l1=[]
    l3=[]
    for i in key:
        l1.append(i)
    for i in l1:
        l3.append(text.index(i))
    keyarr=numpy.array(l1)
    nkeyarr=numpy.array(l3)
    newarr = keyarr.reshape(leng, leng)
    nnewarr = nkeyarr.reshape(leng, leng)
else:
    print('Your key should be perfect square of some number')
print('\nStep: 2\n')
print(newarr)
if not len(plain)%leng == 0:
    a1=leng-(len(plain)%leng)
    for i in range(a1):
        plain+='x'
print('\nStep: 3\n')        
l2 = [(plain[i:i+leng]) for i in range(0, len(plain), leng)]  
print(l2)

for i in l2:
    cipherno=convert_cipher(i, nnewarr)
    for j in cipherno:
        cipher+=text[j]
print('\nStep: 4')
print(f'\nCipher Text: {cipher}')
