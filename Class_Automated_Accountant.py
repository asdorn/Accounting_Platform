class Automated_Accountant():
    def __init__(self):
        self.short_term_asset = []
        self.long_term_assets = []
        self.short_term_liab = []
        self.long_term_liab = []
        self.equity = []

    def first_balance(self):
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