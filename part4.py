def stable_stock_matching(buyers_preferences, stocks_preferences):
    # buyers can be matched to only one stock
    # first buyer matches, second and third cannot match to that stock

    matched_dict = {}

    buyer_pref_lst = [(buyer, buyers_preferences[buyer]) for buyer, stock in buyers_preferences.items()]
    stock_pref_lst = [(stock, stocks_preferences[stock]) for stock, buyer in stocks_preferences.items()]

    for tuple in buyer_pref_lst:
        for tuple2 in stock_pref_lst:

    print(buyer_pref_lst)
    print(stock_pref_lst)



            #
            # if buyer_pref_lst[0] == stock_pref_lst[0]:
            #     matched_dict[buyer] = stock
            #     buyer_pref_lst.remove()



c = stable_stock_matching({"Buyer1" : ["StockA", "StockB", "StockC"],
                           "Buyer2" : ["StockB", "StockA", "StockC"],
                           "Buyer3" : ["StockA", "StockB", "StockC"]},

                          {"StockA": ["Buyer1", "Buyer2", "Buyer3"],
                           "StockB": ["Buyer2", "Buyer1", "Buyer3"],
                           "StockC": ["Buyer1", "Buyer2", "Buyer3"]
                        })
