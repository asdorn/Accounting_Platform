from balance_pre_year import first_balance, dividends_distribution
from balance_pre_year import buying_inventory, selling_inventory, taking_a_loan, returning_a_loan, issue, profit_loss
from balance_pre_year import buying_permanent_possesion, selling_permanent_possesion, paying_ahead, finance_proportion
from balance_pre_year import transactions, user_choice

def automated_accountant():
    print("""Hello, this is your AUTOMATED ACCOUNTANT PROGRAM.\n
    In the next few seconds, your going to learn the basics of using this program.\n
    First of all, when asked, please enter the required data.\n
    Next, you will have the option to add which ever functions you would want.\n
    Than, you would have a printed full accountant report.\n
    Enjoy!\n""")
    short_term_asset, long_term_assets, short_term_liab, long_term_liab, equity = first_balance()
    equity_pre_year = 0
    assets_pre_year = 0
    assets_after_year = 0
    for sum_of_equity in equity:
        equity_pre_year += sum_of_equity[1]
    for sum_of_assets in short_term_asset:
        assets_pre_year += sum_of_assets[1]
    value_of_issue = 0
    print("""\nFor using a function, please use the next manual:\n
    For using the "Buy Inventory" function, please enter 1.\n
    For using the "Sell Inventory" function, please enter 2.\n
    For using the "Create New Inventory" function, please enter 3.\n
    For using the "Take a loan" function, please enter 4.\n
    For using the "Return a loan" function, please enter 5.\n
    For using the "Return debt" function, please enter 6.\n
    For using the "Issue Shares" function, please enter 7.\n
    For using the "Buy permanent possesion" function, please enter 8.\n
    For using the "Sell permanent possesion" function, please enter 9.\n
    For using the "Paying ahead (rental and etc)" function, please enter 10.\n
    For using the "Clients returning debt" function, please enter 11.\n
    If you finished your actions, please enter 0\n""")
    user_choice()
    dividend = float(dividends_distribution())
    print("\nShort Term Assets")
    total_short_term_assets = 0
    for index_short_assets in short_term_asset:
        if index_short_assets[1] == 0:
            continue
        else:
            print(index_short_assets[0],"\t",index_short_assets[1])
        total_short_term_assets += index_short_assets[1]
    assets_after_year += total_short_term_assets
    print("Short term Assets total sum:\t",total_short_term_assets)
    print("\nLong term Assets")
    total_long_term_assets = 0
    for index_long_assets in long_term_assets:
        if index_long_assets[1] == 0:
            continue
        else:
            print(index_long_assets[0],"\t",index_long_assets[1])
        total_long_term_assets += index_long_assets[1]
    assets_after_year += total_long_term_assets
    print("Long term Assets total sum:\t",total_long_term_assets)
    print("\nShort term Liabilities")
    total_short_term_liab = 0
    for index_short_liab in short_term_liab:
        if index_short_liab[1] == 0:
            continue
        else:
            print(index_short_liab[0],"\t",index_short_liab[1])
        total_short_term_liab += index_short_liab[1]
    print("Short term Liabilities total sum:\t",total_short_term_liab)
    print("\nLong term liabilities")
    total_long_term_liab = 0
    for index_long_liab in long_term_liab:
        if index_long_liab[1] == 0:
            continue
        else:
            print(index_long_liab[0],"\t",index_long_liab[1])
        total_long_term_liab += index_long_liab[1]
    print("Long term Liabilities total sum:\t",total_long_term_liab)
    print("\nEquity")
    total_equity = 0
    for index_equity in equity:
        if index_equity[1] == 0:
            continue
        else:
            print(index_equity[0],"\t",index_equity[1])
        total_equity += index_equity[1]
    print("Equity total sum:\t",total_equity)
    net_profit = float(profit_loss())
    print("\nStatments of changes in Equity")
    print("Equity pre year:\t",equity_pre_year)
    print("Issue:\t", value_of_issue)
    print("Net Profit:\t",net_profit)
    print("Dividends distributed:\t", dividend)
    print("Equity end of year:\t",equity_pre_year + value_of_issue + net_profit - dividend)
    print("\nFinancial ratio")
    finance_proportion()
    if ((assets_pre_year + assets_after_year) / 2) != 0:
        print("ROA:\t", (net_profit / ((assets_pre_year + assets_after_year) / 2)))
    else:
        print("ROA is None")
    if ((equity_pre_year + total_equity) / 2) != 0:
        print("ROE:\t", (net_profit / ((equity_pre_year + total_equity) / 2)))
    else:
        print("ROE is None")
    print("\nTransactions:")
    transactions()
automated_accountant()