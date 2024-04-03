import threading
 
def proc(n):
   print("Процесс"), n
 
p1 = threading.Thread(target=proc, name="t1", args=["1"])
p2 = threading.Thread(target=proc, name="t2", args=["2"])
p1.start()
p2.start()

import threading
 
class T(threading.Thread):
  def __init__(self, n):
   threading.Thread.__init__(self, name="t" + n)
   self.n = n
  def run(self):
    print("Процесс"), self.n
 
p1 = T("1")
p2 = T("2")
p1.start()
p2.start()