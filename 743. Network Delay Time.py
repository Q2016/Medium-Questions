Question:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible 
for all the n nodes to receive the signal, return -1.













Solution: DFS, Dijkstra (Edjucational)
    
https://www.youtube.com/watch?v=EaphyqKU4PQ
Approach #1: Depth-First Search [Accepted]

Let's record the time dist[node] when the signal reaches the node. If some signal arrived earlier, we don't need to broadcast it anymore. 
Otherwise, we should broadcast the signal.

Algorithm

We'll maintain dist[node], the earliest that we arrived at each node. When visiting a node while elapsed time has elapsed, if this is the 
currently-fastest signal at this node, let's broadcast signals from this node.
To speed things up, at each visited node we'll consider signals exiting the node that are faster first, by sorting the edges.


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
        
        
Complexity Analysis

Time Complexity: 
O(N^N + E log E) where E is the length of times. We can only fully visit each node up to N−1 times, one per each other node. 
Plus, we have to explore every edge and sort them. Sorting each small bucket of outgoing edges is bounded by sorting all of them, because of repeated use 
of the inequality xlogx+ylogy≤(x+y)log(x+y).

Space Complexity: 
O(N + E), the size of the graph O(E), plus the size of the implicit call stack in our DFS O(N).


Approach #2: Dijkstra's Algorithm [Accepted]
Intuition and Algorithm

We use Dijkstra's algorithm to find the shortest path from our source to all targets. This is a textbook algorithm, refer to this link for more details.
Dijkstra's algorithm is based on repeatedly making the candidate move that has the least distance travelled.
In our implementations below, we showcase both O(N^2) (basic) and O(NlogN) (heap) approaches.

Basic Implementation

class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
        

Heap Implementation


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1
