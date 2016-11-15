"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given set of points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?
"""
class solution(object):
	"""docstring for solution"""
	def reflex(self, points):
		# find max x and min x
		max_x = -100
		max_x_set = []
		min_x = 100
		min_x_set = []

		for point in points:
			if point[0] > max_x:
				max_x = point[0]
				max_x_set = point

			if point[0] < min_x:
				min_x = point[0]
				min_x_set = point

		min_x_set_ref = [min_x_set[0], -min_x_set[1]]
		max_x_set_ref = [max_x_set[0], -max_x_set[1]]

		try: 
			# here if the two lines are parallel, return false
			k1 = float((max_x_set[1] - min_x_set_ref[1])) / (max_x_set[0] - min_x_set_ref[0])
			k2 = float((min_x_set[1] - max_x_set_ref[1])) / (min_x_set[0] - max_x_set_ref[0])


			b1 = max_x_set[1] - k1 * float(max_x_set[0])
			b2 = min_x_set[1] - k2 * float(min_x_set[0])

			x_intercept = (b2-b1) / (k1-k2)
		except:
			return False 
		y_intercept = k1 * x_intercept + b1

		for point in points:
			y1 = k1 * point[0] + b1
			y2 = k2 * point[0] + b2

			if (point[1] < y_intercept):
				return False
			if (y1 != point[1]) and (y2 != point[1]):
				return False
		return True

if __name__ == '__main__':
	print solution().reflex([[1,1],[-1, 1], [2,2], [-2, 2], [-3, -3]])