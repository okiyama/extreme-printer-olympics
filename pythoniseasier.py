import numpy as np
from PIL import Image
import random
import math
from easing_functions import *

class ImageWriter:
	def __init__(self, width, height, fibonacci = False):
		self.width = width
		self.height = height
		self.fibonacci = fibonacci


	def writeImage(self):
		finalImage = np.full((self.width, self.height, 3), [255], dtype=np.uint8)

		prev_line_width = 1
		line_width = 1
		curr_line_progress = 1
		for row in range(self.width):
			if row % 100 == 0:
				print("processed row " + str(row) + " of " + str(self.width) + " percent: " + str(100.0 * float(row)/float(self.width)))
			for col in range(self.height):
				if curr_line_progress > 0:
					curr_line_progress -= 1
				else:
					finalImage[row][col] = np.array([0, 0, 0], dtype=np.uint8)
					new_line_width = (line_width + prev_line_width) if self.fibonacci else line_width + 1
					prev_line_width = line_width
					line_width = new_line_width
					curr_line_progress = line_width

		fib_str = "_fib" if self.fibonacci else ""
		print("writing image, this may take a lil while...")
		to_write = Image.fromarray(finalImage, 'RGB')
		if(self.width < 612):
			to_write = to_write.resize((792, 612))
		to_write.save("output_" + str(self.width) + "_" + str(self.height) + fib_str + ".pdf")

if __name__ == '__main__':
	start = 1
	end = 450
	num_pages = 25
	quad_func = CubicEaseIn(start=start, end=end, duration=num_pages)


	x = np.arange(0, num_pages + 1, 1)
	y0 = list(map(math.floor, map(quad_func, x)))
	print(str(y0))
	#values = range(start, end, math.floor((end - start) / num_pages))
	for scale in y0:
		print(str(scale))
		writer = ImageWriter(math.floor(8.5 * scale), math.floor(11 * scale), False)
		writer.writeImage()