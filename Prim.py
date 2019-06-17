import heapq
def prim_heap():
    used = [True] * n #True:不使用
    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist,e)
    used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,e)
        res += minedge[0]
    return res

#########################
n,w = map(int,input().split())

edge = [[] for i in range(n)]
#隣接リスト edge[i]:[コスト,行先]
for i in range(w):
    x,y,z = map(int,input().split())
    edge[x].append([z,y])
    edge[y].append([z,x])
print(prim_heap())