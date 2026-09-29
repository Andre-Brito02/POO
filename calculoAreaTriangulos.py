import math

class Triangle:
    def calculo_area(self, a,b,c):
        p = (a+b+c)/2.0
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

x = Triangle()
areaX = x.calculo_area(3, 4, 5)
y = Triangle()
areaY = y.calculo_area(7.5, 4.5, 4.02)

print(f'Área X: {areaX:.4f}\nÁrea Y: {areaY:.4f}')
print('Larger Area: X' if areaX > areaY else 'Larger Area: Y')