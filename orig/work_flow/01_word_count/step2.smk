# Step 2: wildcards.
# {name} matches any string. Snakemake fills it in from the file you ask for.
#
#   snakemake -s step2.smk -c1                    # error: which file?
#   snakemake -s step2.smk -c1 counts/forest.txt
#   snakemake -s step2.smk -c1 counts/desert.txt
#   snakemake -s step2.smk -c1 counts/jungle.txt   # error: no data/jungle.txt

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -w < {input} > {output}"
