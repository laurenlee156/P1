def question1(n: dict) -> dict:
    # values in dict 'n' are unique
    # create a new dictionary where keys become values/values become keys
    new_dict = {n[key]: key for key in n}

    return new_dict

def question2(n: dict) -> dict:
    # create a new dictionary where each value from the org. dict is a key in the new dict
    # value of the key is a list of keys from the original dict that had the same value

    # new_dict = {}
    # for key in n:
    #     if n[key] not in new_dict:
    #         new_dict[n[key]] = []
    #     new_dict[n[key]].append(key)

    new_dict = {n[key]: [] for key in n}
    for key in n:
        new_dict[n[key]].append(key)

    return new_dict

def question3(n: dict, n1: dict) -> dict:
    pass


def question4(n: list) -> list:
    pass

a = question2({'a': 1, 'b': 0, 'c': 3, 'd': 4})
b = question4([[1, 2], [3, 2], [1, 5, 3], [6, 5]])
c = question3({'a': 1, 'b': 2}, {'a': 3, 'c': 2})