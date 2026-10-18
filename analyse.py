with open('wards.csv') as f:
    lines=f.readlines()

#print('Number of lines:',len(lines))
for line in lines[1:]:
    #print(line.strip())
    parts = line.strip().split(',')
    ward = parts [0]
    area_km2 = float(parts [1])
    #area_hectares = area_km2 * 100
    #print (ward, "is", area_hectares, "hectares")
    if area_km2 > 9:
        size = 'large'
    else:
        size = 'small'
    print(ward, "is", size)
