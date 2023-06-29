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

  def exposed_remove(self, data):
    if data in self.value:
        self.value.remove(data)
        return f"Element {data} removed from the array."
    else:
        return f"Element {data} not found in the array. Nothing removed."
      
  def exposed_sort(self):
    self.value.sort()
    return "Array sorted in ascending order."


if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

