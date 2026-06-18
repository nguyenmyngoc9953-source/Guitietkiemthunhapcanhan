import streamlit as st
st.image("")
st.set_page_config(page_title="App Tính Toán Tài Chính", page_icon="💰", layout="centered")

st.title("💰 Ứng dụng tính tiền gửi tiết kiệm & Thuế TNCN")
st.caption("Đề tài 3 _ Nguyễn Thị Mỹ Ngọc")

# ==========================================
# 1. TÍNH TIỀN GỬI TIẾT KIỆM
# ==========================================
st.header("1. Tính tiền gửi tiết kiệm")

C = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)",
    min_value=0.0,
    value=100.0,
    step=1.0,
    key="so_tien_gui"
)

i = st.number_input(
    "Nhập lãi suất gửi tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0,
    step=0.1,
    key="lai_suat"
)

n = st.number_input(
    "Nhập số tháng khách hàng gửi tiết kiệm",
    min_value=1,
    value=12,
    step=1,
    key="so_thang_gui"
)

# Tính toán tự động (không cần nút bấm để tránh mất dữ liệu khi tương tác phần dưới)
lai_suat_thap_phan = i / 100
# An: Tổng tiền nhận được theo lãi đơn (Gốc + Lãi)
An = C * (1 + (lai_suat_thap_phan / 12) * n)
# Bn: Tổng tiền nhận được theo lãi kép từng tháng
Bn = C * (1 + lai_suat_thap_phan / 12) ** n
# Tiền lãi chênh lệch
tien_lai_don = An - C
tien_lai_kep = Bn - C

st.info("📊 **Kết quả dự toán tiết kiệm:**")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Tổng nhận (Lãi đơn)", value=f"{An:,.2f} triệu")
    st.caption(f"(Trong đó tiền lãi: {tien_lai_don:,.2f} triệu)")
with col2:
    st.metric(label="Tổng nhận (Lãi kép)", value=f"{Bn:,.2f} triệu")
    st.caption(f"(Trong đó tiền lãi: {tien_lai_kep:,.2f} triệu)")


st.markdown("---")  # Đường kẻ ngang phân chia các phần


# ==========================================
# 2. TÍNH THUẾ THU NHẬP CÁ NHÂN
# ==========================================
st.header("2. Tính Thuế Thu Nhập Cá Nhân")

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

# Tính toán thuế TNCN
thu_nhap_trieu = thu_nhap / 1_000_000
giam_tru_ban_than = 11.0  
giam_tru_phu_thuoc = nguoi_phu_thuoc * 4.4  
thu_nhap_tinh_thue = thu_nhap_trieu - giam_tru_ban_than - giam_tru_phu_thuoc

if thu_nhap_tinh_thue <= 0:
    thue_phai_nop = 0
    thu_nhap_tinh_thue = 0 # Đưa về 0 để hiển thị cho đẹp
else:
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
        
    thue_phai_nop = thue_phai_nop * 1_000_000

# Hiển thị kết quả thuế TNCN
st.success("💵 **Kết quả tính toán thuế:**")
st.write(f"🔹 Thu nhập chịu thuế: **{thu_nhap_tinh_thue * 1_000_000:,.0f}** VNĐ")
st.write(f"🔥 Số thuế TNCN phải nộp: **{thue_phai_nop:,.0f}** VNĐ")
