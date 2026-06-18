def tinh_thue_tncn(thu_nhap_chiu_thue, so_nguoi_phu_thuoc=0):
    # 1. Các khoản giảm trừ
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 4400000
    tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc
    
    # 2. Thu nhập tính thuế
    thu_nhap_tinh_thue = max(0, thu_nhap_chiu_thue - tong_giam_tru)
    
    # 3. Tính thuế theo biểu lũy tiến từng phần
    muc_thue = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35]
    gioi_han = [5000000, 10000000, 1800000, 32000000, 52000000, 80000000] # Phần chênh lệch từng bậc
    thue_phai_nop = 0
    
    if thu_nhap_tinh_thue > 0:
        if thu_nhap_tinh_thue <= 5000000:
            thue_phai_nop = thu_nhap_tinh_thue * muc_thue[0]
        elif thu_nhap_tinh_thue <= 10000000:
            thue_phai_nop = (5000000 * muc_thue[0]) + ((thu_nhap_tinh_thue - 5000000) * muc_thue[1])
        elif thu_nhap_tinh_thue <= 18000000:
            thue_phai_nop = (5000000 * muc_thue[0]) + (5000000 * muc_thue[1]) + ((thu_nhap_tinh_thue - 10000000) * muc_thue[2])
        elif thu_nhap_tinh_thue <= 32000000:
            thue_phai_nop = (5000000 * muc_thue[0]) + (5000000 * muc_thue[1]) + (8000000 * muc_thue[2]) + ((thu_nhap_tinh_thue - 18000000) * muc_thue[3])
        elif thu_nhap_tinh_thue <= 52000000:
            thue_phai_nop = 250000 + 500000 + 1200000 + (thu_nhap_tinh_thue - 32000000) * muc_thue[4]
        elif thu_nhap_tinh_thue <= 80000000:
            thue_phai_nop = 250000 + 500000 + 1200000 + 4000000 + (thu_nhap_tinh_thue - 52000000) * muc_thue[5]
        else:
            thue_phai_nop = 250000 + 500000 + 1200000 + 4000000 + 5000000 + 8400000 + (thu_nhap_tinh_thue - 80000000) * muc_thue[6]
            
    return thue_phai_nop

# Ví dụ thực tế: Thu nhập chịu thuế là 30.000.000 VNĐ, có 1 người phụ thuộc
luong_net = tinh_thue_tncn(30000000, 1)
print(f"Thuế TNCN phải nộp là: {luong_net:,.0f} VNĐ")
