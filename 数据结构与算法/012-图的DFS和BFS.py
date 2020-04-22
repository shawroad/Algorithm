"""

@file  : 012-图的DFS和BFS.py

@author: xiaolu

@time  : 2020-04-22

"""
def BFS(graph, s):
    # 需要一个队列
    queue = list()
    queue.append(s)

    # 看是否访问当前节点
    seen = set()

    seen.add(s)

    result = []
    while len(queue) > 0:
        vertex = queue.pop(0)  # 为了让当前出来的这个节点的周围节点进入
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:   # 判断当前节点有没有被访问
                queue.append(w)
                seen.add(w)
        result.append(vertex)
    return result


def DFS(graph, s):
    # 其实并不难，只要把队列改成栈就可以了
    stack = list()
    stack.append(s)

    seen = set()
    seen.add(s)

    result = []
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:  # 如何判断是否访问过，使用一个数组
                stack.append(w)
                seen.add(w)
        result.append(vertex)
    return result


if __name__ == '__main__':
    # 定义一个图的结构,类似于邻接表的方式存储
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    S = 'A'  # 起始点从A开始
    bfs_res = BFS(graph, S)
    print(bfs_res)

    dfs_res = DFS(graph, S)
    print(dfs_res)




