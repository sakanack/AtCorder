A,B,K = map(int, input().split())

takahashi = A - K
aoki = B

if(takahashi < 0):
    aoki = B + takahashi
    takahashi = 0

if(aoki < 0):
    aoki = 0

print(takahashi, aoki)