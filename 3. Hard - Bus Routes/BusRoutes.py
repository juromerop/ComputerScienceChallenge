'''
My solution to the problem uses a BFS approach to find the minimum number of buses to reach the destination.
I create a dictionary that maps each stop to the routes that pass through it.
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_routes = defaultdict(set)
        for route in range(len(routes)):
            for stop in routes[route]:
                stop_to_routes[stop].add(route)
        queue = deque([(source, 0)])
        visited = set([source])
        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses
            for route in stop_to_routes[stop]:
                for next_stop in routes[route]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append((next_stop, buses+1))
                routes[route] = []
        return -1