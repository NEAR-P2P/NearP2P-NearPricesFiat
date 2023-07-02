from multiprocessing import Process
import fiat_near, fiat_usdt


if __name__ == '__main__':
  p1 = Process(target=fiat_near.exec)
  p2 = Process(target=fiat_usdt.exec)
  p1.start()
  p2.start()
