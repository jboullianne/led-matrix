class LEDText:

	def __init__(self, x, y, rgb, text, matrix):
		self.x = x
		self.y = y
		self.rgb = rgb
		self.text = text
		self.matrix = matrix
		self.matrix.obj_list += [self]

	def draw(self):
		x = self.x
		y = self.y

		for let in self.text.lower():
			letter = self.getLetter(let)
			offset_y = 0
			for row in letter:
				offset_x = 0
				for pix in row:
					if pix:
						self.matrix.setPixel(x + offset_x, y + offset_y, self.rgb)
					offset_x += 1
				offset_y += 1
			x += 5

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setRGB(self, r, g, b):
		self.rgb = (r, g, b)

	def destroy(self):
		self.matrix.obj_list.remove(self)

	def getLetter(self, let):

		letters =	{ 	'a' :  	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[1,1,1,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0]],
						'b' :	[	[1,1,1,0,0],
									[1,0,0,1,0],
									[1,1,1,0,0],
									[1,0,0,1,0],
									[1,1,1,0,0]],
						'c' :	[	[0,1,1,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[0,1,1,0,0]],
						'd' :	[	[1,1,1,0,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,1,1,0,0]],
						'e' :	[	[1,1,1,1,0],
									[1,0,0,0,0],
									[1,1,1,0,0],
									[1,0,0,0,0],
									[1,1,1,1,0]],
						'f' :	[	[1,1,1,1,0],
									[1,0,0,0,0],
									[1,1,1,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0]],
						'g' :	[	[0,1,1,1,0],
									[1,0,0,0,0],
									[1,0,1,1,0],
									[1,0,0,1,0],
									[0,1,1,1,0]],
						'h' :	[	[1,0,0,1,0],
									[1,0,0,1,0],
									[1,1,1,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0]],
						'i' :	[	[1,1,1,0,0],
									[0,1,0,0,0],
									[0,1,0,0,0],
									[0,1,0,0,0],
									[1,1,1,0,0]],
						'j' :	[	[0,1,1,1,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[1,0,1,0,0],
									[0,1,0,0,0]],
						'k' :	[	[1,0,0,1,0],
									[1,0,1,0,0],
									[1,1,0,0,0],
									[1,0,1,0,0],
									[1,0,0,1,0]],
						'l' :	[	[1,0,0,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[1,1,1,1,0]],
						'm' :	[	[1,0,0,0,1],
									[1,1,0,1,1],
									[1,0,1,0,1],
									[1,0,0,0,1],
									[1,0,0,0,1]],
						'n' :	[	[1,0,0,1,0],
									[1,1,0,1,0],
									[1,0,1,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0]],
						'o' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[0,1,1,0,0]],
						'p' :	[	[1,1,1,0,0],
									[1,0,0,1,0],
									[1,1,1,1,0],
									[1,0,0,0,0],
									[1,0,0,0,0]],
						'q' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,1,0,0],
									[0,1,0,1,0]],
						'r' :	[	[1,1,1,0,0],
									[1,0,0,1,0],
									[1,1,1,1,0],
									[1,0,1,0,0],
									[1,0,0,1,0]],
						's' :	[	[0,1,1,1,0],
									[1,0,0,0,0],
									[1,1,1,1,0],
									[0,0,0,1,0],
									[1,1,1,0,0]],
						't' :	[	[0,1,1,1,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0]],
						'u' :	[	[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[0,1,1,1,0]],
						'v' :	[	[1,0,0,0,1],
									[1,0,0,0,1],
									[0,1,0,1,0],
									[0,1,0,1,0],
									[0,0,1,0,0]],
						'w' :	[	[1,0,0,0,1],
									[1,0,0,0,1],
									[1,0,0,0,1],
									[1,0,1,0,1],
									[0,1,0,1,0]],
						'x' :	[	[1,0,0,0,1],
									[0,1,0,1,0],
									[0,0,1,0,0],
									[0,1,0,1,0],
									[1,0,0,0,1]],
						'y' :	[	[1,0,0,0,1],
									[0,1,0,1,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0]],
						'z' :	[	[1,1,1,1,0],
									[0,0,0,1,0],
									[0,0,1,0,0],
									[0,1,0,0,0],
									[1,1,1,1,0]],
						' ' :	[	[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'-' :	[	[0,0,0,0,0],
									[0,0,0,0,0],
									[1,1,1,1,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'+' :	[	[0,0,1,0,0],
									[0,0,1,0,0],
									[1,1,1,1,1],
									[0,0,1,0,0],
									[0,0,1,0,0]],
						'=' :	[	[0,0,0,0,0],
									[1,1,1,1,0],
									[0,0,0,0,0],
									[1,1,1,1,0],
									[0,0,0,0,0]],
						'%' :	[	[1,1,0,0,1],
									[1,1,0,1,0],
									[0,0,1,0,0],
									[0,1,0,1,1],
									[1,0,0,1,1]],
						'!' :	[	[0,1,0,0,0],
									[0,1,0,0,0],
									[0,1,0,0,0],
									[0,0,0,0,0],
									[0,1,0,0,0]],
						'#' :	[	[0,1,0,1,0],
									[1,1,1,1,1],
									[0,1,0,1,0],
									[1,1,1,1,1],
									[0,1,0,1,0]],
						'$' :	[	[0,1,1,1,0],
									[1,0,1,0,0],
									[1,1,1,1,1],
									[0,0,1,0,1],
									[1,1,1,1,0]],
						'*' :	[	[1,0,1,0,1],
									[0,1,1,1,0],
									[1,1,1,1,1],
									[0,1,1,1,0],
									[1,0,1,0,1]],
						'(' :	[	[0,0,0,1,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,0,1,0]],
						')' :	[	[1,0,0,0,0],
									[0,1,0,0,0],
									[0,1,0,0,0],
									[0,1,0,0,0],
									[1,0,0,0,0]],
						'_' :	[	[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[1,1,1,1,1]],
						'"' :	[	[1,0,1,0,0],
									[1,0,1,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'/' :	[	[0,0,0,0,1],
									[0,0,0,1,0],
									[0,0,1,0,0],
									[0,1,0,0,0],
									[1,0,0,0,0]],
						'\'' :	[	[0,1,0,0,0],
									[0,1,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'<' :	[	[0,0,0,1,0],
									[0,1,1,0,0],
									[1,0,0,0,0],
									[0,1,1,0,0],
									[0,0,0,1,0]],
						'>' :	[	[1,0,0,0,0],
									[0,1,1,0,0],
									[0,0,0,1,0],
									[0,1,1,0,0],
									[1,0,0,0,0]],
						',' :	[	[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,1,0,0,0],
									[1,0,0,0,0]],
						'.' :	[	[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,1,0,0,0]],
						';' :	[	[0,0,0,0,0],
									[0,0,1,0,0],
									[0,0,0,0,0],
									[0,0,1,0,0],
									[0,1,0,0,0]],
						':' :	[	[0,0,0,0,0],
									[0,0,1,0,0],
									[0,0,0,0,0],
									[0,0,1,0,0],
									[0,0,0,0,0]],
						'[' :	[	[1,1,0,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[1,0,0,0,0],
									[1,1,0,0,0]],
						']' :	[	[0,0,1,1,0],
									[0,0,0,1,0],
									[0,0,0,1,0],
									[0,0,0,1,0],
									[0,0,1,1,0]],
						'{' :	[	[0,0,1,0,0],
									[0,1,0,0,0],
									[1,1,0,0,0],
									[0,1,0,0,0],
									[0,0,1,0,0]],
						'}' :	[	[0,0,1,0,0],
									[0,0,0,1,0],
									[0,0,0,1,1],
									[0,0,0,1,0],
									[0,0,1,0,0]],
						'|' :	[	[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0]],
						'\\' :	[	[1,0,0,0,0],
									[0,1,0,0,0],
									[0,0,1,0,0],
									[0,0,0,1,0],
									[0,0,0,0,1]],
						'~' :	[	[0,1,0,1,0],
									[1,0,1,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'`' :	[	[1,0,0,0,0],
									[0,1,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0],
									[0,0,0,0,0]],
						'?' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[0,0,1,0,0],
									[0,0,0,0,0],
									[0,0,1,0,0]],
						'1' :	[	[0,0,1,0,0],
									[0,1,1,0,0],
									[0,0,1,0,0],
									[0,0,1,0,0],
									[0,1,1,1,0]],
						'2' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[0,0,1,0,0],
									[0,1,0,0,0],
									[1,1,1,1,0]],
						'3' :	[	[1,1,0,0,0],
									[0,0,1,0,0],
									[1,1,0,0,0],
									[0,0,1,0,0],
									[1,1,0,0,0]],
						'4' :	[	[0,0,1,0,0],
									[0,1,1,0,0],
									[1,1,1,1,0],
									[0,0,1,0,0],
									[0,0,1,0,0]],
						'5' :	[	[1,1,1,1,0],
									[1,0,0,0,0],
									[0,1,1,0,0],
									[0,0,0,1,0],
									[1,1,1,0,0]],
						'6' :	[	[0,0,1,0,0],
									[0,1,0,0,0],
									[1,1,1,0,0],
									[1,0,0,1,0],
									[0,1,1,0,0]],
						'7' :	[	[1,1,1,1,0],
									[0,0,0,1,0],
									[0,0,1,0,0],
									[0,1,0,0,0],
									[1,0,0,0,0]],
						'8' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[0,1,1,0,0],
									[1,0,0,1,0],
									[0,1,1,0,0]],
						'9' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[0,1,1,1,0],
									[0,0,0,1,0],
									[0,0,0,1,0]],
						'0' :	[	[0,1,1,0,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[1,0,0,1,0],
									[0,1,1,0,0]]
					}	

		return letters[let]