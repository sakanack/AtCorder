antena_pos = [int(input()) for _ in range(5)]
k = int(input())

max_dist = antena_pos[-1] - antena_pos[0]

if max_dist <= k:
    print('Yay!')
else:
    print(':(')
