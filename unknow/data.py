# data.py
import unittest
import mybmi 
class printResult(unittest.TestCase): #設計測試驅動程式類別
    def test_computeBMIOK(self): #設計測試主程式功能的方法,self 是物件本身
        self.assertEqual(mybmi.computeBMI(52, 0.05), -1)
        self.assertEqual(mybmi.computeBMI(52, 0.05), -1) 
        self.assertEqual(mybmi.computeBMI(2, 1.55), -1) 
        self.assertEqual(mybmi.computeBMI(500, 5), -1) 
        self.assertEqual(mybmi.computeBMI(500, 1.55), -1) 
        self.assertEqual(mybmi.computeBMI(200, 2.5), 32.00) 
        self.assertEqual(mybmi.computeBMI(3, 0.5), 12.00)
        

a=printResult()
print(a.test_computeBMIOK())



