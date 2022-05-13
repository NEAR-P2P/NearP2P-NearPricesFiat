from multiprocessing import Process
import coinmarketcap

if __name__ == '__main__':
  p1 = Process(target=coinmarketcap.exec)
  p1.start()
