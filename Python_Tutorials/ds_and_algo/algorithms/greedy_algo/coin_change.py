# You are given different denominations and total amt of money. Find the min no. of coins that
# you need to make up the given amount.

# Solution: find the largest coin that is less than the given total number e.g. 201 with 100(max number)
# If the max number is less than the number with which we are comparing then take the max number in our
# case 100 and store it, then subtract it with from the value 201 - 100 = 101
# Again take the max number from the list in our case again it would 100 and compare it with the subtracted
# number, if the max number is still less than the number with which we want to compare again subtract
# i.e. 101 - 100 = 1, again repeat
# If total number becomes 0 then print result else repeat step 2 and 3

def coin_change(total_amount, coins_needed):
    coins_needed.sort()
    index = len(coins_needed) - 1

    while True:
        coins_value = coins_needed[index]
        if total_amount >= coins_value:
            print(coins_value)
            total_amount = total_amount - coins_value
        if total_amount <= coins_value:
            index -= 1
        if total_amount == 0:
            break


coins = [1, 2, 5, 20, 50, 100]
coin_change(201, coins)


