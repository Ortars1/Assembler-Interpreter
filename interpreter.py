import sys
import struct
import xml.etree.ElementTree as ET

MEMORY_SIZE = 1024

class VirtualMachine:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.acc = 0

    def load(self, value):
        self.acc = value

    def read(self, address):
        self.acc = self.memory[address]

    def write(self, address):
        self.memory[address] = self.acc

    def eq(self, address):
        if address < 0 or address >= len(self.memory):
            raise ValueError(f"Invalid memory address: {address}")
        self.acc = 1 if self.acc == self.memory[address] else 0

    def execute(self, command):
        opcode = (command >> 27) & 0x1F
        operand = command & 0x7FFFFFF

        print(f"Executing: opcode={opcode}, operand={operand}")

        if opcode == 7:
            self.load(operand)
        elif opcode == 5:
            self.read(operand)
        elif opcode == 27:
            self.write(operand)
        elif opcode == 19:
            self.eq(operand)
        else:
            raise ValueError("Unknown opcode")

    def run(self, input_file, result_file, memory_range):
        with open(input_file, 'rb') as f:
            while True:
                bytes_data = f.read(5)
                if not bytes_data:
                    break
                command, _ = struct.unpack('>I1B', bytes_data)
                self.execute(command)

        root = ET.Element("Memory")
        start, end = memory_range
        for i in range(start, end):
            ET.SubElement(root, "Cell", address=str(i), value=str(self.memory[i]))

        tree = ET.ElementTree(root)
        tree.write(result_file)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python interpreter.py <input_file> <result_file> <start_address> <end_address>")
        sys.exit(1)

    input_file = sys.argv[1]
    result_file = sys.argv[2]
    start_address = int(sys.argv[3])
    end_address = int(sys.argv[4])

    vm = VirtualMachine()
    vm.run(input_file, result_file, (start_address, end_address))
