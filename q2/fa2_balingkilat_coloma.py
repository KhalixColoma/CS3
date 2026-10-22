class Patient:
    def __init__(self,name,bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self) :
        return self.name

    def set_name(self,name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount > 0:
            self.bill_amount = bill_amount
        else:
            print("Bill amount must be positive")

    def calculate_bill(self):
        return self.bill_amount


class Senior_Patient(Patient):
    def __init__(self,name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealth_Patient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85



patient = Patient("Juan Dela Cruz", 15000.0)
seniorpatient = Senior_Patient("Maria Santos", 15000.0)
phpatient = PhilHealth_Patient("Pedro Reyes", 15000.0)

print("Hospital Billing System")
print("-----------------------\n\n")
print(f"Regular Patient: {patient.get_name()}")
print(f"Original Bill: ₱{patient.get_bill_amount()}")
print(f"Final Bill: ₱{patient.calculate_bill():.2f}\n")
print(f"Senior Patient: {seniorpatient.get_name()}")
print(f"Original Bill: ₱{seniorpatient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{seniorpatient.calculate_bill():.2f}\n")
print(f"PhilHealth Patient: {phpatient.get_name()}")
print(f"Original Bill: ₱{phpatient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{phpatient.calculate_bill():.2f}\n")
