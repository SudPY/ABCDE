a = " A B C D E "
n = 12

for x in a:
    n = n - 2
    print(a[1:n])

    if n == 4:
        print(a[1])
        break
