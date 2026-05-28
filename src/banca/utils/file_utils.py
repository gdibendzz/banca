
def write(text, filename, mode):
     with open(filename, mode) as f:
            f.write(text)

def read(filename):
     
     try:
          with open(filename) as f:
               return f.read()
     except FileNotFoundError:
          print("File non esistente")
                    
