import streamlit as st

st.title("💰 App tính Thuế Thu Nhập Cá Nhân đề tài 3 Nguyễn Thị Mỹ Ngọc")

# 3. Ô nhập dữ liệu số thu nhập trước thuế (có nút + -)
thu_nhap = st.number_input(
    label="Nhập thu nhập trước thuế (VNĐ)",
    min_value=0.0,
    value=50000000.0,
    step=500000.0,
    format="%.2f"
)

# 4. Ô nhập số người phụ thuộc (có nút + -)
nguoi_phu_thuoc = st.number_input(
    label="Nhập số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

# 5. Nút bấm tính thuế
if st.button("Tính thuế"):
    # Quy đổi đơn vị sang triệu đồng cho dễ tính toán bậc lũy tiến
    thu_nhap_trieu = thu_nhap / 1_000_000
    
    # Mức giảm trừ gia cảnh cố định
    giam_tru_ban_than = 11.0  # 11 triệu VNĐ
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 4.4  # 4.4 triệu VNĐ/người
    
    # Tính thu nhập chịu thuế sau giảm trừ
    thu_nhap_tinh_thue = thu_nhap_trieu - giam_tru_ban_than - giam_tru_phu_thuoc
    
    if thu_nhap_tinh_thue <= 0:
        thue_phai_nop = 0
    else:
        # Công thức tính thuế lũy tiến từng phần theo quy định
        if thu_nhap_tinh_thue <= 5:
            thue_phai_nop = thu_nhap_tinh_thue * 0.05
        elif thu_nhap_tinh_thue <= 10:
            thue_phai_nop = thu_nhap_tinh_thue * 0.1 - 0.25
        elif thu_nhap_tinh_thue <= 18:
            thue_phai_nop = thu_nhap_tinh_thue * 0.15 - 0.75
        elif thu_nhap_tinh_thue <= 32:
            thue_phai_nop = thu_nhap_tinh_thue * 0.2 - 1.65
        elif thu_nhap_tinh_thue <= 52:
            thue_phai_nop = thu_nhap_tinh_thue * 0.25 - 3.25
        elif thu_nhap_tinh_thue <= 80:
            thue_phai_nop = thu_nhap_tinh_thue * 0.3 - 5.85
        else:
            thue_phai_nop = thu_nhap_tinh_thue * 0.35 - 9.85
            
        # Quy đổi ngược lại thành tiền VNĐ đầy đủ
        thue_phai_nop = thue_phai_nop * 1_000_000

    # 6. Hiển thị kết quả trực quan ra màn hình
    st.markdown("### Kết quả tính toán:")
    st.success(f"Số thuế TNCN phải nộp: **{thue_phai_nop:,.0f}** VNĐ")
