s = 'CMLIV'
a ={ 'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500, 'M':1000}
r = 0
for i in range(len(s)):
    if i+1 < len(s) and a[s[i]]<a[s[i+1]]:
        r -= a[s[i]]
    else:
        r += a[s[i]]
print (r)