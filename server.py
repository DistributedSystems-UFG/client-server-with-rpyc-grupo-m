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
    try:
        index = self.value.index(data)
        return f"{data} found at position {index} in the array."
    except ValueError:
        return f"{data} not found in the array."

  def exposed_remove
    

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

