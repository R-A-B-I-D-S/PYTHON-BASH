i = 1
a = 10
b = 11
with open('crt_mstp.txt', 'w') as file:
    file.write('spanning-tree mst configuration \n')
    file.write(f'name SW \n')
    while i < 65:
        file.write(f'instance {i} vlan {a}-{b} \n')
        i = i+1
        a = a+2
        b = b+2
file.close()
