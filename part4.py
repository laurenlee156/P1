def stable_stock_matching(buyers_preferences, stocks_preferences):
    # initialize the first pair
    first_key = list(buyers_preferences.keys())[0]
    # check what the first element of the buyer's preferences is and add to matched_dict
    matched_dict = {first_key: buyers_preferences[first_key][0]}
    buyers_preferences[first_key].remove(buyers_preferences[first_key][0])


    # remove the first key first value in every other value list
    for buyer in buyers_preferences:
        if buyer != first_key:
            for element in buyers_preferences[buyer]:
                if element not in matched_dict.values():
                    matched_dict[buyer] = element
                    break
                else:
                    buyers_preferences[buyer].remove(element)

    return matched_dict


# c = stable_stock_matching({"A" : [1, 2, 3],
#                            "B" : [2, 1, 3],
#                            "C" : [1, 2, 3]},
#
#                           {"StockA": ["Buyer1", "Buyer2", "Buyer3"],
#                            "StockB": ["Buyer2", "Buyer1", "Buyer3"],
#                            "StockC": ["Buyer1", "Buyer2", "Buyer3"]
#                         })
#
# print(c)