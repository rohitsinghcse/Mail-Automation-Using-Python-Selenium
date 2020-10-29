# Read file
def readlines_file(filename):
  # Open a file: file
  with open(filename,'r') as f: #open the file
    return f.readlines()

def read_file(filename):
  # Open a file: file
  with open(filename,'r') as f: #open the file
    return f.read()

def writeFile(filename,content):
    with open(filename,'w') as attachment:
        return attachment.write(content)

