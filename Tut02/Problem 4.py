length_1 = float(input('Enter length for triangle #1: '))
width_1 = float(input('Enter width for triangle #1: '))

area_1 = length_1 * width_1

length_2 = float(input('Enter length for triangle #2: '))
width_2 = float(input('Enter width for triangle #2: '))

area_2 = length_2 * width_2

if area_1 > area_2:
    print('Rectangle #1 has the greater area than Rectangle #2', area_1 - area_2, 'm2')
elif area_2 > area_1:
    print('Rectangle #2 has the greater area than Rectangle #1', area_2 - area_1, 'm2')
elif area_1 == area_2:
    print('Rectangles #1 and #2 have the SAME area at', area_1, 'm2')
