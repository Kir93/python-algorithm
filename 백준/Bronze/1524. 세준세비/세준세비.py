for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    n_army = sorted(list(map(int, input().split())), reverse=True)
    m_army = sorted(list(map(int, input().split())), reverse=True)
    while n_army and m_army:
        if n_army[-1] >= m_army[-1]:
            m_army.pop()
        else:
            n_army.pop()

    if n_army: print('S')
    elif m_army: print('B')
    else: print('C')