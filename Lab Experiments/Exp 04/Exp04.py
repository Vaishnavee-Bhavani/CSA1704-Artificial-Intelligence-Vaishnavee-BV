import itertools

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    # S and M cannot be zero as they are leading digits
    for perm in itertools.permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0:
            continue
        
        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y

        if send + more == money:
            return {'SEND': send, 'MORE': more, 'MONEY': money, 'Mapping': dict(zip(letters, perm))}

# Test Run
result = solve_cryptarithmetic()
print("--- Crypt-Arithmetic Problem ---")
print(f"SEND  = {result['SEND']}")
print(f"MORE  = {result['MORE']}")
print(f"MONEY = {result['MONEY']}")
print("Digit Mapping:", result['Mapping'])
