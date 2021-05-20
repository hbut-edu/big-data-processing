import csv


def execute(data, savepath):

    csv_reader = csv.reader(open(data))
    f = open(savepath, 'wb')
    for line in csv_reader:
        label = line[0]
        features = line[1:]
        libsvm_line = label + ' '

        for index, feature in enumerate(features):
            libsvm_line += str(index + 1) + ':' + feature + ' '
        f.write(bytes(libsvm_line.strip() + '\n', 'UTF-8'))

    f.close()


execute('mnist_train.csv', 'mnist_train.libsvm')
execute('mnist_test.csv', 'mnist_test.libsvm')