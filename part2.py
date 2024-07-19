def question1(n: dict) -> dict:
    # values in dict 'n' are unique
    # create a new dictionary where keys become values/values become keys
    return {n[key]: key for key in n}

def question2(n: dict) -> dict:
    # new_dict = {}
    # for key in n:
    #     if n[key] not in new_dict:
    #         new_dict[n[key]] = []
    #     new_dict[n[key]].append(key)

    return {value: [key for key, val in n.items() if val == value] for key, value in n.items()}

def question3(n1: dict, n2: dict) -> dict:
    return {key: n1.get(key, 0) + n2.get(key, 0) if key in n1 and key in n2 else n1.get(key, 0) or n2.get(key, 0)
                for key in sorted(n1.keys()) + sorted(n2.keys())}
def question4(n: list) -> list:
    return [element for lst in range(0, len(n) - 1) for element in n[lst] if element in n[lst] and element in n[lst + 1]]

a = question2({'a': 1, 'b': 0, 'c': 3, 'd': 4, 'e': 4})
b = question4([[1, 2], [3, 2], [1, 5, 3], [6, 5]])
c = question3({'a': 1, 'b': 2}, {'a': 3, 'c': 2})
