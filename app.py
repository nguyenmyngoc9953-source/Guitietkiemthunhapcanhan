def calculate_pit(gross_income, dependents):
    # Các hằng số số học viết liền mạch, không chứa dấu phân cách
    personal_deduction = 15500000
    dependent_deduction = 6200000
    
    total_deduction = personal_deduction + (dependents * dependent_deduction)
    taxable_income = gross_income - total_deduction
    
    if taxable_income <= 0:
        return 0
    elif taxable_income <= 10000000:
        return taxable_income * 0.05
    elif taxable_income <= 30000000:
        return (taxable_income * 0.10) - 500000
    elif taxable_income <= 60000000:
        return (taxable_income * 0.20) - 3500000
    elif taxable_income <= 100000000:
        return (taxable_income * 0.30) - 9500000
    else:
        return (taxable_income * 0.35) - 14500000

# Lớp hiển thị: Sử dụng f-string với định dạng :,.0f để tự động thêm dấu phẩy kiểu Anh
gross_sample = 40000000
dependents_sample = 1
tax_owed = calculate_pit(gross_sample, dependents_sample)

print(f"Gross Income: {gross_sample:,.0f} VND")
print(f"PIT Owed: {tax_owed:,.0f} VND")
