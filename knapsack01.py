def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]
 
def bruteforce(p, w, m):
    n = len(p)
    bit_strings = get_strings(n)
    max_profit = 0
    solution = ''
 
    for s in bit_strings:
        profit = sum([int(s[i]) * p[i] for i in range(n)])
        weight = sum([int(s[i]) * w[i] for i in range(n)])
    
        if weight <=m and profit > max_profit:
            max_profit = profit
            solution = s
    
    return (solution, max_profit)