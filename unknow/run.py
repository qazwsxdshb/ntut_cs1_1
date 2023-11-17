# run.py
import coverage #匯入涵蓋度紀錄套件
import unittest #匯入測試框架套件
# 實體化一個涵蓋度紀錄物件
def testPrintResult():
    cov = coverage.coverage(branch=True, source=['mybmi'])
    cov.start() #啟動測試涵蓋度紀錄
    suite = unittest.defaultTestLoader.discover("./", "data.py") # 載入測試套件
    unittest.TextTestRunner().run(suite) #執行測試套件組之測試
    cov.stop() #停止測試涵蓋度紀錄
    cov.save() #儲存測試涵蓋度資料
    cov.report() # 命令列模式展示結果
    cov.html_report(directory='cov')
testPrintResult()