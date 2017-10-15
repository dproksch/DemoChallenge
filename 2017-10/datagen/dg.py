from datetime import datetime, timedelta
import json
import fileinput
from Configuration import Configuration as C
from Utils import Utils as U


#
# Use stdout for logging.  Can change loggers if needed
#
def logIt(s):
    print(s)
    print("")

if __name__ == "__main__":
    s = "{} Data Generation Process - {} "
    s_ts =  datetime.now().isoformat(sep='T')
    logIt(s.format("Begin",s_ts))


    #
    # Process the configuration file
    #

    fileName="./dg.json"
    p = C(fileName)
    p.processConfiguration()

    # set up randomness
    util = U()
    util.setSeed(p.seed)
    util.getInt()

    #
    # How many days do we need to process?
    #
    daysToProcess = p.numberOfDays
    startDate = p.startDate
    ticks = p.ticks
    l = "Starting at {} for {} days with {} second increments"
    logIt(l.format(startDate, daysToProcess, ticks))
    st = datetime.strptime("2017-01-01", "%Y-%m-%d")
    et = st + timedelta(days=+1)
    time_step = timedelta(seconds=+ticks)

    while et > st:
        #print(st)
        st = st + time_step
    

    e_ts =  datetime.now().isoformat(sep='T')
    logIt(s.format("End",e_ts))
