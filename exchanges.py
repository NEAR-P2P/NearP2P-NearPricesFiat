from multiprocessing import Process
import coinmarketcap_near
import coinmarketcap_usdc


if __name__ == '__main__':
  p1 = Process(target=coinmarketcap_near.exec)
  p2 = Process(target=coinmarketcap_usdc.exec)
  p1.start()
  p2.start()
