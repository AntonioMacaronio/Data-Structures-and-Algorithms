class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import collections, heapq
        graph = defaultdict(list) # maps
        for edge in times:
            source, target, time = edge[0], edge[1], edge[2]
            graph[source].append((target, time))
        
        visited = set()
        pathCost = [float('inf') for i in range(n+1)] # goes from 0 to n, exclude 0 for simplicity 
        pathCost[k] = 0
        nodesToExplore = [(0, k)] # min node is closest node
        heapq.heapify(nodesToExplore)

        while len(nodesToExplore) > 0:
            cost, nodeToExplore = heapq.heappop(nodesToExplore)
            if nodeToExplore in visited:
                continue
            visited.add(nodeToExplore)
            for edge in graph[nodeToExplore]:
                neighbor, time = edge
                pathCost[neighbor] = min(pathCost[nodeToExplore] + time, pathCost[neighbor])
                if neighbor not in visited:
                    heapq.heappush(nodesToExplore, (pathCost[neighbor], neighbor))
        
        pathCost.pop(0)
        return max(pathCost) if len(visited) == n else -1 
