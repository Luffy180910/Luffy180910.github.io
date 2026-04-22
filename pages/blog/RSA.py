def quick_mi(a,b,mod_n):
    ans=1
    while(b):
        if(b&1):
            ans=(ans*a)%mod_n
        a=(a*a)%mod_n
        b=b>>1
    return ans

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

def mod_inverse(e, n):
    gcd, x, y = extended_gcd(e, n)
    
    if gcd != 1:
        raise ValueError("e 和 n 不是互质的，无法计算模逆元")
    
    return x % n if x < 0 else x

p=9437
q=9439
N=p*q
r=(p-1)*(q-1)
print(r)

e=65537
print(extended_gcd(e,r))
d=mod_inverse(e,r)
print(d)


n=20030526
c=quick_mi(n,e,N)
print(c)
s=quick_mi(c,d,N)
print(s)




