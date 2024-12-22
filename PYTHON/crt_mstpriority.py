i = 49

with open('mstp_priority.txt', 'w') as file:
    while i < 65:
        file.write(f'spanning-tree mst {i} priority 16384 \n')
        i = i+1
file.close()
