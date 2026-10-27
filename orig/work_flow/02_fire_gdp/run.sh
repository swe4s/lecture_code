#!/bin/bash
set -euo pipefail

mkdir -p data results/tables results/plots

curl -sL "https://docs.google.com/uc?export=download&id=1AsXP_OGs1O_TDeXiZjk3fYV1SrG4vwXF" \
    -o data/Agrofood_co2_emission.csv
curl -sL "https://docs.google.com/uc?export=download&id=19YEPysdnK7VCXuAe9Og9pwYkNT5CbQzr" \
    -o data/IMF_GDP.csv

# Brazil
python src/get_fire_gdp.py \
    --co2_file data/Agrofood_co2_emission.csv \
    --gdp_file data/IMF_GDP.csv \
    --country Brazil \
    --out_file results/tables/Brazil.tsv
python src/scatter.py \
    --in_file results/tables/Brazil.tsv \
    --out_file results/plots/Brazil.png \
    --x_col 1 --y_col 2 \
    --title Brazil \
    --x_label 'Forest fire emissions (kt CO2)' \
    --y_label 'GDP (millions, local currency)'

# Indonesia
python src/get_fire_gdp.py \
    --co2_file data/Agrofood_co2_emission.csv \
    --gdp_file data/IMF_GDP.csv \
    --country Indonesia \
    --out_file results/tables/Indonesia.tsv
python src/scatter.py \
    --in_file results/tables/Indonesia.tsv \
    --out_file results/plots/Indonesia.png \
    --x_col 1 --y_col 2 \
    --title Indonesia \
    --x_label 'Forest fire emissions (kt CO2)' \
    --y_label 'GDP (millions, local currency)'

# Australia
python src/get_fire_gdp.py \
    --co2_file data/Agrofood_co2_emission.csv \
    --gdp_file data/IMF_GDP.csv \
    --country Australia \
    --out_file results/tables/Australia.tsv
python src/scatter.py \
    --in_file results/tables/Australia.tsv \
    --out_file results/plots/Australia.png \
    --x_col 1 --y_col 2 \
    --title Australia \
    --x_label 'Forest fire emissions (kt CO2)' \
    --y_label 'GDP (millions, local currency)'

# Canada
python src/get_fire_gdp.py \
    --co2_file data/Agrofood_co2_emission.csv \
    --gdp_file data/IMF_GDP.csv \
    --country Canada \
    --out_file results/tables/Canada.tsv
python src/scatter.py \
    --in_file results/tables/Canada.tsv \
    --out_file results/plots/Canada.png \
    --x_col 1 --y_col 2 \
    --title Canada \
    --x_label 'Forest fire emissions (kt CO2)' \
    --y_label 'GDP (millions, local currency)'

# Mexico
python src/get_fire_gdp.py \
    --co2_file data/Agrofood_co2_emission.csv \
    --gdp_file data/IMF_GDP.csv \
    --country Mexico \
    --out_file results/tables/Mexico.tsv
python src/scatter.py \
    --in_file results/tables/Mexico.tsv \
    --out_file results/plots/Mexico.png \
    --x_col 1 --y_col 2 \
    --title Mexico \
    --x_label 'Forest fire emissions (kt CO2)' \
    --y_label 'GDP (millions, local currency)'
