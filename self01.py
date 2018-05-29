class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5

def main():
	p1 = Point(6,8)
	dist = p1.distance()
	print("distance: ", dist)

	print("type(Point.distance): ", type(Point.distance)) 
	print("type(p1.distance): ", type(p1.distance)) 

if __name__ == '__main__':
	main()