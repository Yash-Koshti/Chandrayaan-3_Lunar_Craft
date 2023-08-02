import unittest
from MoveSpaceCraft import *

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.shuttle = Spacecraft()

    def test_forward_and_backward(self):
        commands = ['f', 'b', 'f', 'f']
        self.assertEqual(self.shuttle.Forward_and_Backward(commands), [0, 2, 0], "Test Forward & Backward failed!")

# unittest.main()
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))