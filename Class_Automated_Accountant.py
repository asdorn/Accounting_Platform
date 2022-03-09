class Automated_Accountant():
    def __init__(self):
        self.short_term_asset = []
        self.long_term_assets = []
        self.short_term_liab = []
        self.long_term_liab = []
        self.equity = []

    def first_balance():
        global short_term_asset
        global long_term_assets
        global short_term_liab
        global long_term_liab
        global equity

        # ASSETS

        # SHORT TERM ASSESTS
        cash = float(input("Short term Assets\nPlease enter the amount of Cash available: "))
        short_term_asset.append(["Cash", cash])
        value_of_inventory = float(input("Please enter the Value of Inventory you own: "))
        short_term_asset.append(["Inventory", value_of_inventory, 0])
        if value_of_inventory != 0:
            amount_of_inventory = float(input("Please enter the amount of Inventory you own: "))
            for searching_for_invent in short_term_asset:
                if searching_for_invent[0] == "Inventory":
                    searching_for_invent[2] = amount_of_inventory
        clients_to_pay = float(input("Please enter the amount of money clients are going to pay you: "))
        short_term_asset.append(["Clients to pay", clients_to_pay])

        # LONG TERM ASSETS
        permanent_possesion = float(input("Long term Assets\nPlease enter the value of your Permanent Possesion: "))
        long_term_assets.append(["Permanent Possesion", permanent_possesion])
        bank_trust = float(input("Please enter your Bank Savings: "))
        long_term_assets.append(["Bank Trust", bank_trust])

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
        short_term_liab.append(["Expenses to be payed", expense_to_pay])

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
        return (short_term_asset, long_term_assets, short_term_liab, long_term_liab, equity)