class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for x in tickets:
            g[x[0]].append(x[1])

        for key in g.keys():
            g[key].sort()

        
        res = []

        def dfs(node):
            while g[node]:
                next_val = g[node].pop(0)
                dfs(next_val)
            res.append(node)

        dfs("JFK")

        return res[::-1]
        

        