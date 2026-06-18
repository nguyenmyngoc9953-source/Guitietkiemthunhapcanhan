salary = 10000000  # 10 triệu

# Giảm trừ bản thân (2026 vẫn thường dùng mốc 11 triệu nếu chưa có thay đổi luật)
deduction = 11000000

taxable_income = salary - deduction

if taxable_income <= 0:
    tax = 0
else:
    if taxable_income <= 5000000:
        tax = taxable_income * 0.05
    elif taxable_income <= 10000000:
        tax = taxable_income * 0.10 - 250000
    elif taxable_income <= 18000000:
        tax = taxable_income * 0.15 - 750000

print("Thu nhập chịu thuế:", taxable_income)
print("Thuế TNCN phải nộp:", tax)
print("Lương thực nhận:", salary - tax)
print(f"Gross Income : {sample_gross:,.0f} VND")
    print(f"Dependents   : {sample_dependents}")
    print(f"PIT Owed     : {tax_owed:,.0f} VND")
