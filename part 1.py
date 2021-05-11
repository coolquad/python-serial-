from graph import *
from bfs import *
file_n = input("")

data = open(file_n, "r").read().split("\n")
data = data[:-1]
n_vertex = int(data[0])

end_ver = []

gr = digraph(n_vertex)
for i in range(len(data[1:])):
    
    t_edge = list(map(int,data[i+1].split(" ")))

    if t_edge[0] == 0:
        end_ver.append(i)

    else:
        for j in t_edge[1:]:
            gr.addEdge(i,j-1)

bfs = BFS(gr, 0 )
count = 0
for i in range(1,n_vertex):
    if not (bfs.hasPathTo(i)):
        count=1
        print ("N")
        break
if count==0:
    print("Y")

sho_path = float('inf')
for k in end_ver:
    bfs_min_dist = bfs.distTo(k)
    if bfs_min_dist < sho_path:
        sho_path = bfs_min_dist

print (sho_path+1)
