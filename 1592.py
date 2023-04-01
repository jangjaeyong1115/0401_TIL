N,M,L = list(map(int,input().split()))

list = [0]*N

first = 0
list[first] = 1
cnt = 0
while True:
    
    if list[first] == M:
        print(cnt)
        break

    if list[first]%2 == 0:
        first = abs((first-L) % N)
        list[first] += 1
        cnt += 1

    else:
        first = (first+L)%N
        list[first] +=1
        cnt +=1
        