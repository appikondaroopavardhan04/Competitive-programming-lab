def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B, T = map(int, input().split())

g = find_gcd(A, B)

if T <= max(A, B) and T % g == 0:
    print("YES")
else:
    print("NO")
