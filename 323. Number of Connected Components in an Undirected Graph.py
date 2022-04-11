Problem:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] 
is the same as [1, 0] and thus will not appear together in edges.

Solution: BFS (261. Repeated)
     
Start from index 0 to n. For each index, use BFS to find all it’s related numbers and append them 
to the visited set, if this index has no more related number then count + 1 and start from next 
index, note that if the index is in visited set. we skip to next index.



def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dist = collections.defaultdict(list)
        for source, target in edges:
            dist[source].append(target)
            dist[target].append(source)
        count = 0
        visited=set()
        queue = collections.deque()
        for x in range(n):
            if x in visited:
                continue
            queue.append(x)
            while queue:
                source=queue.popleft()
                if source in visited:
                    continue
                visited.add(source)
                for target in dist[source]:
                    queue.append(target)
            count+=1
        return count
BigO
Build graph will take O(n) and traversal all number will take O(n). In total is O(2n) where n is the given as the size of the index.
