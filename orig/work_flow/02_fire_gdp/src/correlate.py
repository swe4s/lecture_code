"""Print the Pearson correlation between two columns of each input file."""
import argparse
import math
import os
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='Pearson correlation of two columns, one row per file.')
    parser.add_argument('--in_files', type=str, nargs='+', required=True,
                        help='Whitespace-separated data files')
    parser.add_argument('--x_col', type=int, default=1,
                        help='Column index for x values')
    parser.add_argument('--y_col', type=int, default=2,
                        help='Column index for y values')
    return parser.parse_args()


def pearson(X, Y):
    """Return the Pearson correlation of X and Y, or None if undefined."""
    n = len(X)
    if n < 2:
        return None
    mean_x = sum(X) / n
    mean_y = sum(Y) / n
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y))
    var_x = sum((x - mean_x) ** 2 for x in X)
    var_y = sum((y - mean_y) ** 2 for y in Y)
    if var_x == 0 or var_y == 0:
        return None
    return cov / math.sqrt(var_x * var_y)


def main():
    args = get_args()
    print('name\tn\tr')
    for file_name in args.in_files:
        X = []
        Y = []
        try:
            with open(file_name) as f:
                for line in f:
                    A = line.split()
                    X.append(float(A[args.x_col]))
                    Y.append(float(A[args.y_col]))
        except FileNotFoundError:
            print('Could not find ' + file_name, file=sys.stderr)
            sys.exit(1)
        name = os.path.splitext(os.path.basename(file_name))[0]
        r = pearson(X, Y)
        r_str = 'NA' if r is None else '{:.3f}'.format(r)
        print(name + '\t' + str(len(X)) + '\t' + r_str)


if __name__ == '__main__':
    main()
