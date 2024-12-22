w = 1
a = 1
b = 1
with open('IP_svi.txt', 'w') as file:
    while  w < 4095:
        ip = f'1.{a}.{b}.1'
        file.write(f'interface vlan {w} \n')
        file.write(f'ip addr 1.{a}.{b}.1 255.255.255.0 \n')
        file.write('exit \n')
        b = b+1
        w = w+1
        if b == 256:
            b = 0
            a = a+1
