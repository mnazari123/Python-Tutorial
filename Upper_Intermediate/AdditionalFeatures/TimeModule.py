import time

print(time.ctime()) # convert a time expressing in seconds since epoch to a readable string
                     # epock = when your computer htinks time began (reference points)

print(time.time()) # return current seconds since epoch

print(time.ctime(time.time()))
time_object = time.localtime()

print(time_object)
# time.strfime(format, time_object)
localtime = time.strftime("%b %d %Y %H:%M:%S")
print(localtime)

# time.straptime(format, time_object)

time_string = "20 April, 2022"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# Time Tuple (year, month, day, hours, minutes, #day of the week, #day of the year, dst)
time_tuple = (2022, 4, 20 , 4, 20, 0 , 0, 0, 0)
time_string = time.asctime(time_tuple)

print(time_string)

# (year, month, day, hours, minutes, secs, # day oteh week, # day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
