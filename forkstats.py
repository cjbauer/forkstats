# Code to be determining how long it would take to be recovering from large loss of mining power on bitcoin chain.
# Christian Bauer

def postfork_mins_per_block(y):
    return 10.0/y

def postfork_days_until_diffadj(x,y):
    blks=2016.0*(1-x)
    return ((postfork_mins_per_block(y)*blks)/(60*24))

def postdiff_mins_per_block(x,y):
    return postfork_mins_per_block(y)/((x*10.0+(1-x)*postfork_mins_per_block(y))/10.0)

def postfork_weeks_until(x,y,m):
    days1=postfork_days_until_diffadj(x,y)
    mpb2=postdiff_mins_per_block(x,y)
    if mpb2 <= m:
        return (days1/7.0)
    else:
        days2=(mpb2*2016.0)/(60*24)
        return (days1+days2)/7.0

def report2(x,y):
    print ("** Fork "+("{:.0f}".format(x*100))+"% through period with core retaining "+("{:.0f}".format(y*100))+"% of miners")
    days1=postfork_days_until_diffadj(x,y)
    print ("Until next difficulty adjustment: "+("{:.1f}".format(days1))+" days ("+("{:.1f}".format(days1/7.0))+" weeks)")
    mpb2=postdiff_mins_per_block(x,y)
    print ("Minutes per block after first difficulty adjustment: "+("{:.1f}".format(mpb2)))

# Choose best block to fork so m minutes per block comes fastest (or None if impossible).
def bestfork(y,m):
    besti = None
    bestr = 10000.0
    for i in range(2016):
        if postdiff_mins_per_block(i/2016.0,y) < m:
            r = postfork_days_until_diffadj(i/2016.0,y)
            if r < bestr:
                besti = i
                bestr = r
    return besti

# Choose worst block. Unused now.
def worstfork(y,m):
    worsti = 0
    worstr = 0.0
    for i in range(2016):
        r = postfork_weeks_until(i/2016.0,y,m)
        if r > worstr:
            worsti = i
            worstr = r
    return worsti

def report(y):
    print ("\n* Assume core retains "+("{:.0f}".format(y*100))+"% of miners")
    print ("Minutes per block after the fork: "+("{:.1f}".format(postfork_mins_per_block(y))))
    i=bestfork(y,30.0) # find best block to fork at to quickly get out of "Red zone" and into "Amber Zone" (30 minute block times)
    print ("(To Amber) Best recovery if fork is at block "+("{:.0f}".format(i))+" of the 2 week difficulty window -- "+("{:.1f}".format(i/20.16))+"% through the window")
    report2(i/2016.0,y)
    i=bestfork(y,20.0) # find best block to fork at to quickly get out of "Red zone" and into "Yellow Zone" (20 minute block times)
    print ("(To Yellow) Best recovery if fork is at block "+("{:.0f}".format(i))+" of the 2 week difficulty window -- "+("{:.1f}".format(i/20.16))+"% through the window")
    report2(i/2016.0,y)
#    i=bestfork(y,12.0)
#    print ("(To Green) Best recovery if fork is at block "+("{:.0f}".format(i))+" of the 2 week difficulty window -- "+("{:.1f}".format(i/20.16))+"% through the window")
#    report2(i/2016.0,y)
#    j=worstfork(y,12.0)
#    print ("(To Green) Worst recovery if fork is at block "+("{:.0f}".format(j))+" of the 2 week difficulty window -- "+("{:.1f}".format(j/20.16))+"% through the window")
#    report2(j/2016.0,y)
#    j=worstfork(y,20.0)
#    print ("(To Yellow) Worst recovery if fork is at block "+("{:.0f}".format(j))+" of the 2 week difficulty window -- "+("{:.1f}".format(j/20.16))+"% through the window")
#    report2(0.0,y) # fork directly after a difficulty adjustment
#    report2(0.25,y) # fork 1/4 into 2 week period
#    report2(0.5,y) # fork halfway through 2 week period
#    report2(0.65,y) # fork 65% into 2 week period
#    report2(0.67,y) # fork 2/3 into 2 week period
#    report2(0.7,y) # fork 70% into 2 week period
#    report2(0.73,y)
#    report2(0.74,y)
    report2(0.75,y) # fork 3/4 into 2 week period
#    report2(0.76,y)
#    report2(0.77,y)
#    report2(0.78,y)
#    report2(0.79,y)
#    report2(0.8,y) # fork 80% into 2 week period
#    report2(0.81,y)
#    report2(0.82,y)
#    report2(0.83,y)
#    report2(0.84,y)
#    report2(0.85,y)
#    report2(0.99,y) # fork shortly before a difficulty adjustment

# 40% mining power stays on Core chain
# report(0.4)

# 35% mining power stays on Core chain
# report(0.35)

# 30% mining power stays on Core chain
# report(0.3)

# 25% mining power stays on Core chain
report(0.25)

# 20% mining power stays on Core chain
report(0.2)

# 15% mining power stays on Core chain
report(0.15)

# 10% mining power stays on Core chain
report(0.1)

# 5% mining power stays on Core chain
report(0.05)
