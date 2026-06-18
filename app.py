import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính thu nhập cá nhân Đề tài 3 Nguyễn Thị Mỹ Ngọc")

# Nhập dữ liệu
def tinh_thue_tncn(thu_nhap_chiu_thue, so_nguoi_phu_thuoc=0, bao_hiem=0):
    # 1. Tính các khoản giảm trừ
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 4400000
    tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc + bao_hiem
    
    # 2. Tính thu nhập tính thuế
    thu_nhap_tinh_thue = thu_nhap_chiu_thue - tong_giam_tru
    if thu_nhap_tinh_thue <= 0:
        return 0, 0
        
    # 3. Tính thuế theo phương pháp lũy tiến từng phần
    bac_thue = [
        (5000000, 0.05),
        (10000000, 0.10),
        (18000000, 0.15),
        (32000000, 0.20),
        (52000000, 0.25),
        (80000000, 0.30),
        (float('inf'), 0.35)
    ]
    
    thue_phai_nop = 0
    thu_nhap_con_lai = thu_nhap_tinh_thue
    han_muc_truoc = 0
    
    for han_muc, thue_suat in bac_thue:
        khoang_cach = han_muc - han_muc_truoc
        if thu_nhap_con_lai > khoang_cach:
            thue_phai_nop += khoang_cach * thue_suat
            thu_nhap_con_lai -= khoang_cach
            han_muc_truoc = han_muc
        else:
            thue_phai_nop += thu_nhap_con_lai * thue_suat
            break
            
    return thu_nhap_tinh_thue, round(thue_phai_nop)

# --- KHU VỰC NHẬP SỐ LIỆU CỦA BẠN ĐỂ CHẠY THỬ ---
thu_nhap = 30000000  # Tổng thu nhập chịu thuế (Ví dụ: 30 triệu)
nguoi_phu_thuoc = 1  # Số người phụ thuộc (Ví dụ: 1 người)
tien_bao_hiem = 3150000 # Tiền bảo hiểm bắt buộc 10.5% (Ví dụ: 3,15 triệu)

# Chạy lệnh tính toán
tntt, thue = tinh_thue_tncn(thu_nhap, nguoi_phu_thuoc, tien_bao_hiem)

print(f"Thu nhập tính thuế: {tntt:,} VNĐ")
print(f"Thuế TNCN phải nộp: {thue:,} VNĐ")
