"""Make a scatter plot from two columns of a whitespace-separated file.

Best-practice rewrite of the scatter.py that ships with the assignment.
"""
import argparse
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402


def get_args():
    parser = argparse.ArgumentParser(
        description='Scatter plot of two columns from a text file.')
    parser.add_argument('--in_file', type=str, required=True,
                        help='Whitespace-separated data file')
    parser.add_argument('--out_file', type=str, required=True,
                        help='Output image file')
    parser.add_argument('--x_col', type=int, default=0,
                        help='Column index for x values')
    parser.add_argument('--y_col', type=int, default=1,
                        help='Column index for y values')
    parser.add_argument('--title', type=str, default='',
                        help='Plot title')
    parser.add_argument('--x_label', type=str, default='',
                        help='X axis label')
    parser.add_argument('--y_label', type=str, default='',
                        help='Y axis label')
    return parser.parse_args()


def read_columns(file_name, x_col, y_col):
    """Return two lists of floats from the given columns of a file."""
    X = []
    Y = []
    with open(file_name) as f:
        for line in f:
            A = line.split()
            X.append(float(A[x_col]))
            Y.append(float(A[y_col]))
    return X, Y


def plot(X, Y, out_file, title, x_label, y_label):
    """Save a scatter plot of X and Y to out_file."""
    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.savefig(out_file, bbox_inches='tight')
    plt.close(fig)


def main():
    args = get_args()
    try:
        X, Y = read_columns(args.in_file, args.x_col, args.y_col)
    except FileNotFoundError:
        print('Could not find ' + args.in_file, file=sys.stderr)
        sys.exit(1)
    plot(X, Y, args.out_file, args.title, args.x_label, args.y_label)


if __name__ == '__main__':
    main()
