#Uses python3

def lcs2(a,b,lookup):
    #write your code here

    key = str(a) + str(b)     # '[a][b]'

    if key not in lookup.keys():

        if len(a)==0 or len(b)==0:
            lookup[key] = 0

        elif a[0]==b[0]:
            lookup[key] = lcs2(a[1:],b[1:],lookup)+1

        else:
            lookup[key] = max(lcs2(a[1:],b,lookup),lcs2(a,b[1:],lookup))

    return lookup[key]

if __name__ == '__main__':

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    lookup = dict()
    ans = lcs2(a,b,lookup)

    print(ans)

