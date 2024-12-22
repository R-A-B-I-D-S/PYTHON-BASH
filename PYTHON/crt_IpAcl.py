w = 1
a = 1
b = 1
with open('IP_acl.txt', 'w') as file:
    file.write(f'ip access-list standard S01 \n')
    while  w < 3001:
        ip = f'1.1.{a}.{b}'
        file.write(f'permit host-source {ip} \n')
        b = b+1
        w = w+1
        if b == 256:
            b = 0
            a = a+1
    file.write('exit \n')
file.close()
