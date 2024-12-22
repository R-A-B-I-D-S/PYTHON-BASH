w = 1
a = 1
b = 1
with open('IP_aclext.txt', 'w') as file:
    file.write(f'ip access-list extended S01 \n')
    while  w < 2001:
        ip = f'1.1.{a}.{b}'
        ip2 = f'2.2.{a}.{b}'
        file.write(f'permit ip host-source {ip} host-destination {ip2} \n')
        b = b+1
        w = w+1
        if b == 256:
            b = 0
            a = a+1
    file.write('exit \n')
file.close()