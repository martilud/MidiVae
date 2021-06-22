import pypianoroll
import string
import numpy as np
import matplotlib.pyplot as plt
mid = pypianoroll.read('The Legend of Zelda Twilight Princess - Midnas Lament.mid')
mid.binarize()
print(mid.resolution)
mid.set_resolution(4)
pypianoroll.write("test.mid", mid)

