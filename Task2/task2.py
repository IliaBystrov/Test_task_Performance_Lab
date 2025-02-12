import sys

if len(sys.argv) == 3:
    points = []
    circle = ''

    with open(sys.argv[1], 'r') as f_points:
        for line in f_points:
            x, y = line.split(' ')
            points.append({'x': float(x), 'y': float(y)})

    with open(sys.argv[2], 'r') as f_circle:
        lines = f_circle.readlines()
        x, y = lines[0].split(' ')
        circle = {'x': float(x), 'y': float(y), 'r': float(lines[1])}

    for point in points:
        s = ((point['x'] - circle['x'])**2) + ((point['y'] - circle['y'])**2)
        if s == circle['r']**2:
            print(0)
        elif s < circle['r']**2:
            print(1)
        elif s > circle['r']**2:
            print(2)
else:
    print('Нужно указать путь к 2-м файлам')