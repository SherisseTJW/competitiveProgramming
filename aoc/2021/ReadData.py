def readData(filename):
   data = []
   f = open(filename, "r")

   for line in f:
      data.append(line.strip())
   f.close()

   return data