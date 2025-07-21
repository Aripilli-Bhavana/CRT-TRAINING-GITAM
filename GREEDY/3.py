#coins=[1,2,5,10,20,50,100,2000]
#amount=2753
#produce 2753 using minimum number of coins
#coins=[1,10,8]
#amount=16

'''
1. take input from the user
2. sort the coins in descending order [2000,500,100,50,20,10,5,2,1]
3. res=[]
res=[2000,500,100,100,50,2,1]
coins=7---> return 7
'''


def coin_change(coins, amount):
    coins.sort(reverse=True)
    res = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            res.append(coin)
    print("Coins used:", res)
    print("Total coins used:", len(res))

    coins = [1,2,5,10,50,20,500,100,2000]
    amount = 2753
    c=coin_change(coins, amount)
    print("Minimum number of coins:", c)