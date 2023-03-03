def cakes(recipe, available):
    cakes = 0
    while True:
        for i,j in recipe.items():
            try:
                if available[i] < j:
                    return cakes
                else:
                    available[i] -= j
            except:
                return cakes
        cakes += 1
