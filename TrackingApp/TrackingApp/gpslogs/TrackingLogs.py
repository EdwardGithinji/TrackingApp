import csv
with open ('TrackingInfo.csv','w') as csvfile:
    fieldnames=['Command','Coordinates','Time']
    filewriter=csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    #filewriter=csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Command','Coordinates','Time'])
csvfile.close()
