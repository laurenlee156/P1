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
                if element in matched_dict.values():
                    buyers_preferences[buyer].remove(element)
                else:
                    matched_dict[buyer] = element

    return matched_dict


# #c = stable_stock_matching({"Buyer1" : ["StockA", "StockB", "StockC"],
#                            "Buyer2" : ["StockB", "StockA", "StockC"],
#                            "Buyer3" : ["StockA", "StockB", "StockC"]},
#
#                           {"StockA": ["Buyer1", "Buyer2", "Buyer3"],
#                            "StockB": ["Buyer2", "Buyer1", "Buyer3"],
#                            "StockC": ["Buyer1", "Buyer2", "Buyer3"]
#                         })

