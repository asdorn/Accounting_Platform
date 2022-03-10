class Automated_Accountant():
    def __init__(self):
        self.short_term_asset = []
        self.long_term_assets = []
        self.short_term_liab = []
        self.long_term_liab = []
        self.equity = []
        self.total_sales = 0
        self.sales_cost = 0
        self.other_payments = 0
        self.dividend = 0
        self.cash_transaction = []
        self.inventory_transaction = []
        self.permanent_possesion_transaction = []
        self.short_loan_transaction = []
        self.long_loan_transaction = []
        self.shares_and_premia_transaction = []
        self.surpluses_transaction = []
        self.sales_transaction = []
        self.sales_cost_transaction = []
        self.other_payments_transaction = []
        self.clients_to_pay_transaction = []
        self.expense_to_pay_transaction = []

    def create_balance(self):
        # ASSETS

        # SHORT TERM ASSESTS
        print("Short Term Assets")
        while True:
            try:
                cash = float(input("Please enter the amount of Cash available: "))
            except ValueError:
                print("Please enter a valid amount of Cash")
                continue
            else:
                break
            self.short_term_asset.append(["Cash", cash])
            self.cash = cash
        while True:
            try:
                value_of_inventory = float(input("Please enter the Value of Inventory you own: "))
            except ValueError:
                print("Please enter a valid value of Inventory")
                continue
            else:
                break
            self.inventory_value = value_of_inventory
            self.short_term_asset.append(["Inventory", value_of_inventory, 0])
            if value_of_inventory != 0:
                while True:
                    try:
                        amount_of_inventory = float(input("Please enter the amount of Inventory you own: "))
                    except ValueError:
                        print("Please enter a valid amount of Inventory")
                        continue
                    else:
                        break
                for searching_for_invent in short_term_asset:
                    if searching_for_invent[0] == "Inventory":
                        self.inventory_amount = amount_of_inventory
                        searching_for_invent[2] = amount_of_inventory
            while True:
                try:
                    clients_to_pay = float(input("Please enter the amount of money clients are going to pay you: "))
                except ValueError:
                    print("Please enter a valid amount")
                    continue
                else:
                    break
            self.clients_to_pay = clients_to_pay
            self.short_term_asset.append(["Clients to pay", clients_to_pay])


        # LONG TERM ASSETS
        print("Long Term Assets")
        while True:
            try:
                permanent_possesion = float(input("Please enter the value of your Permanent Possesion: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.permanent_possesion = permanent_possesion
        self.long_term_assets.append(["Permanent Possesion", permanent_possesion])
        while True:
            try:
                bank_trust = float(input("Please enter your Bank Savings: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.bank_trust = bank_trust
        self.long_term_assets.append(["Bank Trust", bank_trust])

        # IF USER HAS OTHER ASSETS, APPENDING TO LISTS BASE ON KIND OF ASSET(LONG/SHORT)
        while True:
            try:
                more_assets = int(input("Please enter the number of other kind of assets you have, if none, press 0: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            if more_assets >= 2:
                Yes_or_No = str(input("Are you sure you would want to add that amount of assets? "))
                if Yes_or_No == "No":
                    continue
                if Yes_or_No == "Yes":
                    break
                else:
                    print("Please enter 'Yes' or 'No' after entering number of assets again")
                    continue
        if more_assets > 0:
            self.added_assets = []
            for diverticulum in range(more_assets):
                while True:
                    try:
                        value_1 = input("Please enter if its a long term or a short term asset: ")
                    except ValueError:
                        print("Please enter 'short' or 'long'")
                        continue
                    else:
                        break
                value_2 = str(input("Please enter the name of that asset: "))
                while True:
                    try:
                        value_3 = float(input("Please enter the value of that asset: "))
                    except ValueError:
                        print("Please enter a valid value")
                        continue
                    else:
                        break
                if value_1 == "short term asset" or value_1 == "short":
                    self.short_term_asset.append([value_2, value_3])
                if value_1 == "long term asset" or value_1 == "long":
                    self.long_term_assets.append([value_2, value_3])
                self.added_assets.append([value_1,value_2,value_3])

        # LIABILITIES

        # SHORT TERM LIABILITIES
        print("Short term Liabilities")
        while True:
            try:
                short_term_loans = float(input("Please enter your Short Term Loans: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.short_term_loan = short_term_loans
        self.short_term_liab.append(["Short term loans", short_term_loans])
        while True:
            try:
                clients_to_be_payed = float(input("Please enter the amount of money you are going to pay to your clients: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            else:
                break
        self.client_to_be_payed = clients_to_be_payed
        self.short_term_liab.append(["Clients to be payed", clients_to_be_payed])
        while True:
            try:
                expense_to_pay = float(input("Please enter the amount of expenses to be payed to suppliers: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            else:
                break
        self.expense_to_pay = expense_to_pay
        self.short_term_liab.append(["Expenses to be payed", expense_to_pay])

        # LONG TERM LIABILITIES
        print("Long term Liabilities")
        while True:
            try:
                long_term_loans = float(input("Please enter your long term loans: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.long_term_loans = long_term_loans
        self.long_term_liab.append(["Long term loans", long_term_loans])
        while True:
            try:
                bonds = float(input("Please enter the value of Bonds you owe: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.bonds = bonds
        self.long_term_liab.append(["Bonds", bonds])

        # IF USER HAS OTHER LIABILITIES, APPENDING TO LISTS BASE ON KIND OF LIABILITY(LONG/SHORT)
        while True:
            try:
                more_liab = int(input("Please enter the number of other kind of liabilities you have, if none, press 0: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            if more_liab >= 2:
                Yes_or_No = str(input("Are you sure you would want to add that amount of liabilities? "))
                if Yes_or_No == "No":
                    continue
                if Yes_or_No == "Yes":
                    break
                else:
                    print("Please enter 'Yes' or 'No' after entering number of liabilities again")
                    continue
        if more_liab > 0:
            self.added_liab = []
            for diverticulum_2 in range(more_liab):
                while True:
                    try:
                        value_4 = input("Please enter if its a long term or a short term liability: ")
                    except ValueError:
                        print("Please enter 'short' or 'long'")
                        continue
                    else:
                        break
                value_5 = str(input("Please enter the name of that liability: "))
                while True:
                    try:
                        value_6 = float(input("Please enter the value of that liability: "))
                    except ValueError:
                        print("Please enter a valid value")
                        continue
                    else:
                        break
                if value_4 == "short term liability" or value_4 == "short":
                    self.short_term_liab.append([value_5, value_6])
                if value_4 == "long term asset" or value_4 == "long":
                    self.long_term_liab.append([value_5, value_6])
                self.added_liab.append([value_4,value_5,value_6])

        # EQUITY
        print("Equity")
        while True:
            try:
                shares_value_plus_premia = float(input("Please enter your company share value and premia: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.shares_and_premia = shares_value_plus_premia
        self.equity.append(["Shares and Premia", shares_value_plus_premia])
        while True:
            try:
                surpluses = float(input("Please enter the amount of surpluses that you have: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            else:
                break
        self.surpluses = surpluses
        self.equity.append(["Surpluses", surpluses])

        # IF USER HAS MORE KINDS OF EQUITY,APPENDING TO EQUITY LIST
        while True:
            try:
                more_equity = int(input("Please enter the number of other kind of equities that you have, if none, press 0: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            if more_equity >= 2:
                Yes_or_No = str(input("Are you sure you would want to add that amount of equities? "))
                if Yes_or_No == "No":
                    continue
                if Yes_or_No == "Yes":
                    break
                else:
                    print("Please enter 'Yes' or 'No' after entering number of equities again")
                    continue
        if more_equity > 0:
            self.added_equity = []
            for diverticulum_3 in range(more_equity):
                value_7 = str(input("Please enter the name of that equity: "))
                while True:
                    try:
                        value_8 = float(input("Please enter the value of that equity: "))
                    except ValueError:
                        print("Please enter a valid value")
                        continue
                    else:
                        break
                self.added_equity.append([value_7, value_8])
                self.equity.append([value_7, value_8])

    def profit_loss(self):
        print("Profit and Loss Report:")
        print("Revenue:\t", self.total_sales)
        self.revenue = self.total_sales
        print("Expense on Revenue:\t", self.sales_cost)
        self.expense_on_revenue = self.sales_cost
        print("Gross Profit:\t", (self.total_sales - self.sales_cost))
        self.gross_profit = self.total_sales - self.sales_cost
        print("Operating Expenses:\t", self.other_payments)
        self.operating_expenses = self.other_payments
        print("Operating and Net Profit:\t", (self.total_sales - self.sales_cost - self.other_payments))
        self.operating_and_net_profit = self.total_sales - self.sales_cost - self.other_payments
        return (self.total_sales - self.sales_cost - self.other_payments)

    def dividends_distribution(self):
        self.dividend = float(input("How much Dividends Did you distributed to your Share Holders?"))
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash -= self.dividend
                looking_for_cash[1] = looking_for_cash[1] - self.dividend
        for looking_for_surpluses in self.equity:
            if looking_for_surpluses[0] == "Surpluses":
                self.surpluses -= self.dividend
                looking_for_surpluses[1] = looking_for_surpluses[1] - self.dividend
        return self.dividend

    def transactions(self):
        print("Assets")
        if len(self.cash_transaction) > 0:
            print("Cash\t", self.cash_transaction)
        if len(self.inventory_transaction) > 0:
            print("Stock\t", self.inventory_transaction)
        if len(self.clients_to_pay_transaction) > 0:
            print("Clients to pay\t", self.clients_to_pay_transaction)
        if len(self.permanent_possesion_transaction) > 0:
            print("Permanent Possesion\t", self.permanent_possesion_transaction)
        print("\nLiabilities")
        if len(self.short_loan_transaction) > 0:
            print("Short term loan\t", self.short_loan_transaction)
        if len(self.long_loan_transaction) > 0:
            print("Long term loan\t", self.long_loan_transaction)
        if len(self.expense_to_pay_transaction) > 0:
            print("Expense to be payed\t", self.expense_to_pay_transaction)
        print("\nEquity")
        if len(self.shares_and_premia_transaction) > 0:
            print("Shares and Premia\t", self.shares_and_premia_transaction)
        if len(self.surpluses_transaction) > 0:
            print("Surpluses\t", self.surpluses_transaction)
        print("\nProfit and Loss")
        if len(self.sales_transaction) > 0:
            print("Sales\t", self.sales_transaction)
        if len(self.sales_cost_transaction) > 0:
            print("Sales cost\t", self.sales_cost_transaction)
        if len(self.other_payments_transaction) > 0:
            print("Other payments\t", self.other_payments_transaction)

    def buying_inventory(self):
        while True:
            try:
                value_of_inventory = float(input("Please enter the value of Inventory that was bought: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        self.value_of_bought_inventory = value_of_inventory
        while True:
            try:
                amount_of_inventory = float(input("Please enter the amount of the Inventory was bought: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            else:
                break
        self.amount_of_bought_inventort = amount_of_inventory
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash -= value_of_inventory
                looking_for_cash[1] = looking_for_cash[1] - value_of_inventory
        for looking_for_inventory in self.short_term_asset:
            if looking_for_inventory[0] == "Inventory":
                self.inventory_value += value_of_inventory
                looking_for_inventory[1] = looking_for_inventory[1] + value_of_inventory
                self.inventory_amount += amount_of_inventory
                looking_for_inventory[2] = looking_for_inventory[2] + amount_of_inventory
        self.cash_transaction.append(["Down", value_of_inventory])
        self.inventory_transaction.append(["Up", value_of_inventory, amount_of_inventory])

    def selling_inventory(self):
        last_inventory_buy_value = 1
        last_inventory_buy_amount = 1
        while True:
            try:
                amount_of_inventory = float(input("Please enter the amount of Inventory that was sold: "))
            except ValueError:
                print("Please enter a valid amount")
                continue
            else:
                break
        while True:
            try:
                price_of_sell = float(input("Please enter the price per unit that was sold: "))
            except ValueError:
                print("Please enter a valid price")
                continue
            else:
                break
        while True:
            will_clients_pay_now = str(input("Will you be payed in full now? enter 'Yes' or 'No': "))
            if will_clients_pay_now == "No":
                break
            if will_clients_pay_now == "Yes":
                break
            else:
                print("Please enter 'Yes' or 'No'")
                continue
        if will_clients_pay_now == "No":
            while True:
                try:
                    paying_later = float(input("Please enter the amount of inventory units that you will be payed on later: "))
                except ValueError:
                    print("Please enter a valid amount")
                    continue
                else:
                    break
        else:
            paying_later = 0

        for looking_for_inventory in self.short_term_asset:
            if looking_for_inventory[0] == "Inventory":
                if looking_for_inventory[1] != None:
                    self.inventory_value = ((amount_of_inventory / looking_for_inventory[2]) * looking_for_inventory[1])
                    value_of_inventory = ((amount_of_inventory / looking_for_inventory[2]) * looking_for_inventory[1])
        for number_of_cycles in range(1, len(self.inventory_transaction) + 1):
            if len(self.inventory_transaction) > 0:
                if self.inventory_transaction[len(self.inventory_transaction) - number_of_cycles][0] == "Up":
                    last_inventory_buy_value = self.inventory_transaction[len(self.inventory_transaction) - number_of_cycles][1]
                    last_inventory_buy_amount = self.inventory_transaction[len(self.inventory_transaction) - number_of_cycles][2]
                    break
        if last_inventory_buy_value > 1 and last_inventory_buy_amount > 1:
            self.inventory_value = ((amount_of_inventory / last_inventory_buy_amount) * last_inventory_buy_value)
            value_of_inventory = ((amount_of_inventory / last_inventory_buy_amount) * last_inventory_buy_value)
        sale_price = amount_of_inventory * price_of_sell

        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                if paying_later > 0:
                    self.cash = self.cash + sale_price - (paying_later * price_of_sell)
                    looking_for_cash[1] = looking_for_cash[1] + sale_price - (paying_later * price_of_sell)
                else:
                    self.cash += sale_price
                    looking_for_cash[1] = looking_for_cash[1] + sale_price
        if paying_later > 0:
            for looking_for_clients in self.short_term_asset:
                if looking_for_clients[0] == "Clients to pay":
                    self.clients_to_pay += (paying_later * price_of_sell)
                    looking_for_clients[1] = looking_for_clients[1] + (paying_later * price_of_sell)
        for looking_for_stock in self.short_term_asset:
            if looking_for_stock[0] == "Inventory":
                self.inventory_value -= value_of_inventory
                looking_for_stock[1] = looking_for_stock[1] - value_of_inventory
        for looking_for_surpluses in self.equity:
            if looking_for_surpluses[0] == "Surpluses":
                self.surpluses += sale_price
                looking_for_surpluses[1] = looking_for_surpluses[1] + sale_price
        for looking_for_surpluses_2 in self.equity:
            if looking_for_surpluses_2[0] == "Surpluses":
                self.surpluses -= value_of_inventory
                looking_for_surpluses_2[1] = looking_for_surpluses_2[1] - value_of_inventory

        self.cash_transaction.append(["Up", sale_price - (paying_later * price_of_sell)])
        self.inventory_transaction.append(["Down", value_of_inventory, amount_of_inventory])
        self.surpluses_transaction.append(["Up", (sale_price)])
        self.surpluses_transaction.append(["Down", value_of_inventory])
        self.sales_cost_transaction.append(["Up", value_of_inventory])
        self.sales_transaction.append(["Up", sale_price])
        if paying_later > 0:
            self.clients_to_pay_transaction.append(["Up", (paying_later * price_of_sell)])
        self.total_sales += sale_price
        self.sales_cost += value_of_inventory

    def take_a_loan(self):
        while True:
            try:
                value_of_loan = float(input("Please enter the value of loan that you took: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        while True:
            long_or_short = input("Please enter if it was a 'long' term or 'short' term loan: ")
            if long_or_short == "short":
                break
            elif long_or_short == "long":
                break
            else:
                continue
        if long_or_short == "short":
            for looking_for_short_loan in self.short_term_liab:
                if looking_for_short_loan[0] == "Short term loans":
                    self.short_term_loan += value_of_loan
                    looking_for_short_loan[1] = looking_for_short_loan[1] + value_of_loan
            self.short_loan_transaction.append(["Up", value_of_loan])
        if long_or_short == "long":
            for looking_for_long_loan in self.long_term_liab:
                if looking_for_long_loan[0] == "Long term loans":
                    self.long_term_loans += value_of_loan
                    looking_for_long_loan[1] = looking_for_long_loan[1] + value_of_loan
            self.long_loan_transaction.append(["Up", value_of_loan])
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash += value_of_loan
                looking_for_cash[1] = looking_for_cash[1] + value_of_loan
        self.cash_transaction.append(["Up", value_of_loan])

    def returning_a_loan(self):
        while True:
            try:
                value_of_loan = float(input("Please enter the value of loan that you are returning: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        for looking_for_short_loan in self.short_term_liab:
            if looking_for_short_loan[0] == "Short term loans":
                self.short_term_loan -= value_of_loan
                looking_for_short_loan[1] = looking_for_short_loan[1] - value_of_loan
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash -= value_of_loan
                looking_for_cash[1] = looking_for_cash[1] - value_of_loan

        self.cash_transaction.append(["Down", value_of_loan])
        self.short_loan_transaction.append(["Down", value_of_loan])

    def issue(self):
        while True:
            try:
                value_of_issue = float(input("Please enter the value of the issue: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        for looking_for_shares in self.equity:
            if looking_for_shares[0] == "Shares and Premia":
                self.shares_and_premia += value_of_issue
                looking_for_shares[1] = looking_for_shares[1] + value_of_issue
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash += value_of_issue
                looking_for_cash[1] = looking_for_cash[1] + value_of_issue

        self.cash_transaction.append(["Up",value_of_issue])
        self.shares_and_premia_transaction.append(["Up",value_of_issue])
        return value_of_issue

    def buying_permanent_possesion(self):
        while True:
            try:
                possesion_value = float(input("Please enter the value of the permanent possesion that you bought: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash -= possesion_value
                looking_for_cash[1] = looking_for_cash[1] - possesion_value
        for looking_for_permanent_possesion in self.long_term_assets:
            if looking_for_permanent_possesion[0] == "Permanent Possesion":
                self.permanent_possesion += possesion_value
                looking_for_permanent_possesion[1] = looking_for_permanent_possesion[1] + possesion_value

        self.cash_transaction.append(["Down", possesion_value])
        self.permanent_possesion_transaction.append(["Up", possesion_value])

    def selling_permanent_possesion(self):
        while True:
            try:
                possesion_value = float(input("Please enter the value of the permanent possesion that you sold: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            else:
                break
        for looking_for_cash in self.short_term_asset:
            if looking_for_cash[0] == "Cash":
                self.cash += possesion_value
                looking_for_cash[1] = looking_for_cash[1] + possesion_value
        for looking_for_permanent_possesion in self.long_term_assets:
            if looking_for_permanent_possesion[0] == "Permanent Possesion":
                self.permanent_possesion -= possesion_value
                looking_for_permanent_possesion[1] = looking_for_permanent_possesion[1] - possesion_value

        self.cash_transaction.append(["Up", possesion_value])
        self.permanent_possesion_transaction.append(["Down", possesion_value])

