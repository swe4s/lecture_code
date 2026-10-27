import sys
import unittest

sys.path.insert(0, 'src')

import fire_gdp  # noqa: E402

CO2 = 'test/data/co2.csv'
GDP = 'test/data/gdp.csv'


class TestGetData(unittest.TestCase):
    def test_all_rows(self):
        self.assertEqual(len(fire_gdp.get_data(CO2)), 6)

    def test_query(self):
        rows = fire_gdp.get_data(CO2, query_column=0, query_value='Brazil')
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(row[0] == 'Brazil' for row in rows))

    def test_query_no_match(self):
        self.assertEqual(fire_gdp.get_data(CO2, 0, 'Atlantis'), [])

    def test_return_header(self):
        header, rows = fire_gdp.get_data(GDP, return_header=True)
        self.assertEqual(header[0], 'Country')
        self.assertEqual(header[56], '2005')
        self.assertEqual(len(rows), 2)


class TestGetColumnIndex(unittest.TestCase):
    def test_present(self):
        self.assertEqual(fire_gdp.get_column_index(['a', 'b', 'c'], 'b'), 1)

    def test_absent(self):
        self.assertIsNone(fire_gdp.get_column_index(['a', 'b'], 'z'))

    def test_empty_header(self):
        self.assertIsNone(fire_gdp.get_column_index([], 'a'))


class TestGetFireGdpYearData(unittest.TestCase):
    def test_brazil(self):
        data = fire_gdp.get_fire_gdp_year_data(CO2, GDP, 'Brazil')
        self.assertEqual(len(data), 3)
        self.assertEqual(data[1], [2005, 18253.5232, 2170584.50])

    def test_skips_missing_fire(self):
        data = fire_gdp.get_fire_gdp_year_data(CO2, GDP, 'Canada')
        self.assertEqual([d[0] for d in data], [2004, 2005])

    def test_unknown_country(self):
        self.assertEqual(
            fire_gdp.get_fire_gdp_year_data(CO2, GDP, 'Atlantis'), [])


if __name__ == '__main__':
    unittest.main()
