import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính thu nhập cá nhân Đề tài 3 Nguyễn Thị Mỹ Ngọc")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền thu nhập cá nhân (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất gửi tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng thu nhập cá nhân",
    min_value=1,
    value=12
)

# Đổi lãi suất từ % sang số thập phân
i = i / 100

# Nút tính toán
if st.button("Tính toán"):
    
    # Lãi đơn
    An = C * (1 + (i / 12) * n)

    # Lãi kép
    Bn = C * (1 + i / 12) ** n

    st.success("Kết quả tính toán")

    st.write(
        f"📌 Số tiền thu nhập cá nhân theo lãi đơn: **{An:,.2f} triệu đồng**"
    )

    st.write(
        f"📌 Số tiền thu nhập cá nhân theo lãi kép: **{Bn:,.2f} triệu đồng**"
    )
