from mtgcalc import MortgageCalculator as MC

class Income:

    def __init__(self, name, income, category):
        self.name = name
        self.income = income
        self.category = category
        
class Expenses():

    def __init__(self, name, cost, category):
        self.name = name
        self.cost = cost
        self.category = category

class CashInvested:

    def __init__(self, name, cost): 
        self.name = name
        self.cost = cost

class ROICalculator:

    def __init__(self):
            self.property = {}
            self.total_invest = []
            self.expense_total = []
            self.income_total = []
            
    def main(self):

        while True:
            
            user_choice = input("Please enter: (income/expenses/invested/mortgage/roi/quit): ").lower()

            if user_choice == "income":
                name = input("Name of the type of income: ").lower()
                income = input("Income amount as a digit: ")
                category = input("Category of income: ").lower()
                self.adding_income(name, income, category)
            elif user_choice == "expenses":
                name = input("Name of the expense: ").lower()
                cost = input("Cost amount as a digit: ")
                category = input("What type of expense: ").lower()
                self.adding_expenses(name, cost, category)
            elif user_choice == "invested":
                name = input("Type of investment: ").lower()
                cost = input("Investment cost amount as a digit: ")
                self.adding_invest(name, cost)
            elif user_choice == "roi":
                self.cash_flow()
            elif user_choice == "mortgage":
                loan_amount = input("Total loan amount: ")
                loan_interest = input("Interest on loan: ") 
                length_of_loan = input("15 year or 30 year loan peroid: (15/30): ") 
                loan_PMI = input("Private Mortgage Insurence percentage if any: ") 
                mortgage_insure = input("Mortgage insurence if any: ")
                mort = MC(loan_amount, loan_interest, length_of_loan, loan_PMI, mortgage_insure)
                if mort.monthly_payments() != None:    
                    self.property[loan_amount] = mort
                    self.expense_total.append(mort.monthly_payments())
                    print(f"Your monthly mortgage payment is roughly ${mort.monthly_payments()} and has been added to your total expenses")
                    print(self.expense_total)
            elif user_choice == "quit":
                print("Have a nice day.")
                break
            else:
                print("!!Invald Input!!")
                continue

    def adding_income(self, name, income, category):
            try:
                income1 = float(income)
                if isinstance(income1, float):
                    self.income_total.append(income)
            except:
                print("Invald Input! Please enter digits only for 'income amount'.")
                return 
            inc = Income(name, income, category)
            self.property[name] = inc
            return       
            
    def adding_expenses(self, name, cost, category):           
            try:
                cost1 = float(cost)
                if isinstance(cost1, float):
                    self.expense_total.append(cost)
            except:
                print("Invald Input! Please enter digits only for 'cost amount'.")
                return            
            exp = Expenses(name, cost, category)
            self.property[name] = exp
            return

    def adding_invest(self, name, cost):
            try:
                cost1 = float(cost)
                if isinstance(cost1, float):
                    self.total_invest.append(cost)
            except:
                print("Invald Input! Please enter digits only for 'investment amount'.")
                return 
            inv = CashInvested(name, cost)
            self.property[name] = inv
            return

    def cash_flow(self):
        income = sum([float(num) for num in self.income_total])
        expenses = sum([float(expnum) for expnum in self.expense_total]) 
        cashflow_income = (income - expenses) * 12
        
        investment = sum([float(invnum) for invnum in self.total_invest])
                
        property_roi = round(((cashflow_income / investment) * 100), 2)
        
        return print(f"The ROI for this property is {property_roi}%")
        


blue_house = ROICalculator()
blue_house.main()


        