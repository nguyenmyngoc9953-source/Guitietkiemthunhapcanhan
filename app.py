import streamlit as st
st.image("IMG_7732.jpeg")
st.title("💰 Ứng dụng tính tiền gửi tiết kiệm & Thuế TNCN Đề tài 3 _ Nguyễn Thị Mỹ Ngọc")

st.header("1. Tính tiền gửi tiết kiệm")

# Nhập dữ liệu tiết kiệm
C = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)",
    min_value=0.0,
    value=100.0,
    key="so_tien_gui"
)

i = st.number_input(
    "Nhập lãi suất gửi tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0,
    key="lai_suat"
)

n = st.number_input(
    "Nhập số tháng khách hàng gửi tiết kiệm",
    min_value=1,
    value=12,
    key="so_thang_gui"
)

# Nút tính toán tiết kiệm
if st.button("Tính toán tiết kiệm"):
    # Đổi lãi suất từ % sang số thập phân
    lai_suat_thap_phan = i / 100
    
    # Lãi đơn
    An = C * (1 + (lai_suat_thap_phan / 12) * n)
    # Lãi kép
    Bn = C * (1 + lai_suat_thap_phan / 12) ** n

    st.success("Kết quả tính toán tiết kiệm:")
    st.write(f"📌 Số tiền khách hàng nhận được theo lãi đơn: **{An:,.2f} triệu đồng**")
    st.write(f"📌 Số tiền khách hàng nhận được theo lãi kép: **{Bn:,.2f} triệu đồng**")

st.markdown("---")  # Đường kẻ ngang phân chia các phần
st.header("2. Tính Thuế Thu Nhập Cá Nhân")

# Nhập dữ liệu tính thuế
thu_nhap = st.number_input(
    label="Nhập thu nhập trước thuế (VNĐ)",
    min_value=0.0,
    value=20000000.0,
    step=500000.0,
    format="%.2f",
    key="thu_nhap_tncn"
)

nguoi_phu_thuoc = st.number_input(
    label="Nhập số người phụ thuộc",
    min_value=0,
    value=0,
    step=1,
    key="phu_thuoc_tncn"
)

# Nút tính toán thuế
if st.button("Tính thuế TNCN"):
    # Đổi sang đơn vị Triệu Đồng để áp biểu thuế lũy tiến
    thu_nhap_trieu = thu_nhap / 1_000_000
    
    # Mức giảm trừ
    giam_tru_ban_than = 11.0  # 11 triệu/tháng
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 4.4  # 4.4 triệu/người
    
    # Thu nhập tính thuế
    thu_nhap_tinh_thue = thu_nhap_trieu - giam_tru_ban_than - giam_tru_phu_thuoc
    
    if thu_nhap_tinh_thue <= 0:
        thue_phai_nop = 0
    else:
        # Biểu thuế lũy tiến từng phần hiện hành
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
            
        # Quy đổi lại thành tiền Đồng
        thue_phai_nop = thue_phai_nop * 1_000_000

    st.success("Kết quả tính toán thuế:")
    st.write(f"💵 Số thuế TNCN phải nộp: **{thue_phai_nop:,.0f} VNĐ**")
