

"""
Lots of code from http://personalwebs.coloradocollege.edu/~mwhitehead/courses/2011/CP215_ApplicationDesign/Assignments/6/6.html
"""
__author__ = Emily

import wave, struct, sys

def processFrames(wave_read):
    """ read in the frames, structing the bytes into a list of shorts"""
    frames = []
    frame_bytes = wave_read.readframes(2)

    while frame_bytes:
        frame_value, = struct.unpack("h",frame_bytes)
        frames.append(frame_value)
        frame_bytes = wave_read.readframes(2)
    return frames


class MyWave:
    """
    MyWave class stores a wave_read object and some of its attributes
    """

    def __init__(self):
        '''Initialize a new Wave object.  Use load to read in an existing file.'''
        self.MAX_FRAME_VALUE = 65536
        self.wave = None
        self.number_channels = 1
        self.sample_width = 16
        self.sampling_rate = 48000
        self.number_frames = 0
        self.frames = []

    def load(self, wavfilename):
        '''Load in a wave file given by wavfilename.'''
        self.wave = wave.open(wavefilename, 'r')
        self.number_channels = self.wave.getnchannels()
        self.sample_width = self.wave.getsampwidth()
        self.sampling_rate = self.wave.getframerate()
        self.number_frames = self.wave.getnframes()
        self.frames = processFrames(wave)
        self.MAX_FRAME_VALUE = 2**(self.sample_width-1)

    def get_max_frame(self):
        '''Find and return the most extreme wave value in the file.'''
        biggest_index = 0
        for i in range(0, self.number_frames):
            if abs(self[i] > self.frames[biggest_index]):
                biggest_index = i
        return self.frames[biggest_index] 

    def adjust_volume(self, multiplier):
        """increase or decrease the volume by the given factor"""

        for i in range(len(self.frames)):
            new_value = int(self.frames[i] * multiplier)
            if new_value > self.MAX_FRAME_VALUE:
                new_value = self.MAX_FRAME_VALUE
            self.frames[i] = new_value
         
    def normalize_volume(self):
        """ """
        max_amp = self.get_max_frame()
        mult_factor = self.MAX_FRAME_VALUE / max_amp     

        self.adjust_volume(mult_factor)

    def save(self, filename):
        """Takes the current wave and writes it to a new file"""

        wave_w = wave.open(filename, 'w')
        wave_w.setparams(self.wave.getparams())

        for frame in self.frames:  #write frame data
            data = struct.pack("<h", frame)
            wave_w.writeframes(data)

        f.close()
        

#myWave = wave.open(wavefilename, 'r')      #open Wave_read object
