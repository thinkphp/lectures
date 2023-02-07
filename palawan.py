def insertsort(arr):

    size = len( arr )

    for i in range(1, size ):
        j = i - 1
        aux = arr[i]

        while j >= 0 and arr[j] > aux:
              arr[j+1] = arr[j]
              j -= 1

        arr[j+1] = aux

def palawan():

    arr = [ -5, 4, -3, 2, 1, 0 ]

    print( arr )

    insertsort( arr )

    print( arr )

    a,b,c = -33, 8,-110
    if a > b:
        if c > a:
            print(c, a, b)
        elif c > b:
            print(a, c, b)
        else:
            #c >= b
            print(a, b, c)
    else:
        #it means b <= a
        if c > b:
            print(c, b, a)
        elif c > a:
            print(b, c, a)
        else:
            print(b, a, c)

palawan()
