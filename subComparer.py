# -*- coding: utf-8 -*-
import csv

def SubCompare (sub1, sub2):
    
    sub1Dict = {} #will be populated with the contents of the csv of sub1
    sub2Dict = {} #will be populated with the contents of the csv of sub2
    diffs = {}
    
    count = 0
    sub1Total = 0
    sub2Total = 0
    
    with open(sub1 + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            print(count)
            count += 1
            try: 
                if row:
                    if (int(row[1]) >= 5):
                        sub1Dict[row[0]] = int(row[1])
                        sub1Total += int(row[1])
            except UnicodeDecodeError:
                pass
    
    with open(sub2 + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            try:
               if row:
                    if (int(row[1]) >= 5):
                        sub2Dict[row[0]] = int(row[1])
                        sub2Total += int(row[1])
            except UnicodeDecodeError:
                pass
    
    for key in sub1Dict:
        if (key in sub2Dict and sub1Dict[key] >= 5):
            diffs[key] = ((sub2Dict[key] / sub2Total) / (sub1Dict[key] / sub1Total))
        elif (sub1Dict[key] >= 5):
            diffs[key] = 1/sub1Dict[key]
    
    for key in sub2Dict:
        if (key in sub1Dict and sub2Dict[key] >= 5):
            diffs[key] = ((sub2Dict[key] / sub2Total) / (sub1Dict[key] / sub1Total))  
        elif (sub2Dict[key] >= 5): 
            diffs[key] = sub2Dict[key]
    
    print(sorted(diffs.items(), key=lambda item: item[1]))
        
    #method to populate the dictionary, while counting the words used in both
    
