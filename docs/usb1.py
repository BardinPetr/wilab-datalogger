import time

import pyshark

AC_GREY = "\033[0;37m"
AC_RED = "\033[0;31m"
AC_GREEN = "\033[0;32m"
AC_BLUE = "\033[1;34m"
AC_END = "\033[0m"
AC_LGREEN = "\033[1;32m"
AC_YELLOW = "\033[1;33m"

capture = pyshark.LiveCapture(interface='usbmon1')

messages = {
    'I': {},
    'O': {}
}
messages_ready = []

opcodes = {
    0x0a: (f'{AC_RED}CONF{AC_END}', lambda x: (bin(x[0] >> 4), x[0] & 0xF, x[1:3].hex(), hex(x[3]))),
    0x2a: (f'{AC_RED}WRCF{AC_END}', lambda x: x[0]),
    0x14: (f'{AC_YELLOW}0X14{AC_END}', lambda x: x[0]),
    0x1c: (f'{AC_GREEN}RDFQ{AC_END}', lambda x: f"{x[0]:x}"),
    0x22: (f'RSFQ', lambda x: f"{x[0]:x}"),
    0x03: (f'{AC_BLUE}RDVO{AC_END}', lambda x: f"{x[0]:x}"),
    0x07: (f'RSTC', lambda x: 'C0 0x07'),
    0x1f: (f'RSTC', lambda x: 'C1 0x1f'),
    0x09: (f'{AC_LGREEN}RDCN{AC_END}', lambda x: 'C0 0x09'),
    0x1e: (f'{AC_LGREEN}RDCN{AC_END}', lambda x: 'C1 0x1e'),
}
ignored = {
    0x03, 0x14, 0x09, 0x1e
}

for src in capture.sniff_continuously():
    p = src.usb

    endpoint = 'I' if p.endpoint_address.hex_value == 0x81 else 'O'
    direction = 'S' if p.urb_type.hex_value == 0x53 else 'C'
    urb_id = p.urb_id

    data = None
    try:
        data = src.DATA.usbhid_data.binary_value
        data = data[:16]
    except:
        pass

    # print(endpoint, direction, data is not None)

    if endpoint == 'I':  # read request
        if direction == 'S':
            messages[endpoint][urb_id] = data
        elif direction == 'C' and urb_id in messages[endpoint]:
            messages_ready.append((endpoint, messages[endpoint].pop(urb_id), data))
            # print(messages_ready[-1])
    else:  # write
        if direction == 'S' and data is not None:
            # used.add(data)
            # print(f"WRITE {int(time.time())} {data.hex()} {data}")
            opcode = data[0]
            data = data[1:]
            if opcode not in ignored:
                if opcode not in opcodes:
                    print(f"!!{opcode:x} {data.rstrip()[:7].hex()}")
                else:
                    op, fx = opcodes[opcode]
                    print(f"{op} {fx(data)}")

            messages_ready.append((endpoint, data))
