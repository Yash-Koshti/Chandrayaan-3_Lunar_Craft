import unittest
from MoveSpaceCraft import Spacecraft

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.shuttle = Spacecraft(0, 0, 0)

    def test_forward(self):
        self.assertEqual(self.shuttle.Forward(), [0, 1, 0, 'N'], "Test Forward failed!")
    
    def test_backward(self):
        self.assertEqual(self.shuttle.Backward(), [0, -1, 0, 'N'], "Test Backward failed!")
    
    def test_left(self):
        self.assertEqual(self.shuttle.Left(), [0, 0, 0, 'W'], "Test Left failed!")
    
    def test_right(self):
        self.assertEqual(self.shuttle.Right(), [0, 0, 0, 'E'], "Test Right failed!")

    def test_up(self):
        self.assertEqual(self.shuttle.Up(), [0, 0, 0, 'U'], "Test Up failed!")
    
    def test_down(self):
        self.assertEqual(self.shuttle.Down(), [0, 0, 0, 'D'], "Test Down failed!")

    def test_execute_all_commands(self):
        commands = ['f', 'r', 'u', 'b', 'l']
        self.assertEqual(self.shuttle.Execute_all_commands(commands), [0, 1, -1, 'W'], "Test Execute all commands failed!")

    def test_invalid_inputs_in_execute_all_commands(self):
        # Here only one command is correct which is Left
        commands = ['a', 'B', 'F', 'l', '1', 1, True, [1, 'r'], 1.2]
        self.assertEqual(self.shuttle.Execute_all_commands(commands), [0, 0, 0, 'W'], "Test Invalid inputs in execute all commands failed!")

    def test_all_individual_methods_with_new_instance(self):
        temp_shuttle = Spacecraft(1, 5, -9, 'E')
        temp_shuttle.Down()
        temp_shuttle.Forward()
        temp_shuttle.Left()
        temp_shuttle.Backward()
        temp_shuttle.Right()
        temp_shuttle.Up()
        self.assertEqual(temp_shuttle.pos, [2, 5, -10, 'U'], "Test all individual methods with new instance failed!")

if __name__ == "__main__":
    unittest.main(exit=False)
