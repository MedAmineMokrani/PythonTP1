def sycaruse (a):
        
        while (a != 1):
            if ( a % 2 == 0 and a > 0):
                a = a/2
                print(a)
            elif (a % 2 == 1 and a > 0):
                a =a*3 + 1
                print(a)
        return a


a = int(input())
sycaruse(a)