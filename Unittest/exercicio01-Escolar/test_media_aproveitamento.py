import unittest
from media_aproveitamento import media_aproveitamento

class TestMediaAproveitamento(unittest.TestCase):
    def test_entradas_invalidas_n1(self):
        self.assertRaises(ValueError, media_aproveitamento, -1, 0, 0, 0)
    def test_entradas_invalidas_n2(self):    
        self.assertRaises(ValueError, media_aproveitamento, 0, -1, 0, 0)
    def test_entradas_invalidas_n3(self):
        self.assertRaises(ValueError, media_aproveitamento, 0, 0, -1, 0)
    def test_entradas_invalidas_me(self):
        self.assertRaises(ValueError, media_aproveitamento, 0, 0, 0, -1)
    def test_conceito_A(self):
        self.assertEqual(media_aproveitamento(10, 10, 10, 10), 'A')
    def test_conceito_A2(self):
        self.assertEqual(media_aproveitamento(9, 9, 9, 9), 'A')
    def test_conceito_B(self):
        self.assertEqual(media_aproveitamento(7.5,7.5, 7.5, 7.5), 'B')
    def test_conceito_C(self):
        self.assertEqual(media_aproveitamento(6, 6, 6, 6), 'C')
    def test_conceito_D(self):
        self.assertEqual(media_aproveitamento(4, 4, 4, 4), 'D')
    

if __name__ == '__main__':
    unittest.main()