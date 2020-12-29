N, K = map(int, input().split())
R,S,P = map(int, input().split())
T = input()

wp = { 
    "r": P,
    "s": R,
    "p": S 
}
wc = { 
    "r": "p",
    "s": "r",
    "p": "s" 
}

commandHistory = [""] * N
point = 0
for i in range(N):
    machineCommand = T[i]
    if(i < K):
        point += wp[machineCommand]
        commandHistory[i] = wc[machineCommand]
    if(i >= K):
        if(commandHistory[i - K] == wc[machineCommand]):
            commandHistory[i] = ""
        else:
            point += wp[machineCommand]
            commandHistory[i] = wc[machineCommand]
print(point)