a = " A B C D E "
n = 0

for x in a:
    n = n + 2
    print(a[1:n])

    if n == 8:
        print(a[1:10])
        break
