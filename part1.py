def read_calls(file: open) -> {(str, str): int}:
    # purpose: store a database containing the # of times every person called another person
    # dictionary: contains a 2 tuple of str (caller/callee) with an int (# of times caller called callee)
    # output: each line can contain the name of the caller followed by each callee they called, names will be separated by colons
    # returns a dictionary w/ the 2nd line

    # define the empty dictionary and list
    calls_dict = {}
    tuples_lst = []

    # open the .txt file
    with open(file, 'r') as f:
        # .readlines() returns a list containing each line in the file as a list item
        lines_lst = f.readlines()

        for string in lines_lst:
            # b cannot call b, etc.
            # break up the string into individual elements
            characters = [c for c in string]
            for char in characters:
                if char != ':' and char != '\n' and characters[0] != char:
                    char_tuple = (characters[0], char)
                    tuples_lst.append(char_tuple)

        # count occurences of tuples in tuples_lst
        for i in tuples_lst:
            count = tuples_lst.count(i)
            calls_dict[i] = count

        return calls_dict

def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    # takes a dict argument and returns a dictionary in the form of data structure 2
    # data structure 2: dictionary's keys are CALLERS, each caller is associated with a dictionary whose keys are the callee with the value of int
    reversed_dict = {}
    value_dict = {}

    for key in calls:
        if
    print(reversed_dict)




a = call1to2({('a', 'b'): 2, ('a', 'c'): 1, ('b', 'a'): 3, ('b', 'c'): 1, ('c', 'a'): 1, ('c', 'd'): 2})

