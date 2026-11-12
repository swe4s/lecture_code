import argparse

def h_ascii_sum(key, N):
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_polynomial_rolling(key, N, p=53):
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    return s % N

def h_python(key, N):
    return hash(key) % N


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hash strings from a file')
    parser.add_argument('file', help='Input file')
    parser.add_argument('-H', '--hash', choices=['ascii', 'rolling', 'python'],
                        default='ascii', help='Hash function (default: ascii)')
    parser.add_argument('-n', '--size', type=int, default=1000,
                        help='Hash table size (default: 1000)')
    args = parser.parse_args()

    functions = {
        'ascii': h_ascii_sum,
        'rolling': h_polynomial_rolling,
        'python': h_python
    }

    h = functions[args.hash]

    with open(args.file) as f:
        for line in f:
            key = line.strip()
            print(h(key, args.size))
