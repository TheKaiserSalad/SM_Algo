def sm_algo(a: int, b: int, c: int) -> int:
    b = bin(b).replace("0b", "")
    ans = a

    for i in b[1:]:
        if i == "0":
            ans = (ans ** 2) % c
        else:
            ans = (ans ** 2) % c
            ans = (ans * a) % c
    print(ans)

sm_algo(26, 521654984984941651321694987498465165, 16)