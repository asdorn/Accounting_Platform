short_term_asset = []
long_term_assets = []
short_term_liab = []
long_term_liab = []
equity = []
def first_balance():
    global short_term_asset
    global long_term_assets
    global short_term_liab
    global long_term_liab
    global equity

    # ASSETS

    # SHORT TERM ASSESTS
    cash = float(input("Short term Assets\nPlease enter the amount of Cash available: "))
    short_term_asset.append(["Cash",cash])
    value_of_inventory = float(input("Please enter the Value of Inventory you own: "))
    short_term_asset.append(["Inventory", value_of_inventory,0])
    if value_of_inventory != 0:
        amount_of_inventory = float(input("Please enter the amount of Inventory you own: "))
        for searching_for_invent in short_term_asset:
            if searching_for_invent[0] == "Inventory":
                searching_for_invent[2] = amount_of_inventory
    clients_to_pay = float(input("Please enter the amount of money clients are going to pay you: "))
    short_term_asset.append(["Clients to pay", clients_to_pay])

    # LONG TERM ASSETS
    permanent_possesion = float(input("Long term Assets\nPlease enter the value of your Permanent Possesion: "))
    long_term_assets.append(["Permanent Possesion",permanent_possesion])
    bank_trust = float(input("Please enter your Bank Savings: "))
    long_term_assets.append(["Bank Trust",bank_trust])

    # IF USER HAS OTHER ASSETS, APPENDING TO LISTS BASE ON KIND OF ASSET(LONG/SHORT)
    more_assets = int(input("Please enter the number of other kind of assets you have, if none, press 0: "))
    if more_assets > 0:
        for diverticulum in range(more_assets):
            value_1 = input("Please enter if its a long term or a short term asset: ")
            value_2 = input("Please enter the name of that asset: ")
            value_3 = float(input("Please enter the value of that asset: "))
            if value_1 == "short term asset" or value_1 == "short":
                short_term_asset.append([value_2, value_3])
            if value_1 == "long term asset" or value_1 == "long":
                long_term_assets.append([value_2, value_3])

    # LIABILITIES

    # SHORT TERM LIABILITIES
    short_term_loans = float(input("Short term Liabilities\nPlease enter your Short Term Loans: "))
    short_term_liab.append(["Short term loans", short_term_loans])
    clients_to_be_payed = float(input("Please enter the amount of money you are going to pay to your clients: "))
    short_term_liab.append(["Clients to be payed", clients_to_be_payed])
    expense_to_pay = float(input("Please enter the amount of expenses to be payed to suppliers: "))
    short_term_liab.append(["Expenses to be payed",expense_to_pay])

    # LONG TERM LIABILITIES
    long_term_loans = float(input("Long term Liabilities\nPlease enter your long term loans: "))
    long_term_liab.append(["Long term loans", long_term_loans])
    bonds = float(input("Please enter the value of Bonds you owe: "))
    long_term_liab.append(["Bonds", bonds])

    # IF USER HAS OTHER LIABILITIES, APPENDING TO LISTS BASE ON KIND OF LIABILITY(LONG/SHORT)
    more_liab = int(input("Please enter the number of other kind of liabilities you have, if none, press 0: "))
    if more_liab > 0:
        for diverticulum in range(more_liab):
            value_4 = input("Please enter if its a long term or a short term liability: ")
            value_5 = input("Please enter the name of that liability: ")
            value_6 = float(input("Please enter the value of that liability: "))
            if value_4 == "short term liability" or value_4 == "short":
                short_term_liab.append([value_5, value_6])
            if value_4 == "long term liability" or value_4 == "long":
                long_term_liab.append([value_5, value_6])

    # EQUITY
    shares_value_plus_premia = float(input("Equity\nPlease enter your company share value and premia: "))
    equity.append(["Shares and Premia", shares_value_plus_premia])
    surpluses = float(input("Please enter the amount of surpluses that you have: "))
    equity.append(["Surpluses", surpluses])

    # IF USER HAS MORE KINDS OF EQUITY,APPENDING TO EQUITY LIST
    more_equity = int(input("Please enter the number of other kind of equities that you have, if none, press 0: "))
    if more_equity > 0:
        for diverticulum in range(more_equity):
            value_7 = input("Please enter the name of that equity: ")
            value_8 = float(input("Please enter the value of that equity: "))
            equity.append([value_7, value_8])
    return (short_term_asset,long_term_assets,short_term_liab,long_term_liab,equity)

