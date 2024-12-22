x = 1

with open('crt_vrf.txt', 'w') as file:
    while x < 301:
        file.write(f'ip vrf {x} \n')
        file.write(f'exit \n')
        x = x+1
file.close()
