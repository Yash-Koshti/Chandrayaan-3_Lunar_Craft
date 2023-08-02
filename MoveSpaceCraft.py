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
                if self.pos[3] in ['N', 'E', 'S', 'W']:
                    cur_face += 1
                    if cur_face > 3:
                        cur_face = 0
                    self.pos[3] = direction[cur_face]
                elif self.pos[3] in ['U', 'D']:
                    self.pos[3] = 'E'
            elif c == 'l': #rotate anti-clockwise
                if self.pos[3] in ['N', 'E', 'S', 'W']:
                    cur_face -= 1
                    if cur_face < 0:
                        cur_face = 3
                    self.pos[3] = direction[cur_face]
                elif self.pos[3] in ['U', 'D']:
                    self.pos[3] = 'W'
        return self.pos

    def Up_and_Down(self, commands: list):
        for c in commands:
            c = str(c).lower()
            if c == 'u':
                if self.pos[3] in ['N', 'E', 'S', 'W']:
                    self.pos[3] = 'U'
                elif self.pos[3] == 'U':
                    self.pos[3] = 'N'
                else:
                    self.pos[3] = 'N'
            elif c == 'd':
                if self.pos[3] in ['N', 'E', 'S', 'W']:
                    self.pos[3] = 'D'
                elif self.pos[3] == 'D':
                    self.pos[3] = 'S'
                else:
                    self.pos[3] = 'S'
        return self.pos

    def Execute_all_commands(self, commands: list):
        for c in commands:
            c = str(c).lower()
            if c in ['f', 'b']:
                self.Forward_and_Backward(c)
            elif c in ['l', 'r']:
                self.Left_and_Right(c)
            elif c in ['u', 'd']:
                self.Up_and_Down(c)
        return self.pos
