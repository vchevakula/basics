import shutil
  
# Path
path = "/home/vchevakula/"

# Get the disk usage statistics
# about the given path
stat = shutil.disk_usage(path)
gb = 10 ** 9
  
# Print disk usage statistics
print("Disk usage statistics in your linux server:")
print('Total Space: {:6.2f} GB'.format(stat[0] /gb))
print('Total Used Space: {:6.2f} GB'.format(stat[1] /gb))
print('Total Free Space: {:6.2f} GB'.format(stat[2] /gb))
