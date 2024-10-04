# class Solution(object):
#     def dividePlayers(self, skill):
#         """
#         :type skill: List[int]
#         :rtype: int
#         """
#         dic = {}
#         s = sum(skill) // (len(skill) // 2)
#         res = []
#         for i,r in enumerate(skill):
#             if s - r in dic:
#                 res.append(r*skill[dic[(s-r)]])
#                 dic.pop(s-r)
#             else:
#                 dic[r] = i
    
#         if len(res) == (len(skill) // 2):
#             return sum(res)
#         else:
#             return -1
        
class Solution(object):
    def dividePlayers(self, skill):
        n = len(skill)
        total_skill = sum(skill)

        # Check if total skill can be evenly distributed
        if total_skill % (n // 2) != 0:
            return -1

        target_skill = total_skill // (n // 2)
        skill_map = Counter(skill)
        total_chemistry = 0

        # Iterate through unique skill values
        for curr_skill, curr_freq in skill_map.items():
            partner_skill = target_skill - curr_skill

            # Check if valid partner skill exists with matching frequency
            if (
                partner_skill not in skill_map
                or curr_freq != skill_map[partner_skill]
            ):
                return -1

            # Calculate chemistry for all pairs with this skill
            total_chemistry += curr_skill * partner_skill * curr_freq

        # Return half of total chemistry (as each pair is counted twice)
        return total_chemistry // 2