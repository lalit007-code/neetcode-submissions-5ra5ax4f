class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        self.mini.append(float('inf'))
    def push(self, val: int) -> None:
        if self.mini and self.mini[-1] >= val:
            self.mini.append(val)
            # print(self.mini)
        self.stack.append(val)
        # print(self.mini)

    def pop(self) -> None:
        if self.stack and self.mini and self.stack[-1] == self.mini[-1]:
            self.mini.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # print("inside getmin",self.mini)
        return self.mini[-1]
        
