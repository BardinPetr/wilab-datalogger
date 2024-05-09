import scapy
from scapy.layers.usb import USBpcap
from scapy.utils import rdpcap

msgs = []
opened = {
    'I': [],
    'O': []
}

data = rdpcap("/home/petr/wi3.pcap")
for i in data:
    msg = i.load
    endpoint = 'I' if msg[10] == 0x81 else 'O'
    direction = 'S' if msg[8] == 0x53 else 'R'

    payload = msg[64:]
    payload = payload.strip(b'\x00')
    # if not payload: continue

    # print(f"{endpoint}{direction}")

    if direction == 'S':
        opened[endpoint].append(payload)
    else:
        if opened[endpoint]:
            msgs.append((endpoint, opened[endpoint].pop(), payload))

    # print(endpoint, list(payload), payload)


cmds = []
cmd_map = {}
cmd_map_cnt = {}
unhandled = []

for i in range(len(msgs)):
    ep, req, res = msgs[i]
    if ep == 'I':
        cmd = msgs[i - 1][1]
        cmds.append((cmd, res))
        cmd_map[cmd] = cmd_map.get(cmd, set())
        cmd_map[cmd].add(res)
    else:
        unhandled.append(req)
        cmd_map_cnt[req] = cmd_map_cnt.get(req, 0) + 1


for r, s in cmds:
    print(f"{r.hex():010} {s.hex():010}")


print("#" * 10)
print("all write commands cnt")
print("#" * 10)

for n, c in sorted(cmd_map_cnt.items(), key=lambda x: x[0]):
    print(f"{c}\t{n.hex():010}\t{n}")

print("#" * 10)
print("no-response commands")
print("#" * 10)

handled = set(cmd_map.keys())
# print(handled)
for i in unhandled:
    if i in handled: continue
    print(f"{i.hex():010}", i)

print("#" * 10)
print("#" * 10)

for i, j in cmd_map.items():
    print(i.hex(), ": ")
    for k in j:
        print(f"{k.hex():016}", k)

    print("#" * 20)


"""

"""