# FUNCTIONS FOR THE SOURCE CODE
def user_choice():
    while True:
        user_input = float(input())
        if user_input == 0:
            break
        elif user_input == 1:
            buying_inventory()
        elif user_input == 2:
            selling_inventory()
        elif user_input == 3:
            inventory_to_inventory()
        elif user_input == 4:
            taking_a_loan()
        elif user_input == 5:
            returning_a_loan()
        elif user_input == 6:
            returning_expenses_to_pay()
        elif user_input == 7:
            value_of_issue = issue()
        elif user_input == 8:
            buying_permanent_possesion()
        elif user_input == 9:
            selling_permanent_possesion()
        elif user_input == 10:
            paying_ahead()
        elif user_input == 11:
            clients_paying_you()

# OTHER VARIABLES FOR REPORTS
total_sales = 0
sales_cost = 0
other_payments = 0
dividend = 0

def profit_loss():
    global total_sales
    global sales_cost
    global other_payments
    global tax_rate
    print("\n\nProfit and Loss Report:")
    print("Revenue:\t",total_sales)
    print("Expense on Revenue:\t",sales_cost)
    print("Gross Profit:\t",(total_sales - sales_cost))
    print("Operating Expenses:\t",other_payments)
    print("Operating and Net Profit:\t",(total_sales - sales_cost - other_payments))
    return (total_sales - sales_cost - other_payments)

def dividends_distribution():
    global dividend
    dividend = float(input("\nHow much Dividends Did you distributed to your Share Holders?"))
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] - dividend
    for looking_for_surpluses in equity:
        if looking_for_surpluses[0] == "Surpluses":
            looking_for_surpluses[1] = looking_for_surpluses[1] - dividend
    return dividend

# LISTS TO HOLD RECORD OF TRANSACTIONS
cash_transaction = []
inventory_transaction = []
permanent_possesion_transaction = []
short_loan_transaction = []
long_loan_transaction = []
shares_and_premia_transaction = []
surpluses_transaction = []
sales_transaction = []
sales_cost_transaction = []
other_payments_transaction = []
clients_to_pay_transaction = []
expense_to_pay_transaction = []

def transactions():
    print("Assets")
    if len(cash_transaction) > 0:
        print("Cash\t",cash_transaction)
    if len(inventory_transaction) > 0:
        print("Stock\t",inventory_transaction)
    if len(clients_to_pay_transaction) > 0:
        print("Clients to pay\t",clients_to_pay_transaction)
    if len(permanent_possesion_transaction) > 0:
        print("Permanent Possesion\t",permanent_possesion_transaction)
    print("\nLiabilities")
    if len(short_loan_transaction) > 0:
        print("Short term loan\t",short_loan_transaction)
    if len(long_loan_transaction) > 0:
        print("Long term loan\t",long_loan_transaction)
    if len(expense_to_pay_transaction) > 0:
        print("Expense to be payed\t",expense_to_pay_transaction)
    print("\nEquity")
    if len(shares_and_premia_transaction) > 0:
        print("Shares and Premia\t",shares_and_premia_transaction)
    if len(surpluses_transaction) > 0:
        print("Surpluses\t",surpluses_transaction)
    print("\nProfit and Loss")
    if len(sales_transaction) > 0:
        print("Sales\t",sales_transaction)
    if len(sales_cost_transaction) > 0:
        print("Sales cost\t",sales_cost_transaction)
    if len(other_payments_transaction) > 0:
        print("Other payments\t",other_payments_transaction)

def buying_inventory():
    global inventory_transaction
    global cash_transaction
    value_of_inventory = float(input("Please enter the value of Inventory that was bought: "))
    amount_of_inventory = float(input("Please enter the amount of the Inventory was bought: "))
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] - value_of_inventory
    for looking_for_inventory in short_term_asset:
        if looking_for_inventory[0] == "Inventory":
            looking_for_inventory[1] = looking_for_inventory[1] + value_of_inventory
            looking_for_inventory[2] = looking_for_inventory[2] + amount_of_inventory
    cash_transaction.append(["Down", value_of_inventory])
    inventory_transaction.append(["Up",value_of_inventory,amount_of_inventory])

