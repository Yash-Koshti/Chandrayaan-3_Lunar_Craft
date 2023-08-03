class Spacecraft:
    # This static variable is used for reference of directions. The directions are in clockwise manner
    __direction_NESW = ['N', 'E', 'S', 'W']
    __direction_UD = ['U', 'D']
    
    def __init__(self, x: int, y: int , z: int, d: str = 'N') -> None:
        """Takes x, y and z as arguments and d (Direction) is optional and by default North"""
        self.pos = [x, y, z, d]
    
    def Forward(self) -> list:
        """It moves the spacecraft one step forward in the current facing direction"""

        # The direction in which the spacecraft is facing currently
        facing_into = self.pos[3]
        
        # Updates the x or y or z coordinates according to which the spacecraft is facing
        if facing_into == 'E':
            self.pos[0] += 1
        elif facing_into == 'W':
            self.pos[0] -= 1
        elif facing_into == 'N':
            self.pos[1] += 1
        elif facing_into == 'S':
            self.pos[1] -= 1
        elif facing_into == 'U':
            self.pos[2] += 1
        elif facing_into == 'D':
            self.pos[2] -= 1

        return self.pos
    
    def Backward(self) -> list:
        """It moves the spacecraft one step backward in the current facing direction"""
        
        # The direction in which the spacecraft is facing currently
        facing_into = self.pos[3]
        
        # Updates the x or y or z coordinates according to which the spacecraft is facing
        if facing_into == 'E':
            self.pos[0] -= 1
        elif facing_into == 'W':
            self.pos[0] += 1
        elif facing_into == 'N':
            self.pos[1] -= 1
        elif facing_into == 'S':
            self.pos[1] += 1
        elif facing_into == 'U':
            self.pos[2] -= 1
        elif facing_into == 'D':
            self.pos[2] += 1

        return self.pos
    
    def Right(self) -> list:
        """It rotates the spacecraft 90 degrees into its right direction from its current facing direction"""

        # The direction in which the spacecraft is facing currently
        facing_into = self.pos[3]
        
        # Taking the index of the current direction according to the direction list
        if facing_into in Spacecraft.__direction_NESW:
            cur_face = Spacecraft.__direction_NESW.index(facing_into)
            cur_face += 1
            
            # If the index goes out of range of directions list, then it will reset it to zero
            if cur_face > 3:
                cur_face = 0
            
            # Getting the current facing direction after turning
            facing_into = Spacecraft.__direction_NESW[cur_face]
        elif facing_into in Spacecraft.__direction_UD:
            facing_into = 'E'
        
        # Updating the direction in current list of position
        self.pos[3] = facing_into

        return self.pos
    
    def Left(self) -> list:
        """It rotates the spacecraft 90 degrees into its left direction from its current facing direction"""

        # The direction in which the spacecraft is facing currently
        facing_into = self.pos[3]
        
        # Taking the index of the current direction according to the direction list
        if facing_into in Spacecraft.__direction_NESW:
            cur_face = Spacecraft.__direction_NESW.index(facing_into)
            cur_face -= 1

            # If the index goes out of range of directions list, then it will reset it to three
            if cur_face < 0:
                cur_face = 3
            
            # Getting the current facing direction after turning
            facing_into = Spacecraft.__direction_NESW[cur_face]
        elif facing_into in Spacecraft.__direction_UD:
            facing_into = 'W'

        # Updating the direction in current list of position
        self.pos[3] = facing_into

        return self.pos

    def Up(self) -> list:
        """It rotates the spacecraft into the upward direction"""

        facing_into = self.pos[3]
        
        # It will face Up if facing NESW, but face North if facing UD
        if facing_into in Spacecraft.__direction_NESW:
            facing_into = 'U'
        elif facing_into in Spacecraft.__direction_UD:
            facing_into = 'N'
        
        self.pos[3] = facing_into
        return self.pos

    def Down(self) -> list:
        """It rotates the spacecraft into the downward direction"""

        facing_into = self.pos[3]
        
        # It will face Up if facing NESW, but face North if facing UD
        if facing_into in Spacecraft.__direction_NESW:
            facing_into = 'D'
        elif facing_into in Spacecraft.__direction_UD:
            facing_into = 'S'
        
        self.pos[3] = facing_into
        return self.pos

    def Execute_all_commands(self, commands: list) -> list:
        """It will execute all the commands provided in a list of characters.
        The commands are...
        f - move Forward
        b - move Backward
        l - rotate Left
        r - rotate Right
        u - rotate Up
        d - roate Down"""

        for c in commands:
            c = str(c).lower()
            if c == 'f':
                self.Forward()
            elif c == 'b':
                self.Backward()
            elif c == 'l':
                self.Left()
            elif c == 'r':
                self.Right()
            elif c  == 'u':
                self.Up()
            elif c  == 'd':
                self.Down()
                
        return self.pos
