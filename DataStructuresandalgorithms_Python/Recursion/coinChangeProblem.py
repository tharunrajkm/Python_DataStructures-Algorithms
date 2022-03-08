def rec_coin(target,coins):

    min_coins = target
    print('target is ',target)

    if target in coins:
        return 1

    else:
        # For every coin value that is less than or equal to my target value
        for i in (c for c in coins if c <= target):
            print('i is ',i)
            num_coins = 1 + rec_coin(target - i , coins)
            if num_coins < min_coins:
                print('n_c',num_coins)
                min_coins = num_coins
                #print('min_coin is', min_coins)
        
    return min_coins



print(rec_coin(10,[1,5]))
#print(rec_coin(15,[1,5,10]))