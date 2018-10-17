import unittest,time
from cms import goods
from order import  xhjx_order
import HTMLTestRunner
print("目前在执行之前需要进行手动操作的有：\n"+
"1.进入前端页面后，手动移动vc位置，以免页面可能无法点击")
cmsGoods=goods.cmsGoods
order = xhjx_order.order
order.goodsName = cmsGoods.goodsName
order.goodsName='autoTjl10081521'
suite = unittest.TestSuite()
# suite.addTest(cmsGoods('testAddGoods'))
# suite.addTest(cmsGoods('testCheckGoods'))
suite.addTest(order('testOrderGoodsdetail2Pay'))
suite.addTest(order('testOrderGoodsdetail2PayCansel'))
suite.addTest(order('testOrderGoodsdetail2PayAutoReceipt'))
suite.addTest(order('testOrderGoodsdetail2TimeOutCansel'))
time=time.strftime('%y%m%d%H%M',time.localtime())
fileName='../report/'+time+'res.html'
fp=open(fileName,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp)
runner.run(suite)
fp.close()