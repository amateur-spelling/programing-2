print("input time in mintues")
ipdtime = float(input("Designing: "))
ipctime = float(input("Coding: "))
ipbtime = float(input("Debugging: "))
ipttime = float(input("Testing: "))

sum = float(ipdtime + ipctime + ipbtime + ipttime)
dtime = round(float((ipdtime / sum) * 100),2)
ctime = round(float((ipctime / sum) * 100),2)
btime = round(float((ipbtime / sum) * 100),2)
ttime = round(float((ipttime / sum) * 100),2)

print("Task     " + "Percent of time")
print("Designing: " + str(dtime) + "%")
print("Coding: " + str(ctime) + "%")
print("Debugging: " + str(btime) + "%")
print("Testing: " + str(ttime) + "%")