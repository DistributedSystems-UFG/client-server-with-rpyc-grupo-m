import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  conn.root.exposed_search(6)
  conn.root.exposed_search(4)
  conn.root.exposed_remove(6)
  conn.root.exposed_sort()
  print (conn.root.exposed_value())   # Print the result
