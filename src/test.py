import random


def fileGenerator():
    data = []
    for i in range(500):
        line = []
        for j in range(29):
            if j <= 5:
                line.append(abs(int(random.gauss(5, 2))))
            elif 6 <= j <= 18:
                line.append(abs(random.gauss(0.5, 1)))
            else:
                line.append(abs(int(random.gauss(15, 2))))
        data.append(line)
    with open('../dataset/source.txt', 'w') as fr:
        for item in data:
            for i in item:
                fr.write('%s|' % str(i))
            fr.write('\n')

if __name__ == '__main__':
    fileGenerator()
