Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#while loop
n=int(input("enter no.:"))
enter no.:10
i=1
while i<=10:
    print(i,end='')
    i+=1

    
12345678910
#even no.
num=int(input("enter no.:"))
enter no.:15
i=1
while i<=15:
    if 1 % 2 == 0 :
        print(i, end=' ')

        
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    if 1 % 2 == 0 :
KeyboardInterrupt




w
print(i)


while i<=15:
    if 1 % 2 == 0 :
        print(i, end=' ')

#even no.
        
num=int(input("enter no."))
enter no.15
i=1
while i<=15:
    if i % 2 == 0 :
        print(i,end=' ')

        
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    if i % 2 == 0 :
KeyboardInterrupt

num=int(input("enter no."))
enter no.15
i=1
while i<=15:
    if i % 2 == 0 :
        print(i,end=' ')
        
SyntaxError: multiple statements found while compiling a single statement
num=int(input("enter no.:"))
enter no.:15
i=1
while i<=15:
    if i % 2 == 0 :
        print(i)
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    if i % 2 == 0 :
KeyboardInterrupt
    i+=1

n=int(input("enter no."))
enter no.10
i=1
while i<=10:
    if i % 2 == 0 :
        print(i)
    i += 1

    
2
4
6
8
10
num=int(input("enter no.:"))
enter no.:15
i=1
while i<=15:
    if i%2!=0:
        print(i)
    i+=1

    
1
3
5
7
9
11
13
15
#sum of natural no.
n=int(input("enter the no."))
enter the no.13
i=1
while i<=13:
    i=1
KeyboardInterrupt
num=int(input("enter no.:"))
enter no.:13
i=1
sum=0
while i<=13:
    sum=sum+i
    print(i)
    i+=1

    
1
2
3
4
5
6
7
8
9
10
11
12
13
num=int(input("enter no."))
enter no.10
sum=0
i=1
while i<=num:
    sum=sum+i
    print(sum)
    i+=1

    
1
3
6
10
15
21
28
36
45
55
n=int(input("enter the no."))
enter the no.12
i=1
sum=0
while i<=n:
    if i % 2 == 0 :
        sum=sum+1
        print(sum,end=' ')
        i+=1

        
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    if i % 2 == 0 :
KeyboardInterrupt
    i+=1

n=int(input("enter the no."))
enter the no.12
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
        print(sum,end=' ')
    i+=1

    
2 6 12 20 30 42 
n=int(input("enter the no."))
enter the no.10
i=1
sum=0
while i<=n:
    sum=sum+1
    i+=1
print(sum,end=' ')
SyntaxError: invalid syntax
n=int(input("enter the no."))
enter the no.10
s=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)
SyntaxError: invalid syntax
while i<=n:
    sum=sum+i
    i+=i
    print(sum)

    
1
3
7
15
n=int(input("enter the no."))
enter the no.10
while i<=n:
    sum
KeyboardInterrupt
n=int(input("enter the no."))
enter the no.10
sum=o
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    sum=o
NameError: name 'o' is not defined
i=1
sum=0
while i<=n:
    sum=sum+1
    i+=1

    
print(sum)
10
n=int(input("enter the no."))
enter the no.15
i=1
s=0
while i <=n
SyntaxError: expected ':'
while i <=n:
    if i%2==0:
        sum=sum+i
    i+=1

    
print(sum)
66
#sum of odd no.
n=int(input("enter the no."))
enter the no.13
i=1
sum=0
while i<=n
SyntaxError: expected ':'
KeyboardInterrupt
n=int(input("enter the no."))
enter the no.10
i=1
s=0
while i<=n:
    if i%2!=0:
        s=s+i
    i+=1

    
print(s)
25
n=int(input("enter the no."))
enter the no.20
s=0
i=1
while i<=n:
    if i%2!=0:
        s=s+i
    i+=1

    
print(s)
100
#reverse no.
n=int(input("enter the no."))
enter the no.10
i=n
while i>=n:
    print(i)
    i-=1

    
10
n=int(input("enter the no."))
enter the no.10
i=n
while i>=1:
    print(i)
    i-=1

    
10
9
8
7
6
5
4
3
2
1
#factorial no.
n=int(input("enter the no."))
enter the no.5
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1

    
print(fact)
120

#prime or not
n=int(input("enter the no."))
enter the no.10
i=2
while i<n:
    if n%i==0:
        print("not prime")
    i+=1

not prime
not prime
n=int(input("enter the no."))
enter the no.10
i=2
while i<n:
    if n%i==0:
...         print("not prime")
...     i+=1
... 
...     
not prime
not prime
>>> n=int(input("enter the no."))
enter the no.3
>>> i=2
>>> while i<n:
...     if n%i==0:
...         ptint("not prime")
...         i+=1
... 
...     
Traceback (most recent call last):
  File "<pyshell#188>", line 2, in <module>
    if n%i==0:
KeyboardInterrupt

>>> #multiplication
>>> n=int(input("enter the no."))
enter the no.3
>>> i=1
>>> while i<=10:
...     print("3 x ",i,"=",3*i)
...     i+=1
... 
...     
3 x  1 = 3
3 x  2 = 6
3 x  3 = 9
3 x  4 = 12
3 x  5 = 15
3 x  6 = 18
3 x  7 = 21
3 x  8 = 24
3 x  9 = 27
3 x  10 = 30
