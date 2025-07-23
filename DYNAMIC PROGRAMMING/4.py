s=[10,7,19]
amount=45
stock=[]
for p in range(len(s)):#[(10,1),(7,2),(19,3)]
    stock.append((s[p],p+1))  #(0,2)
stock.sort()  # Sort by price
print(stock)
c=0
for stocks in stock:#(19,3)
    price,limit=stocks
    d=amount//price  # How many stocks can be bought
    if d>limit:  # If we can buy more than the limit, buy only
        amount-=price*limit  # Reduce the amount by the total cost
        c+=limit  # Increase the count of stocks bought
    else:
        amount-=price*d
        c+=d
print(c)  # Output: Total number of stocks bought
print(amount)  # Remaining amount after buying stocks