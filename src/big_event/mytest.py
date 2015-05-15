__author__ = 'haochen'


def result():
    f1 = open('BigEvent','r')
    Event = f1.readline().strip().split()
    print Event
    EventMonth = Event[0]
    EventDay = Event[1].strip().split('-')
    print EventMonth
    print EventDay
    f = open('dayRevenue','r')
    line = f.readlines()
    for day in line:
        day1 = day.strip().split('\t')
        day2 = day1[0].strip().split('-')
        month = day2[1]
        dayRevenue = day2[2]
        if EventMonth == month:
            if dayRevenue in EventDay:
                print day

if __name__ =='__main__':
    result()