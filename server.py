import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
    
  def exposed_search(self, data):
        if data in self.value:
            return f"{data} found in the array."
        else:
            return f"{data} not found in the array."
    

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

