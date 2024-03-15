from multiprocessing import Process
import fiat_near, fiat_usdt, fiat_weth, fiat_eth, fiat_btc, fiat_wbtc, fiat_aurora


if __name__ == '__main__':
  p1 = Process(target=fiat_near.exec)
  p2 = Process(target=fiat_usdt.exec)
  p3 = Process(target=fiat_weth.exec)
  p4 = Process(target=fiat_eth.exec)
  p5 = Process(target=fiat_btc.exec)
  p6 = Process(target=fiat_wbtc.exec)
  p7 = Process(target=fiat_aurora.exec)
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p5.start()
  p6.start()
  p7.start()
