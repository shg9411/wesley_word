
def solve():
    n = int(input())
    maxPay = 0
    pay = list(map(int, input().split())) + [0]
    stack = []
    for i in range(len(pay)):
        while stack and pay[stack[-1]] > pay[i]:
            val = stack.pop()
            if not stack:
                break
            x = i-1-stack[-1]
            tmpPay = x * pay[val]
            if tmpPay > maxPay:
                maxPay = tmpPay
        stack.append(i)
    print(maxPay)


if __name__ == '__main__':
    solve()
