def divide(dividend, divisor):
    if divisor == 0:
        return "Division by zero not possible"

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    low, high = 0, dividend
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * divisor == dividend:
            ans = mid
            break
        elif mid * divisor < dividend:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return sign * ans


a = int(input())
b = int(input())

print(divide(a, b))
