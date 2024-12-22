import random
w = 1
c = []
d = []
for i in range(1, 256):
    c.append(i)
    d.append(i)
d.remove(255)
new_c = []
new_d = []
ip_list = []
while  w < 4095:
    a = random.choice(c)
    b = random.choice(d)
    ip = f'172.{a}.{b}.1'
    if ip  not in ip_list :
        print(f'interface vlan {w}')
        print(f'ip addr 172.{a}.{b}.1 255.255.255.0 ')
        print('exit')
        w = w+1
    ip_list.append(ip)
print(len(new_c))
print(len(new_d))


