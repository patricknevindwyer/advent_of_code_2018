import sys


def read_logs(filename):
    
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    # read all the lines, with a time stamp and a message
    logs = []
    for line in raw.split("\n"):
        line = line.strip()
        
        # break out the ts and message
        ts_raw, msg_raw = line.split("]")
        
        # get the ts, find the minute portion as well
        ts = ts_raw[1:]
        mn = ts_raw[-2:]
        
        # get the message cleaned up
        msg = msg_raw.strip()
        logs.append({"ts": ts, "minute": mn, "msg": msg})
    
    # sort the logs
    logs = sorted(logs, key=lambda l: l["ts"])
    
    return logs


def logs_to_sleep_schedule(logs):
    
    schedules = []
    
    # break it down to guards and sleep/wake
    sleeps = []
    guard = None
    start = None
    
    for log in logs:
        if log["msg"].startswith("Guard"):
            # close out the old sleep schedule if it exists:
            if guard is not None:
                
                # track
                schedules.append(
                    {"guard": guard, "sleeps": sleeps}
                )
                
                # reset
                guard = None
                sleeps = []
                start = None
            
            # parse the guard name
            guard = log["msg"].split("#")[1].split(" ")[0]

        elif log["msg"].startswith("wakes"):
            # close out a sleep
            sleeps.append({"start": int(start), "end": int(log["minute"])})
            start = None
        elif log["msg"].startswith("falls"):
            # start a sleep
            start = log["minute"]
            
    # track last cycle
    if guard is not None:
        schedules.append(
            {"guard": guard, "sleeps": sleeps}
        )
    
    # for each sleep cycle, we need to stretch out the minutes so we can count and diff them later
    for s_idx in range(len(schedules)):
        sched = schedules[s_idx]
        sched["sleeping_minutes"] = []
        for sleep in sched["sleeps"]:
            for sleep_minute in range(sleep["start"], sleep["end"] + 1):
                sched["sleeping_minutes"].append(sleep_minute)
    
    # now gather by guard
    guards = {}
    
    for sched in schedules:
        g = sched["guard"]
        if g not in guards:
            guards[g] = {"times_asleep": 0, "sleep_minutes": []}
        
        # add in the number of times asleep
        guards[g]["times_asleep"] += len(sched["sleeps"])
        
        # add on all the minutes
        for sleep_min in sched["sleeping_minutes"]:
            guards[g]["sleep_minutes"].append(sleep_min)
    
    return guards


def guard_sleeping_most(guards):
    
    g_mins = {}
    
    for g, data in guards.items():
        g_mins[g] = len(data["sleep_minutes"])
    
    return sorted(g_mins.items(), key=lambda g: g[1], reverse=True)[0][0]


def most_likely_asleep_at(guards, g_id):
    sleep_hist = {}
    for m in guards[g_id]["sleep_minutes"]:
        if m not in sleep_hist:
            sleep_hist[m] = 0
        sleep_hist[m] += 1
    
    return sorted(sleep_hist.items(), key=lambda s: s[1], reverse=True)[0][0]
    
if __name__ == "__main__":
    logs = read_logs(sys.argv[-1])
    guards = logs_to_sleep_schedule(logs)
    
    g_id = guard_sleeping_most(guards)
    print("Guard %s slept the most" % (g_id,))
    g_at = most_likely_asleep_at(guards, g_id)
    print("Guard %s is most likely asleep at %d" % (g_id, g_at))
    print("Chksum: %d" % (int(g_id) * g_at,))
    