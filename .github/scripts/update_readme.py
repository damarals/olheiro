import os
import pandas as pd

if __name__ == '__main__':
    print(os.listdir('.'))
    da_fiis = pd.read_csv('data/ranked_fiis_*.csv') 
    da_fiis_top_15 = da_fiis.head(15)

    markdown_table = da_fiis_top_15.to_markdown(index=False, numalign="left", stralign="left")

    with open('.github/templates/README.md', 'r') as f:
        readme_template = f.read()

    updated_readme = readme_template.replace('{{fii_ranking_table}}', markdown_table)

    with open('README.md', 'w') as f:
        f.write(updated_readme)