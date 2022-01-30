def get_rate_avg(arg):
    rate = []
    for i in arg:
        rate.append(i.rate)
    avg=0
    for i in rate:
        avg+=i
    avg = float(avg/len(rate))
    return avg