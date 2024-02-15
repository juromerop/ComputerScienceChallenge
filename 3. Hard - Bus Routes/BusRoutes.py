class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        def convert_to_adjacency_list(routes):
            adj_list = {}
            for route in range(len(routes)):
                for stop in routes[route]:
                    if stop not in adj_list:
                        adj_list[stop] = set()
                    adj_list[stop].add(route)
            return adj_list
        def bfs(adj_list, routes, source, target):
            pass
            # To implement
        adj_list = convert_to_adjacency_list(routes)
        return bfs(adj_list, routes, source, target)