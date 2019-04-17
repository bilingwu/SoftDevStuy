#Python
#import csv
#f = open("republicanPollData2016.csv")
#for row in csv.reader(f):
#    print(row)
#for row in csv.reader(f):
#    newrow = [row[1], row[7], row[8]]
#    print(newrow)

repubData = [
    ['Start Date', 'Trump', 'Cruz'],
    ['2016-03', 42.4, 26.7],
    ['2016-02', 37.4, 18.7],
    ['2016-01', 37.6, 16.9],
    ['2015-12', 35.7, 15.3],
    ['2015-11', 31.1,11.6]
]

trumpData = {
    {"x":"2015-nov", "y":"31.1"},
    {"x":"2015-dec", "y":"35.7"},
    {"x":"2016-jan", "y":"37.6"},
    {"x":"2016-feb", "y":"37.4"},
    {"x":"2016-mar", "y":"42.4"}
}
cruzData = {
    {"x":"2015-nov", "y":"11.6"},
    {"x":"2015-dec", "y":"15.3"},
    {"x":"2016-jan", "y":"16.9"},
    {"x":"2016-feb", "y":"18.7"},
    {"x":"2016-mar", "y":"26.7"}
}
