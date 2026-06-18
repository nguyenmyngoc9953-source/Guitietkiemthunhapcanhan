def calculate_pit(gross_income: float, dependents: int) -> float:
    """
    Calculate Personal Income Tax (PIT) based on Vietnam General Tax Regulations.
    - Personal deduction: 15,500,000 VND
    - Dependent deduction: 6,200,000 VND per person
    """
    personal_deduction = 15500000
    dependent_deduction = 6200000
    
    # Calculate total deductions and taxable income
    total_deductions = personal_deduction + (dependents * dependent_deduction)
    taxable_income = gross_income - total_deductions
    
    # Non-taxable if taxable income is zero or negative
    if taxable_income <= 0:
        return 0.0
        
    # 5-level progressive tax bracket matrix
    if taxable_income <= 10000000:
        return taxable_income * 0.05
    elif taxable_income <= 30000000:
        return (taxable_income * 0.10) - 500000
    elif taxable_income <= 60000000:
        return (taxable_income * 0.20) - 3500000
    elif taxable_income <= 100000000:
        return (taxable_income * 0.30) - 9500000
    else:
        return (taxable_income * 0.35) - 14500000

# Example Execution
if __name__ == "__main__":
    sample_gross = 40000000
    sample_dependents = 1
    tax_owed = calculate_pit(sample_gross, sample_dependents)
    
    # Format output using international standard commas for thousands
    print(f"Gross Income : {sample_gross:,.0f} VND")
    print(f"Dependents   : {sample_dependents}")
    print(f"PIT Owed     : {tax_owed:,.0f} VND")
