

class MortgageCalculator:

    def __init__(self, loan_amount, loan_interest, length_of_loan, loan_PMI, mortgage_insure):
        self.loan_amount = loan_amount
        self.loan_interest = loan_interest
        self.length_of_loan = length_of_loan
        self.loan_PMI = loan_PMI
        self.mortgage_insure = mortgage_insure

    def monthly_payments(self):
        try:
            self.loan_amount = float(self.loan_amount)
            if isinstance(self.loan_amount, float):
                pass
        except:
            print("Invald Input! Please enter digits only.")
            return 
        
        try:
            self.loan_interest = float(self.loan_interest)
            if isinstance(self.loan_interest, float):
                pass
        except:
            print("Invald Input! Please enter digits only.")
            return 
        
        try:
            self.length_of_loan = float(self.length_of_loan)
            if isinstance(self.length_of_loan, float):
                pass
        except:
            print("Invald Input! Please enter digits only.")
            return 
       
        try:
            self.loan_PMI = float(self.loan_PMI)
            if isinstance(self.loan_PMI, float):
                pass
        except:
            print("Invald Input! Please enter digits only.")
            return 
        
        try:
            self.mortgage_insure = float(self.mortgage_insure)
            if isinstance(self.mortgage_insure, float):
                pass
        except:
            print("Invald Input! Please enter digits only.")
            return 
        
        mo_interest = round(((float(self.loan_interest) / 100) / 12), 3)

        mo_payments = float(self.length_of_loan) * 12
        
        convert_PMI = round((float(self.loan_PMI) / 100), 3)
        if convert_PMI != 0:
            add_PMI_to_loan = round((float(self.loan_amount) * convert_PMI + float(self.loan_amount)), 2)
        else:
            add_PMI_to_loan = float(self.loan_amount)
        
        monthly_payment1 =(add_PMI_to_loan * (mo_interest*((1.00 + mo_interest)**mo_payments))) / (((1.00 + mo_interest)**mo_payments) - 1.00) 
        monthly_payment = monthly_payment1 + float(self.mortgage_insure)
        return round((monthly_payment), 2)