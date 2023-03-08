def sum_possible(amount, numbers, memo={}):
    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for n in numbers:
        if sum_possible(amount - n, numbers, memo) == True:
            memo[amount] = True
            return True

    memo[amount] = False
    return False


print(sum_possible(13, [6, 2, 1])) # -> True
