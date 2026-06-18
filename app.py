# Nhập dữ liệu
gross_income = 10000000   # 10 triệu
deduction = 11000000      # giảm trừ bản thân
dependents = 0            # số người phụ thuộc
dependent_deduction = dependents * 4400000

# Tính thu nhập chịu thuế
taxable_income = gross_income - deduction - dependent_deduction

# Nếu âm thì bằng 0
if taxable_income < 0:
    taxable_income = 0

# Tính thuế
if taxable_income <= 5000000:
    tax = taxable_income * 0.05
elif taxable_income <= 10000000:
    tax = taxable_income * 0.10 - 250000
elif taxable_income <= 18000000:
    tax = taxable_income * 0.15 - 750000
else:
    tax = taxable_income * 0.20 - 1650000

# Lương thực nhận
net_income = gross_income - tax

# In kết quả
print("Gross Income:", gross_income)
print("Dependents:", dependents)
print("Taxable Income:", taxable_income)
print("Personal Income Tax:", tax)
print("Net Income:", net_income)
