class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # hmap = defaultdict(list)
        # current_capital = w
        # for i in range(len(profits)):
        #     heapq.heappush(hmap[capital[i]], -1*profits[i])

        # if k > len(profits):
        #     k = len(profits)
        # while k:
        #     max_capital = max(hmap.keys())
        #     if current_capital in hmap or current_capital > max_capital:
        #         if current_capital < max_capital:
        #             val = -1*heapq.heappop(hmap[current_capital])
                    
        #         else:
        #             val = -1*heapq.heappop(hmap[max_capital])
                    
        #         current_capital += val
        #     k-=1
        # return current_capital

        projects = list(zip(capital, profits))
        projects.sort()
        
        current_capital = w
        available_profits = []  # max heap (use negative values)
        project_idx = 0
        
        for _ in range(min(k, len(profits))):
            # Add all projects we can afford to the heap
            while project_idx < len(projects) and projects[project_idx][0] <= current_capital:
                heapq.heappush(available_profits, -projects[project_idx][1])  # negative for max heap
                project_idx += 1
            
            # If no projects available, break
            if not available_profits:
                break
                
            # Pick the most profitable project
            max_profit = -heapq.heappop(available_profits)
            current_capital += max_profit
        
        return current_capital