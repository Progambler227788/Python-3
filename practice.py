import collections
# root = 0

# que_with_brackets = collections.deque([root])


# print("Deque with brackets:")
# print("Type:", type(que_with_brackets))
# print("Contents:", que_with_brackets)

# # print('\n')
# # que_with_brackets = collections.deque(root)

# # print("Deque without brackets:")
# # print("Type:", type(que_with_brackets))
# # print("Contents:", que_with_brackets)


def bfs(graph,root):
    visited = set()
    que = [root]
    while que:
        vertex = que.pop(0) # pop first element of que
        
        visited.add(vertex) # add node mark as visit
        print(que)
        for i in graph[vertex]:
            if i not in visited:
                que.append(i)
    print(visited)
    print(graph)
    
visited = set()
def dfs(graph,root):
    global visited
    if root not in visited:
        print(root)
        visited.add(root)
        for i in graph[root]:
            dfs(graph,i)
 
    
graph = {0:[1,2,3],1:[0,3],3:[0,1,3],2:[0,3]}
bfs( graph ,  2)

dfs( graph ,  0)


a = "greatest"
a[0:4] = 'b','e','s','t'