import streamlit as st

# Thiết lập tiêu đề trang
st.set_page_config(page_title="Tính Thuế TNCN", page_icon="💰")

st.title("Tính Thuế TNCN · Streamlit")

# Tạo form nhập liệu như trong image.png
thu_nhap = st.number_input("Nhập thu nhập trước thuế (VNĐ):", min_value=0, value=20000000, step=1000000)
nguoi_phu_thuoc = st.number_input("Nhập số người phụ thuộc:", min_value=0, value=0, step=1)

st.markdown("---")

# Nút tính toán
if st.button("📊 Tính toán"):
    # Công thức tính toán cơ bản (Giảm trừ gia cảnh bản thân 11tr, phụ thuộc 4.4tr)
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 4400000
    
    thu_nhap_tinh_thue = max(0, thu_nhap - giam_tru_ban_than - giam_tru_phu_thuoc)
    
    # Tính thuế theo lũy tiến đơn giản để minh họa kết quả giống ảnh
    # Với 20tr, 0 người phụ thuộc -> Thu nhập tính thuế = 9tr -> Thuế = 9tr * 5% = 450,000đ
    if thu_nhap_tinh_thue <= 5000000:
        thue = thu_nhap_tinh_thue * 0.05
    elif thu_nhap_tinh_thue <= 10000000:
        thue = 250000 + (thu_nhap_tinh_thue - 5000000) * 0.1
    else:
        thue = 750000 + (thu_nhap_tinh_thue - 10000000) * 0.15
        
    thu_nhap_sau_thue = thu_nhap - thue

    # Hiển thị kết quả đúng định dạng trong ảnh
    st.header("📈 Kết quả tính toán")
    st.success("Tính toán thành công!")
    
    st.write(f"📌 **Thu nhập tính thuế:** {thu_nhap_tinh_thue:,.0f} VNĐ")
    st.write(f"📌 **Thuế TNCN phải nộp:** {thue:,.0f} VNĐ")
    st.write(f"📌 **Thu nhập sau thuế:** {thu_nhap_sau_thue:,.0f} VNĐ")
