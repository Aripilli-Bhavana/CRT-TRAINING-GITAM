'''you are given an array of n strings, you have to find out the number of balanced strings from the given array.
 The string is said to be balanced if and only if its middle character has equal non-zero count in the left substring and right substring.
 note: while checking the balance consider the middle character exclusively.
 input : 5
 output : 3
'''

def balanced(l): #aabaaba
    c=0
    for p in l:
        if(len(p)%2==0):
            f=0

        else:
            m=len(l)//2 #7//2=3
            mi=p[m]#a
            fh=p[:m]#aab
            sh=p[m+1:]#aba
            f1=fh.count(mi)#2
            s1.sh.count(mi)#2
            if(f1!=s1):
                f=0
        if(f==1):
            c=c+1
    return c

n=int(input())
l=[]
for p in range(n):
    s=input()
    l.append(s)
c=balanced(l)
print(c)
