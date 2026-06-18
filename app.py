def calculate_pit_with_insurance(gross_income: float, dependents: int) -> float:
    """
    Calculate PIT including mandatory insurance deductions (10.5%).
    Base salary for insurance cap assumed at 2,340,000 VND (Max cap = 20 times base).
    """
    # 1. Calculate Mandatory Insurance (8% BHXH + 1.5% BHYT + 1% BHTN = 10.5%)
    # Note: Max income for BHXH/BHYT cap is 20 times the base salary
    base_salary = 2340000  
    insurance_cap_income = base_salary * 20
    
    if gross_income > insurance_cap_income:
        insurance = insurance_cap_income * 0.105
    else:
        insurance = gross_income * 0.105
        
    # 2. Deductions
    personal_deduction = 15500000
    dependent_deduction = 6200000
    total_deductions = personal_deduction + (dependents * dependent_deduction)
    
    # 3. Taxable Income (Thu nhập tính thuế sau khi trừ Bảo hiểm và Giảm trừ)
    taxable_income = gross_income - insurance - total_deductions
    
    if taxable_income <= 0:
        return 0.0
        
    # Progressive tax brackets
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
