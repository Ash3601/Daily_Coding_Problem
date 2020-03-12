def get_next_permute(input):
    # inp_arr = str(input).split()
    inp_arr = [int(d) for d in str(input)]
    i = len(inp_arr) - 2
    j = len(inp_arr) - 1
    # print(inp_arr)

    while i >= 0:
        # print('Value is ', inp_arr[i])
        if (int(inp_arr[i]) > int(inp_arr[j])) == False:
            inp_arr[i], inp_arr[j] = inp_arr[j], inp_arr[i]
            # print('In')
            break
        i -= 1
        j -= 1
    inp_arr[j:] = sorted(inp_arr[j:])
    for i in range(len(inp_arr)):
        inp_arr[i] = str(inp_arr[i])

    return int(''.join(inp_arr))


ans = get_next_permute(48975)
print('Ans: ', ans)
