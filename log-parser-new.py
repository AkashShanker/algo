def log_parse(logfile):
    errorMap = {}
    with open(logfile, 'r') as logfile:
        for line in logfile:
            hostname = line.split(" ")[0]
            error_code = line.split(" ")[8]
            errorMap[hostname] = errorMap.get(hostname, 0) + 1
        
        logfile = "log_out.txt"
        outfile = open(logfile, 'w')
        
        for h,f in errorMap.items():
            outfile.write(h+" "+str(f)+"\n")
        outfile.close()
    
if __name__ == '__main__':
    log_parse("log.txt")