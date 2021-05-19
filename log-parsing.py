with open("log.txt", "r") as file:
    prev_time = ""
    hostMap = {}
    status_timeMap = {}
    for line in file:
        time = line.split("[")[1].split("]")[0].split(" ")[0]
        status_code = line.split('"')[2].split(" ")[1]
        hostname = line.split(" ")[1]
        hostMap[hostname] = hostMap.get(hostname, 0) + 1
        status_timeMap[time] = status_timeMap
#    print(hostMap)    
#        for hostname, freq in hostMap.items():
#            print(hostname, freq)

#    print(hostname)