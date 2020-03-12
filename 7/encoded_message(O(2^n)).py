def getCountOfMsgs(msg):
    # mappings
    return helper(msg, len(msg))


def helper(msg, k):
    # ? BASE CASE
    if k == 0:  # meaning we do have an empty string ""
        return 1  # we can count it as 1

    s = len(msg) - k

    # if the msg contains a 0 then we will return a zero (since no message can be encoded with it)
    if msg[s] == '0':
        return 0  # ! if the question starts from 0123 then no message can be encoded

    # at some point the string will gonna be empty or k == 0 at that point
    result = helper(msg, k - 1)
    # we will count as 1 and thus we get the answer

    if k >= 2 and int(msg[s: s+2]) <= 26:
        result = result + helper(msg, k-2)

    return result


print(getCountOfMsgs('123'))
