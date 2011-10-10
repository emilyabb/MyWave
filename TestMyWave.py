


import unittest
from MyWave import MyWave


class TestMyWave(unittest.TestCase):

    def setUp(self):
        
        self.testmw = MyWave()


    def tearDown(self):

        pass


    def test_load(self):

        self.testmw.load("failure1.wav")
        tmp_wave = wave.open("failure1.wav")
        assert self.testmw.wave == tmp_wave
        assert self.testmw.number_channels == tmp.wave.getnchannels()
        assert self.testmw.sample_width == tmp_wave.getsampwidth()

    def test_get_max_frame(self):
        max_frame = self.testmw.get_max_frame()






if __name__ == '__main__':
    unittest.main()
