class Calculate_area:
    def rectangle_area(self, w, h):
        return w * h
    
    @classmethod
    def triangle_area(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r
    
cal = Calculate_area()
cal_rec = cal.rectangle_area(5, 10)
cal_tri = Calculate_area.triangle_area(5, 10)
cal_cir = Calculate_area.circle_area(7)

print(f"Area of Rectangle: {cal_rec}")
print(f"Area of Triangle: {cal_tri}")
print(f"Area of Circle: {cal_cir}")

# Output:
#print('Test Triangle Area', Calculate_area.triangle_area(5, 10))
#print('Test Circle Area', Calculate_area.circle_area(7))
#print('Test Rectangle Area', cal.rectangle_area(5, 10))