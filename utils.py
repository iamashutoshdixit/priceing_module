def calcluate_fare(add_dist, DBP, DAP, TBP):
    total_fare = (DBP+(add_dist*DAP))*TBP
    return total_fare

def get_DAB(arr, distance):
    
    for i in arr:
        if distance<=i.distance:
            break
    print("Distance Select ",i.distance)
    return i

def get_duration(arr, duration):
    for i in arr:
        if duration<=i.time:
            break
    print("time range ",i.time)
    return i

    
            



