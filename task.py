import csv
# format distance to integers on file read

def get_stops(string):
    li = list(string.split(", "))
    return li

def is_trip(firstcity, secondcity, row):
    return (row['to'] == firstcity and row['from'] == secondcity) or (row['from'] == firstcity and row['to'] == secondcity)

def get_trip_distance(firstcity, secondcity):
    for row in distances:
        if is_trip(firstcity,secondcity, row):
            return int(row['distance'])
        
def calc_distance(row):
        stops = get_stops(row['stops'])
        len_stops = len(stops)
        totalDist = 0
        i = 0
        while i < len_stops - 1:
            totalDist += get_trip_distance(stops[i], stops[i + 1])
            i += 1
        return totalDist

distances = list(csv.DictReader(open("data/Routes - distances.csv")))
routes = list(csv.DictReader(open("data/Routes - routes.csv")))
for row in routes:
    totaldistance = calc_distance(row)
    print(f"Distance from {row['source']} to {row['destination']} is {totaldistance}.")
    