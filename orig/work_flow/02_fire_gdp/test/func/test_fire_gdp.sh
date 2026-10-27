test -e ssshtest || curl -sLO https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

OUT=test_out
mkdir -p $OUT

run test_get_fire_gdp python src/get_fire_gdp.py \
    --co2_file test/data/co2.csv --gdp_file test/data/gdp.csv \
    --country Brazil --out_file $OUT/Brazil.tsv
assert_exit_code 0
assert_equal $OUT/Brazil.tsv $( ls $OUT/Brazil.tsv )

run test_get_fire_gdp_unknown python src/get_fire_gdp.py \
    --co2_file test/data/co2.csv --gdp_file test/data/gdp.csv \
    --country Atlantis --out_file $OUT/Atlantis.tsv
assert_exit_code 1
assert_in_stderr "No data for Atlantis"

run test_scatter python src/scatter.py --in_file $OUT/Brazil.tsv \
    --out_file $OUT/Brazil.png --x_col 1 --y_col 2
assert_exit_code 0
assert_equal $OUT/Brazil.png $( ls $OUT/Brazil.png )

run test_correlate python src/correlate.py --in_files $OUT/Brazil.tsv
assert_exit_code 0
assert_in_stdout "Brazil"

# The whole pipeline, end to end, on the small test data
rm -rf $OUT/tables $OUT/plots $OUT/correlations.tsv
run test_pipeline snakemake -c1 --configfile config_test.yaml --quiet
assert_exit_code 0
assert_equal $OUT/correlations.tsv $( ls $OUT/correlations.tsv )

rm -rf $OUT
