import os
output = os.environ['HOME']
desktop = os.path.expanduser("Desktop")
  

beg_path=os.path.join(output, desktop)
print(beg_path)