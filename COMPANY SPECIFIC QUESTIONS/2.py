s1=inptu()#beads
s2=input()#leaps
s3=set(s1)
s4=set(s2)
s=s3.intersection(s4)#"aes"-->"eas"
print("".join(sorted(s)))#"eas" 

