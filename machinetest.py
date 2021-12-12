# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

MAX_VALUE = int(math.pow(2, 20))

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            raise MachineError("not enough elements in stack")
    return inner_function

class MachineError(Exception):
    pass

class Machine:
    stack = []

    def push(self, number):
        number = int(number)
        if number >= 0 and number < MAX_VALUE:
            self.stack.append(number)
        else:
            raise MachineError("Not a valid integer")

    @exception_handler
    def pop(self):
        self.stack.pop()


    @exception_handler
    def dup(self):
        self.stack.append(self.stack[-1])

    @exception_handler
    def add(self):
        top_stack = self.stack.pop()
        second_top_stack = self.stack.pop()
        sum = top_stack + second_top_stack
        if sum > MAX_VALUE:
            raise MachineError("Too big number")
        self.stack.append(sum)

    @exception_handler
    def subtract(self):
        top_stack = self.stack.pop()
        second_top_stack = self.stack.pop()
        diff = top_stack - second_top_stack
        if diff < 0:
            raise MachineError("Negative subtraction result!")
        self.stack.append(diff)
    
    def action_selector(self, command):
        action_map = {
            "POP": self.pop,
            "DUP": self.dup,
            "+": self.add,
            "-": self.subtract
        }
        try:
            action_map[command]()
        except KeyError:
            return self.push(command)

def solution(S) -> int:
    # write your code in Python 3.6
    machine = Machine()
    S_command_list = S.split(" ")
    try:
        for command in S_command_list:
            machine.action_selector(command)
    except MachineError as e:
        print(f"Exception error message: {e}")
        return -1
    return machine.stack.pop()
        
if __name__ == '__main__':
    example1 = "1048575 DUP +"
    print(solution(example1))