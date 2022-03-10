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

def finance_proportion():
    short_asset_sum = 0
    long_asset_sum = 0
    asset_total_sum = 0
    short_liab_sum = 0
    long_liab_sum = 0
    liab_total_sum = 0
    equity_total_sum = 0

    for counting_sum_short_asset in short_term_asset:
        short_asset_sum += counting_sum_short_asset[1]
        asset_total_sum += counting_sum_short_asset[1]
    for counting_sum_long_asset in long_term_assets:
        long_asset_sum += counting_sum_long_asset[1]
        asset_total_sum += counting_sum_long_asset[1]
    for counting_sum_short_liab in short_term_liab:
        short_liab_sum += counting_sum_short_liab[1]
        liab_total_sum += counting_sum_short_liab[1]
    for counting_sum_long_liab in long_term_liab:
        long_liab_sum += counting_sum_long_liab[1]
        liab_total_sum += counting_sum_long_liab[1]
    for counting_sum_equity in equity:
        equity_total_sum += counting_sum_equity[1]
    if short_liab_sum == 0:
        print("Current proportion is None")
    else:
        current_ratio = (short_asset_sum / short_liab_sum)
        print("Curent Ratio is",current_ratio)
    if liab_total_sum == 0:
        print("Asset to Liabilities ratio is None")
    else:
        assets_to_liab = (asset_total_sum / liab_total_sum)
        print("Assets to liabilities ratio is",assets_to_liab)
    if equity_total_sum == 0:
        print("Liabilities to Equity ratio is None")
    else:
        liab_to_equity = (liab_total_sum / equity_total_sum)
        print("liabilities to Equity ratio is",liab_to_equity)

def clients_paying_back():
    amount_payed_back = float(input("Please enter the amount of cash your clients payed you back: "))

    for looking_for_clients in short_term_asset:
        if looking_for_clients[0] == "Clients to pay":
            looking_for_clients[1] = looking_for_clients[1] - amount_payed_back
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] + amount_payed_back

    clients_to_pay_transaction.append(["Down",amount_payed_back])
    cash_transaction.append(("Up",amount_payed_back))

def returning_expenses_to_pay():
    global cash_transaction
    global expense_to_pay_transaction

    how_much_to_return = float(input("Please enter the amount that you are returning: "))

    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] - how_much_to_return
    for looking_for_expenses_to_be_payed in short_term_liab:
        if looking_for_expenses_to_be_payed[0] == "Expenses to be payed":
            looking_for_expenses_to_be_payed[1] = looking_for_expenses_to_be_payed[1] - how_much_to_return

    cash_transaction.append(["Down",how_much_to_return])
    expense_to_pay_transaction.append(["Down",how_much_to_return])

def create_new_inventory():
    global cash_transaction
    global inventory_transaction
    global expense_to_pay_transaction

    used_inventory = float(input("Please enter the amount of Inventory that was used to create the new Inventory: "))
    new_inventory_amount = float(input("Please enter the amount of Inventory that was created: "))
    salary_per_unit = float(input("Please enter the price of creating each unit: "))
    paying_now_or_future = input("Did you pay the whole sum now? enter 'yes' or 'no': ")
    if paying_now_or_future == "no":
        how_many_payed_now = float(input("Please enter the amount of units that was payed on now: "))

    for looking_for_inventory_1 in short_term_asset:
        if looking_for_inventory_1[0] == "Inventory":
            looking_for_inventory_1[1] = looking_for_inventory_1[1] + (new_inventory_amount * salary_per_unit)
            looking_for_inventory_1[2] = looking_for_inventory_1[2] - (used_inventory + new_inventory_amount)
        for looking_for_cash in short_term_asset:
            if looking_for_cash[0] == "Cash":
                if paying_now_or_future == "yes":
                    looking_for_cash[1] = looking_for_cash[1] - (new_inventory_amount * salary_per_unit)
                    cash_transaction.append(["Down",new_inventory_amount * salary_per_unit])
                elif paying_now_or_future == "no":
                    looking_for_cash[1] = looking_for_cash[1] - (how_many_payed_now * salary_per_unit)
                    short_term_liab.append(["Expenses to be payed",((new_inventory_amount * salary_per_unit) - how_many_payed_now * salary_per_unit)])
                    cash_transaction.append(["Down",(new_inventory_amount * salary_per_unit)])
                    expense_to_pay_transaction.append(["Up",(new_inventory_amount * salary_per_unit) - (how_many_payed_now * salary_per_unit)])