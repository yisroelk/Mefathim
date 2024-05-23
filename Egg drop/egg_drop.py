def recursive_egg_drop(h:int, k:int):
    for x in range(k):
        recursive_egg_drop(x - 1, k - 1)
        recursive_egg_drop(h - x + 1 , k)
    