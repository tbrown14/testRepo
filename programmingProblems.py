

#Fibonacci Sequence 
a,b = 0,1
for i in range(0,45):
    if i % 2 !=0:
        print(i, end = "")

    

#return people who live in ontario
def get_resident_Prov_on(file_name, prov_name):
    data = {}
    csv = open(file_name, "r")
    for line in csv:
        print(line)
        first, last, address, province = line.split(',')
        province_s = province.replace(" ", "")
      
        if province_s not in data:
            data[province_s] = []
        data[province_s].append(first)
    print(data.get(prov_name))
    return data.get(prov_name)

get_resident_Prov_on('C:\\Users\\Travis Brown\\Downloads\\address - address.csv', 'Ontario')