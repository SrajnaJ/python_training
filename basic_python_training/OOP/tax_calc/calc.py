# Base class
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        pass

    def apply_deductions(self, salary, apply_pf=True):
        tax = 0.10 * salary  # 10% tax deduction
        pf = 0.12 * salary if apply_pf else 0  # 12% PF deduction for applicable employees
        final_salary = salary - (tax + pf)
        return final_salary

    def display_info(self):
        return f"Employee: {self.name}, ID: {self.emp_id}"

# Full-time employee subclass
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        return self.apply_deductions(self.base_salary)

# Part-time employee subclass
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.apply_deductions(self.base_salary)

# Contractor employee subclass
class Contractor(Employee):
    def __init__(self, name, emp_id, contract_amount):
        super().__init__(name, emp_id, contract_amount)

    def calculate_salary(self):
        return self.apply_deductions(self.base_salary, apply_pf=False)

# Example:
rahul = FullTimeEmployee("Rohan", 101, 5000)
rohan = PartTimeEmployee("Rohan", 102, 20, 120)
sourav = Contractor("Sourav", 103, 3000)

for emp in [rahul, rohan, sourav]:
    print(f"{emp.display_info()}, Final Salary: ${emp.calculate_salary():.2f}")
