import  random
hex_list = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
mac_list = []
a = 1100
with open('list_MacAcl.txt', 'w') as file:
    while a < 1200:
        c = random.choice(hex_list)
        d = random.choice(hex_list)
        e = random.choice(hex_list)
        f = random.choice(hex_list)
        mac1 = f'00:11:01:00:{e}{f}:{c}{d}'
        mac2 = f'00:12:01:00:{e}{f}:{c}{d}'
        if mac1 or mac2 not in mac_list:
            file.write(f'access-list {a} deny host-source-mac {mac1} host-destination-mac {mac2} \n')
        mac_list.append(mac1)
        mac_list.append(mac2)
        a = a+1
file.close()



