class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        if self.ast[0] == 'PRINT':
            message = self.ast[1].strip('"')
            asm_code = f"""
section .data
    msg db '{message}', 0

section .text
    global _start

_start:
    ; sys_write (stdout)
    mov rax, 0x2000004  ; syscall number for sys_write
    mov rdi, 1          ; file descriptor (stdout)
    lea rsi, [rel msg]  ; address of the message
    mov rdx, {len(message)}  ; length of the messagrm aue
    syscall

    ; sys_exit
    mov rax, 0x2000001  ; syscall number for sys_exit
    xor rdi, rdi        ; exit code 0
    syscall
"""
            return asm_code
