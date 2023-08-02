class Spacecraft:
    def __init__(self) -> None:
        self.pos = [0, 0, 0]
        self.facing = 'N'
    
    def Forward_and_Backward(self, commands: list):
        for c in commands:
            c = str(c).lower()
            if c == 'f' or c == 'b':
                if self.facing == 'E':
                    self.pos[0] += 1
                elif self.facing == 'W':
                    self.pos[0] -= 1
                if self.facing == 'N':
                    self.pos[1] += 1
                if self.facing == 'S':
                    self.pos[1] -= 1
                if self.facing == 'U':
                    self.pos[2] += 1
                if self.facing == 'D':
                    self.pos[2] -= 1

        return self.pos
