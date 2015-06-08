import itertools


def checkio(matrix):
    target = [0, 225, 315]
    rods = list(zip(*matrix))
    total_effect = lambda move, side_effects: sum(move * effect for effect in side_effects) % 360
    ranges = [range(-180, 181, l) for l in [sum(rod) for rod in rods]]
    print(list(ranges[1]))
    print(ranges[1])
    print(ranges[1])


    for r in itertools.product(*ranges):
        x = [total_effect(move, side_effects) for side_effects, move in zip(rods, r)]
        print(x)

        if r == target:
            return list(r)


print(checkio([[1,2,3],[3,1,2],[2,3,1]]))