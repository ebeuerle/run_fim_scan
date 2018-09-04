

class FileController(object):
     def __init__(self):
         return

     def load_file(self):
         f = open('agent_ids.txt', 'r')
         x = f.read().splitlines()
         f.close()
         return x
