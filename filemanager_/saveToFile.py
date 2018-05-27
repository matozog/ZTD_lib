import csv

def saveDataToFile(station):
    w = csv.writer(open(station.getID() + '.csv', 'w', newline=''))
    for key, val in station.getDict().items():
        w.writerow([key, val])
        print([key, val])
