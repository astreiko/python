#������� 10
import numpy

s = 7.4
m = 10.0
f = 3.2 * (10 ** 4)
k = (4.0, 0.5, 8.0)

print('���� for')
for j in range(len(k)):
    y = s / numpy.log(5.2 * f) / (numpy.e**(-5) + 2)
    v = (1 + m * y - m * k[j]) / numpy.log(y)
    print('��� k = ', k[j], ' v = ', v)

k = 0
print('\n���� while')
while k <= 4:
    y = s / numpy.log(5.2 * f) / (numpy.e**(-5) + 2)
    v = (1 + m * y - m * k) / numpy.log(y)
    print('��� k = ', k, ' v = ', v)
    k += 0.5

k = (0.9, 11.0, 0.5)
print('\n������� ����')
for j in range(len(k)):
    m = 0.3
    while m <= 0.7:
        y = s / numpy.log(5.2 * f) / (numpy.e ** (-5) + 2)
        v = (1 + m * y - m * k[j]) / numpy.log(y)
        print('��� k = ', k[j], ' � m = ', m, ' v = ', v)
        m += 0.1