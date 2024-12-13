import sys
import struct
import xml.etree.ElementTree as ET

def parse_instruction(line):
    parts = line.strip().split()
    if not parts:
        return None
    mnemonic, *operands = parts
    if mnemonic == 'LOAD':
        A = 7
        B = int(operands[0])
        instruction = (A << 27) | (B & 0x7FFFFFF)
    elif mnemonic == 'READ':
        A = 5
        B = int(operands[0])
        instruction = (A << 27) | (B & 0x3FFFFFFF)
    elif mnemonic == 'WRITE':
        A = 27
        B = int(operands[0])
        instruction = (A << 27) | (B & 0x3FFFFFFF)
    elif mnemonic == 'EQ':
        A = 19
        B = int(operands[0])
        instruction = (A << 27) | (B & 0x3FFFFFFF)
    else:
        raise ValueError(f"Unknown instruction: {mnemonic}")
    return struct.pack('>I', instruction) + b'\x00'

def assemble(input_file, output_file, log_file):
    with open(input_file, 'r') as infile, open(output_file, 'wb') as outfile:
        root = ET.Element("Instructions")
        for line in infile:
            instruction = parse_instruction(line)
            if instruction:
                outfile.write(instruction)
                ET.SubElement(root, "Instruction", hex=instruction.hex())

        tree = ET.ElementTree(root)
        tree.write(log_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python assembler.py <input_file> <output_file> <log_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    assemble(input_file, output_file, log_file)
