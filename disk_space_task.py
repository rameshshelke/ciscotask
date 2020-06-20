# import psutil
#
# hdd = psutil.disk_usage('/')
#
# print ("Total: %d GiB" % hdd.total / (2**30))
# print ("Used: %d GiB" % hdd.used / (2**30))
# print ("Free: %d GiB" % hdd.free / (2**30))

import shutil
#amounts of total, used and free space in your hard drive.
total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))


