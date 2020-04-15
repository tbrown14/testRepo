

#Fibonacci Sequence 

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

        province = province.rstrip()
      
        if province not in data:
            data[province] = []
        data[province].append(first)
    print(data.get(prov_name))
    return data.get(prov_name)

get_resident_Prov_on('C:\\Users\\Travis Brown\\Downloads\\address - address.csv', 'Ontario')