import binascii
import struct

currentAddress = 0x1678f

def vm_handler(instruction, bin):
    global currentAddress
    match instruction:
        case '0x16101':
            appendedByte = f.read(1)
            currentAddress+=5
            return "pop r" + str(int.from_bytes(appendedByte)) + "(64 bit)"
        case '0x1606a':
            appendedByte = f.read(1)
            currentAddress+=5
            return "push r" + str(int.from_bytes(appendedByte)) + "(64 bit)" 
        case '0x1620a':
            currentAddress+=4
            return "push sp"
        case '0x16194':
            appendedByte = f.read(8)
            currentAddress+=12
            return "push " + str(hex(struct.unpack_from("<I", appendedByte)[0])) + "(64 bit)"
        case '0x1631f':
            currentAddress+=4
            return "sub something"
        case '0x1626c':
            currentAddress+=4
            return "pop sp"
        case '0x162b1':
            currentAddress+=4
            return "add something"
        case '0x16090':
            appendedByte = f.read(1)
            currentAddress+=5
            return "push r" + str(int.from_bytes(appendedByte)) 
        case '0x16707':
            currentAddress+=4
            return "mov somewhere"
        case '0x161b1':
            appendedByte = f.read(4)
            currentAddress+=8
            return "push " + str(hex(struct.unpack_from("<I", appendedByte)[0])) + "(32 bit)"
        case '0x16689':
            currentAddress+=4
            return "DEREF_AND_REPLACE sp (64 bit)"
        case '0x1669f':
            currentAddress+=4
            return "DEREF_AND_REPLACE sp (32 bit)"
        case '0x16481':
            currentAddress+=4
            return "or something"
        case '0x16413':
            currentAddress+=4
            return "and something"
        case '0x162c9':
            currentAddress+=4
            return "add something"
        case '0x16337':
            currentAddress+=4
            return "sub something"
        case '0x163a5':
            currentAddress+=4
            return "xor something"
        case '0x16126':
            appendedByte = f.read(1)
            currentAddress+=5
            return "pop r" + str(int.from_bytes(appendedByte)) + "(32 bit)"
        case '0x1676b':
            appendedAddy = f.read(4)
            currentAddress+=8
            return "jnz " + str(hex(struct.unpack_from("<I", appendedAddy)[0]))
        case '0x1604e':
            currentAddress+=4
            return "emulation complete"
size = 4


#valid keys: 1859, 2418, 1638, 299902, 29763, 


with open('vm_instructions.bin', 'rb') as f:
    while True:
        chunk = f.read(size)
        if not chunk:
            break;
        chunk = hex(struct.unpack_from("<I", chunk)[0])
        
        
        decompiled_instr = vm_handler(chunk, f)
        
        print(str(hex(currentAddress)) + ": "+ decompiled_instr)
        
 