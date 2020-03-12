def getCountOfEncMsgs(msg):
    # create an array to store the repeatitive elements
    memo = [None for i in range(len(msg) + 1)]
    return helper(msg, len(msg), memo)


def helper(msg, k, memo):
    # ? If the string is empty we are essentially gonna count it as 1
    if k == 0:
        return 1
    # ? If the string contains 0 as the initial character then we gonna count as 0
    if msg[len(msg) - k] == '0':
        return 0  # count 0

    # ? Check if the memo table contains some value
    if memo[k] != None:
        return memo[k]  # ? If yes then return the value

    # ? We gonna check for the first characters
    result = helper(msg, k-1, memo)

    if k >= 2 and int(msg[len(msg) - k:len(msg) - k + 2]) <= 26:
        # ? then check for the twos characters also
        result = result + helper(msg, k-2, memo)

    # ? Store the result in the memoization table
    memo[k] = result

    return result


print(getCountOfEncMsgs('111'))
