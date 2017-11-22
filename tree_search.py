# Leetcode interview problem.
# input: 2D graph * = bob, # = food, 0 = traversable, X = wall, \n = new line.  (May be multiple or no paths to food)
# output: length of shortest path to food, or -1 if no path
#  Solved for test cases below in: 16:17 -> 17:40 = 83 mins hmm.
# -> basically DFS/BFS problem plus some parsing.

# Todo: 
# - provide parsers, rewrite DFS and BFS.
# - parsing improvements?

# remember: while checks done at the end.

TESTS = [("""XXXXX
            X*00X
            XXX0X
            X###X
            XXXXX """,4),

        ("""XXXXX
            X*00X
            XXXXX
            X###X
            XXXXX """,-1),

        ("""XXXXX
            X*#0X
            XXX0X
            X###X
            XXXXX""",1),

        ("""XXXXX
            X*00X
            XXX0X
            X000X
            X0XXX 
            X000X
            X0#0X
            XXXXX""",10),

        ("""XXXXXXX
            X*00XXX
            XXX0X0X
            X#0000X
            X0XX#XX 
            X00000X
            X0#000X
            XXXXX""",6)
        ]


def parse_graph(graph_str):
    graph = {0:{}}
    (i,j) = (0,0)
    for line in graph_str.split('\n'):
        j=0
        for ch in line.strip():
            graph[i][j] = ch
            j += 1
        i+=1
        graph[i] = {}
        
    return (i,j,graph)

def find_bob(graph):
    for (i, row) in graph.items():
        for (j, ch) in row.items():
            if ch == "*":
                return (i,j)
    return -1

def valid_coord(L,W,node):
    return (node[0]>=0 and node[0]<=L and node[1]>=0 and node[1]<=W)

def find_valid_neighbour_coords(L, W, node):
    (i,j) = node
    up    = (i-1,j)
    right = (i,j+1)
    down  = (i+1,j)
    left  = (i,j-1)
    neighbours = [up,right, down, left]
    valid_neighbours = [n for n in neighbours if valid_coord(L,W,n)]
    return valid_neighbours


def search(graph_str):
    # Find Bob add to frontier
    (L, W, graph) = parse_graph(graph_str)
    bob_node = find_bob(graph)

    frontier = {(bob_node,0)}
    explored = {bob_node}
    N = 0
    while (N < len(graph_str)) and frontier:        
        # print("frontier:",frontier)
        # print("explored:",explored)
        # Check frontier for food
        (inq, N) = frontier.pop()
  
        # Expand frontier
        valid_neighbours = find_valid_neighbour_coords(L, W, inq)
        explored.add(inq)

        for node in valid_neighbours:
            if graph[node[0]][node[1]] == "0" and not node in explored:
                frontier.add((node,N+1))
            elif graph[node[0]][node[1]] == "#":
                return N+1

    return -1
print("testing:")
i = 0
for (graph, score) in TESTS:
    print(str(i)+": "+"passed" if search(graph) == score else str(i)+": "+"failed")
    i += 1
