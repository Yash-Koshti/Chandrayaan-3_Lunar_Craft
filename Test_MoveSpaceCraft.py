import unittest
from MoveSpaceCraft import *

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.shuttle = Spacecraft()

    def test_forward_and_backward(self):
        commands = ['f', 'b', 'f', 'f']
        self.assertEqual(self.shuttle.Forward_and_Backward(commands), [0, 2, 0, 'N'], "Test Forward & Backward failed!")
    
    def test_left_and_right(self):
        commands = ['r', 'l', 'l', 'l']
        self.assertEqual(self.shuttle.Left_and_Right(commands), [0, 0, 0, 'S'], "Test Left & Right failed!")

    def test_up_and_down(self):
        commands = ['d', 'u', 'd', 'd', 'u']
        self.assertEqual(self.shuttle.Up_and_Down(commands), [0, 0, 0, 'U'], "Test Up & Down failed!")

# unittest.main()
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))