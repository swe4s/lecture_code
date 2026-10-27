"""Write the year, forest fire and GDP table for one country."""
import argparse
import sys

import fire_gdp


def get_args():
    parser = argparse.ArgumentParser(
        description='Write year, forest fires and GDP for one country.')
    parser.add_argument('--co2_file', type=str, required=True,
                        help='Agrofood CO2 emission CSV')
    parser.add_argument('--gdp_file', type=str, required=True,
                        help='IMF GDP CSV')
    parser.add_argument('--country', type=str, required=True,
                        help='Country name')
    parser.add_argument('--out_file', type=str, required=True,
                        help='Tab-separated output file')
    return parser.parse_args()


def main():
    args = get_args()
    try:
        data = fire_gdp.get_fire_gdp_year_data(args.co2_file,
                                               args.gdp_file,
                                               args.country)
    except FileNotFoundError as e:
        print('Could not find ' + e.filename, file=sys.stderr)
        sys.exit(1)

    if len(data) == 0:
        print('No data for ' + args.country, file=sys.stderr)
        sys.exit(1)

    with open(args.out_file, 'w') as f:
        for year, fire, gdp in data:
            f.write(str(year) + '\t' + str(fire) + '\t' + str(gdp) + '\n')


if __name__ == '__main__':
    main()
