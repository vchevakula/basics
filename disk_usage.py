import shutil
  
# Path
path = "/home/User/Documents"
  
# Get the disk usage statistics
# about the given path
stat = shutil.disk_usage(path)
  
# Print disk usage statistics
print("Disk usage statistics:")
print(stat)