def selling_inventory():
    global total_sales
    global sales_cost
    global inventory_transaction
    global cash_transaction
    global surpluses_transaction
    global sales_transaction
    global sales_cost_transaction
    global clients_to_pay_transaction
    last_inventory_buy_value = 1
    last_inventory_buy_amount = 1

    amount_of_inventory = float(input("Please enter the amount of Inventory that was sold: "))
    price_of_sell = float(input("Please enter the price per unit that was sold: "))
    will_clients_pay_now = input("Will you be payed in full now? enter 'yes' or 'no': ")
    if will_clients_pay_now == "no":
        paying_later = float(input("Please enter the amount of inventory units that you will be payed on later: "))
    else:
        paying_later = 0

    for looking_for_inventory in short_term_asset:
        if looking_for_inventory[0] == "Inventory":
            if looking_for_inventory[1] != None:
                value_of_inventory = ((amount_of_inventory / looking_for_inventory[2]) * looking_for_inventory[1])
    for number_of_cycles in range(1,len(inventory_transaction) + 1):
        if len(inventory_transaction) > 0:
            if inventory_transaction[len(inventory_transaction) - number_of_cycles][0] == "Up":
                last_inventory_buy_value = inventory_transaction[len(inventory_transaction) - number_of_cycles][1]
                last_inventory_buy_amount = inventory_transaction[len(inventory_transaction) - number_of_cycles][2]
                break
    if last_inventory_buy_value > 1 and last_inventory_buy_amount > 1:
        value_of_inventory = ((amount_of_inventory / last_inventory_buy_amount) * last_inventory_buy_value)
    sale_price = amount_of_inventory * price_of_sell

    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            if paying_later > 0:
                looking_for_cash[1] = looking_for_cash[1] + sale_price - (paying_later * price_of_sell)
            else:
                looking_for_cash[1] = looking_for_cash[1] + sale_price
    if paying_later > 0:
        for looking_for_clients in short_term_asset:
            if looking_for_clients[0] == "Clients to pay":
                looking_for_clients[1] = looking_for_clients[1] + (paying_later * price_of_sell)
    for looking_for_stock in short_term_asset:
        if looking_for_stock[0] == "Inventory":
            looking_for_stock[1] = looking_for_stock[1] - value_of_inventory
    for looking_for_surpluses in equity:
        if looking_for_surpluses[0] == "Surpluses":
            looking_for_surpluses[1] = looking_for_surpluses[1] + sale_price
    for looking_for_surpluses_2 in equity:
        if looking_for_surpluses_2[0] == "Surpluses":
            looking_for_surpluses_2[1] = looking_for_surpluses_2[1] - value_of_inventory

    cash_transaction.append(["Up", sale_price - (paying_later * price_of_sell)])
    inventory_transaction.append(["Down", value_of_inventory,amount_of_inventory])
    surpluses_transaction.append(["Up",(sale_price)])
    surpluses_transaction.append(["Down",value_of_inventory])
    sales_cost_transaction.append(["Up",value_of_inventory])
    sales_transaction.append(["Up",sale_price])
    if paying_later > 0:
        clients_to_pay_transaction.append(["Up", (paying_later * price_of_sell)])
    total_sales += sale_price
    sales_cost += value_of_inventory

def taking_a_loan():
    global cash_transaction
    global short_loan_transaction
    global long_loan_transaction

    value_of_loan = float(input("Please enter the value of loan that you took: "))
    long_or_short = input("Please enter if it was a 'long' term or 'short' term loan: ")

    if long_or_short == "short":
        for looking_for_short_loan in short_term_liab:
            if looking_for_short_loan[0] == "Short term loans":
                looking_for_short_loan[1] = looking_for_short_loan[1] + value_of_loan
        short_loan_transaction.append(["Up",value_of_loan])
    if long_or_short == "long":
        for looking_for_long_loan in long_term_liab:
            if looking_for_long_loan[0] == "Long term loans":
                looking_for_long_loan[1] = looking_for_long_loan[1] + value_of_loan
        long_loan_transaction.append(["Up",value_of_loan])
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] + value_of_loan

    cash_transaction.append(["Up",value_of_loan])

def returning_a_loan():
    global cash_transaction
    global short_loan_transaction

    value_of_loan = float(input("Please enter the value of loan that you are returning: "))

    for looking_for_short_loan in short_term_liab:
        if looking_for_short_loan[0] == "Short term loans":
            looking_for_short_loan[1] = looking_for_short_loan[1] - value_of_loan
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] - value_of_loan

    cash_transaction.append(["Down",value_of_loan])
    short_loan_transaction.append(["Down",value_of_loan])

def issue():
    global cash_transaction
    global shares_and_premia_transaction

    value_of_issue = float(input("Please enter the value of the issue: "))

    for looking_for_shares in equity:
        if looking_for_shares[0] == "Shares and Premia":
            looking_for_shares[1] = looking_for_shares[1] + value_of_issue
    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] + value_of_issue

    cash_transaction.append(["Up",value_of_issue])
    shares_and_premia_transaction.append(["Up",value_of_issue])
    return value_of_issue

