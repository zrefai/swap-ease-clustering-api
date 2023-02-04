import datetime

def getDateBoundary(daysToSubtract):
    return datetime.datetime.now() - datetime.timedelta(daysToSubtract)

def getDateObject(dateString):
    return datetime.datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S')