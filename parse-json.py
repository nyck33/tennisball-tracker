import json
from pprint import pprint
import glob
import re
import sys

with open('train_set4/train/via_region_data.json') as f:
    data = json.load(f)

datatxt = json.dumps(data)

f = open("json-annot.txt", "w")
f.write(datatxt)
f.close()  

#f = open("json-annot.txt", "r")
#print(f[:10])
print(datatxt[:10])
xy = []
for line in datatxt:
    #if word in line.split():
    m = re.match('\d{3}', line)
    #m = re.match('\d{3}', line)
    print(m)
    
    #xy.append(m)

#print(xy)

#xy = []

print(data["frame65.jpg79938"]['regions']["0"]['shape_attributes']['cx'])
#print(data["frame65.jpg79938"]['regions'].values)

'''
#iterate through keys in dict
for key in data.keys():
    print("key {}".format(key))
    m = re.match('frame(\d+).jpg(\d+)$' , key)
    if not m: 
        continue
    f1, f2 = map(int, m.groups()) #mapping the wildcards to f1 and f2
    print("f1 {}, f2 {}".format(f1, f2))
    if f1<0 or f1>1199 or f2<10000 or f2>99999: 
        continue
    print("x {}".format(data[key]['regions']))  # .values)) #['0']['shape_attributes']['cx']))
    print("y {}".format(data[key]['regions']))   #.values)) #['0']['shape_attributes']['cy']))
    x = data[key]['regions']['0']['shape_attributes']['cx']
    y = data[key]['regions']['0']['shape_attributes']['cy']
    pts = (x, y)
    xy.append(pts)

f = open("json-annot.txt", "w")
f.write(data)
f.close()  
'''