def buying_permanent_possesion():
    global cash_transaction
    global permanent_possesion_transaction

    possesion_value = float(input("Please enter the value of the permanent possesion that you bought: "))

    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] - possesion_value
    for looking_for_permanent_possesion in long_term_assets:
        if looking_for_permanent_possesion[0] == "Permanent Possesion":
            looking_for_permanent_possesion[1] = looking_for_permanent_possesion[1] + possesion_value

    cash_transaction.append(["Down",possesion_value])
    permanent_possesion_transaction.append(["Up",possesion_value])

def selling_permanent_possesion():
    global cash_transaction
    global permanent_possesion_transaction

    possesion_value = float(input("Please enter the value of the permanent possesion that you sold: "))

    for looking_for_cash in short_term_asset:
        if looking_for_cash[0] == "Cash":
            looking_for_cash[1] = looking_for_cash[1] + possesion_value
    for looking_for_permanent_possesion in long_term_assets:
        if looking_for_permanent_possesion[0] == "Permanent Possesion":
            looking_for_permanent_possesion[1] = looking_for_permanent_possesion[1] - possesion_value

    cash_transaction.append(["Up",possesion_value])
    permanent_possesion_transaction.append(["Down",possesion_value])

def paying_ahead():
    global cash_transaction
    global other_payments
    global other_payments_transaction
    global surpluses_transaction

    value_of_payment = float(input("Please enter the value of the payment: "))
    name_of_payment = input("Please enter how you wish this payment will be called in the assets: ")
    which_quarter = float(input("Please enter in which quarter you made the payment: "))
    num_of_payments = float(input("Please enter the number of payment you are going to pay (per quarter): "))
    short_term_asset.append([name_of_payment, value_of_payment])

    if ((4 - which_quarter)/ num_of_payments > 1 or ((4 - which_quarter) / num_of_payments == 1)):
        other_payments = other_payments + value_of_payment
        for looking_for_name_of_payment in short_term_asset:
            if looking_for_name_of_payment[0] == name_of_payment:
                short_term_asset.remove(looking_for_name_of_payment)
        for looking_for_cash in short_term_asset:
            if looking_for_cash[0] == "Cash":
                looking_for_cash[1] = looking_for_cash[1] - value_of_payment
        for looking_for_surpluses in equity:
            if looking_for_surpluses[0] == "Surpluses":
                looking_for_surpluses[1] = looking_for_surpluses[1] - value_of_payment
        other_payments_transaction.append([name_of_payment,"Up",value_of_payment])
        surpluses_transaction.append(["Down",value_of_payment])
    if ((4 - which_quarter) / num_of_payments < 1):
        other_payments = other_payments + (value_of_payment * ((4 - which_quarter)) / num_of_payments)
        for looking_for_name_of_payment in short_term_asset:
            if looking_for_name_of_payment[0] == name_of_payment:
                looking_for_name_of_payment[1] = looking_for_name_of_payment[1] * ((4 - which_quarter) / num_of_payments)
        for looking_for_cash in short_term_asset:
            if looking_for_cash[0] == "Cash":
                looking_for_cash[1] = looking_for_cash[1] - value_of_payment
        for looking_for_surpluses in equity:
            if looking_for_surpluses[0] == "Surpluses":
                looking_for_surpluses[1] = looking_for_surpluses[1] - (value_of_payment * ((4 - which_quarter)) / num_of_payments)

        other_payments_transaction.append([name_of_payment,"Up",value_of_payment,"Value payed this year: ",(value_of_payment * ((4 - which_quarter)) / num_of_payments)])
        surpluses_transaction.append(["Down",(value_of_payment * ((4 - which_quarter) / num_of_payments))])
    cash_transaction.append(["Down",value_of_payment])

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

def clients_paying_you():
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
            looking_for_cash[1] = looking_for_cash[1] + how_much_to_return
    for looking_for_expenses_to_be_payed in short_term_liab:
        if looking_for_expenses_to_be_payed[0] == "Expenses to be payed":
            looking_for_expenses_to_be_payed[1] = looking_for_expenses_to_be_payed[1] - how_much_to_return

    cash_transaction.append(["Up",how_much_to_return])
    expense_to_pay_transaction.append(["Down",how_much_to_return])

def inventory_to_inventory():
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