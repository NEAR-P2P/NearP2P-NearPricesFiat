from multiprocessing import Process
import fiat_near, fiat_usdt, fiat_weth, fiat_eth, fiat_btc, fiat_wbtc, fiat_aurora, fiat_wnear, fiat_from_ref_finance


if __name__ == '__main__':
  p1 = Process(target=fiat_near.exec)
  p2 = Process(target=fiat_from_ref_finance.exec)
  p1.start()
  p2.start()
