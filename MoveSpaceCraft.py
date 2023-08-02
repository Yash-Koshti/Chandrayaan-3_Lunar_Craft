class Spacecraft:
    def __init__(self) -> None:
        self.pos = [0, 0, 0, 'N']
    
    def Forward_and_Backward(self, commands: list):
        for c in commands:
            c = str(c).lower()
            if c == 'f':
                if self.pos[3] == 'E':
                    self.pos[0] += 1
                elif self.pos[3] == 'W':
                    self.pos[0] -= 1
                if self.pos[3] == 'N':
                    self.pos[1] += 1
                if self.pos[3] == 'S':
                    self.pos[1] -= 1
                if self.pos[3] == 'U':
                    self.pos[2] += 1
                if self.pos[3] == 'D':
                    self.pos[2] -= 1
            elif c == 'b':
                if self.pos[3] == 'E':
                    self.pos[0] -= 1
                elif self.pos[3] == 'W':
                    self.pos[0] += 1
                if self.pos[3] == 'N':
                    self.pos[1] -= 1
                if self.pos[3] == 'S':
                    self.pos[1] += 1
                if self.pos[3] == 'U':
                    self.pos[2] -= 1
                if self.pos[3] == 'D':
                    self.pos[2] += 1

        return self.pos

    def Left_and_Right(self, commands: list):
        direction = ['N', 'E', 'S', 'W']
        cur_face = direction.index(self.pos[3])
        for c in commands:
            c = str(c).lower()
            if c == 'r': #rotate clockwise
                cur_face += 1
            elif c == 'l': #rotate anti-clockwise
                cur_face -= 1
        self.pos[3] = direction[cur_face]
        return self.pos