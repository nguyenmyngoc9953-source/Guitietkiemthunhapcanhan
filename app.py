import unittest
from main import tinh_thue_tncn 

class TestTinhThueHoanChinh(unittest.TestCase):
    
    def test_thu_nhap_5_trieu(self):
        # Lương 5tr -> Không phải nộp thuế
        self.assertEqual(tinh_thue_tncn(5000000, 0), 0)
        
    def test_thu_nhap_20_trieu_khong_nguoi_phu_thuoc(self):
        # Giả sử thu nhập chịu thuế đã trừ bảo hiểm là 17.900.000
        # TNTT = 17.900.000 - 15.500.000 = 2.400.000 (Bậc 1: 5%)
        self.assertEqual(tinh_thue_tncn(17900000, 0), 120000)

    def test_thu_nhap_cao_co_nguoi_phu_thuoc(self):
        # Giả sử thu nhập chịu thuế đã trừ bảo hiểm là 44.750.000, có 1 NPT
        # TNTT = 44.750.000 - 15.500.000 - 6.200.000 = 23.050.000 (Bậc 2)
        # Thuế = 23.050.000 * 10% - 500.000 = 1.805.000
        self.assertEqual(tinh_thue_tncn(44750000, 1), 1805000)

if __name__ == '__main__':
    unittest.main()
