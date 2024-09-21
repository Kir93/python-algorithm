from bisect import bisect_left
INF = float('INF')

def findLIS():
    dp = [switchToBulb[0][0]] 
    LIS = [(0, switchToBulb[0][1])]

    for i in range(1, N):
        idx, switch = switchToBulb[i]

        if idx > dp[-1]:
            dp.append(idx)
            LIS.append((len(dp)-1, switch))
        else:
            dpIdx = bisect_left(dp, idx)
            dp[dpIdx] = idx
            LIS.append((dpIdx, switch))
    
    return len(dp), LIS

if __name__ == '__main__':
    N = int(input()) 
    switches = list(map(int, input().split()))
    bulbs = list(map(int, input().split()))

    switchToBulb = []

    for switch in switches:
        switchToBulb.append((bulbs.index(switch), switch))

    LISLength, LIS = findLIS()

    print(LISLength)

    cnt = LISLength - 1
    res = [0 for _ in range(LISLength)]

    for (idx, data) in reversed(LIS):
        if cnt == idx:
            res[idx] = data
            cnt -= 1

        if cnt < 0:
            break

    res.sort()
    print(" ".join(map(str, res)))