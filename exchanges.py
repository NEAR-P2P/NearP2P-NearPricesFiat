from multiprocessing import Process
import time
import fiat_near, fiat_usdt, fiat_weth, fiat_eth, fiat_btc, fiat_wbtc, fiat_aurora, fiat_wnear, fiat_from_ref_finance


if __name__ == '__main__':
  while True:
    print("Starting price update...")
    # p1 = Process(target=fiat_near.exec)
    p2 = Process(target=fiat_from_ref_finance.exec)
    # p1.start()
    p2.start()

    # p1.join()
    p2.join() # Wait for the process to complete before continuing

    print("Update finished. Waiting for 5 minutes.")
    time.sleep(300) # Wait for 5 minutes (5 * 60 seconds)
