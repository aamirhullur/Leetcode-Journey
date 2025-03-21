class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        supplies = set(supplies)
        while True:
            found = False
            for i in range(len(recipes)):
                if recipes[i] in res:
                    continue
                if all(x in supplies for x in ingredients[i]):
                    supplies.add(recipes[i])
                    found = True
                    res.append(recipes[i])

            if not found:
                break
        return res