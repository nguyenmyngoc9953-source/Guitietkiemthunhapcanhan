def tinh_thue_tncn(thu_nhap_chiu_thue, nguoi_phu_thuoc=0):
    # Các khoản giảm trừ (Cập nhật mức mới nhất)
    # Giảm trừ bản thân: 11 triệu đồng/tháng
    # Giảm trừ người phụ thuộc: 4.4 triệu đồng/người/tháng
    giam_tru_ban_than = 11.0
    giam_tru_nguoi_phu_thuoc = 4.4 * nguoi_phu_thuoc
    
    # Thu nhập tính thuế
    thu_nhap_tinh_thue = thu_nhap_chiu_thue - giam_tru_ban_than - giam_tru_nguoi_phu_thuoc
    
    # Nếu thu nhập tính thuế <= 0, không phải đóng thuế
    if thu_nhap_tinh_thue <= 0:
        return 0.0
        
    # Tính thuế theo biểu thuế lũy tiến (triệu đồng/tháng)
    bac_thue = [
        (5.0, 0.05),   # Đến 5 triệu: 5%
        (10.0, 0.10),  # Từ 5 - 10 triệu: 10%
        (18.0, 0.15),  # Từ 10 - 18 triệu: 15%
        (32.0, 0.20),  # Từ 18 - 32 triệu: 20%
        (52.0, 0.25),  # Từ 32 - 52 triệu: 25%
        (80.0, 0.30),  # Từ 52 - 80 triệu: 30%
        (float('inf'), 0.35) # Trên 80 triệu: 35%
    ]
    
    tien_thue = 0.0
    han_muc_truoc = 0.0
    
    for han_muc, thue_suat in bac_thue:
        if thu_nhap_tinh_thue > han_muc:
            tien_thue += (han_muc - han_muc_truoc) * thue_suat
            han_muc_truoc = han_muc
        else:
            tien_thue += (thu_nhap_tinh_thue - han_muc_truoc) * thue_suat
            break
            
    return tien_thue
