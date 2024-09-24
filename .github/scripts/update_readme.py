from glob import glob
import pandas as pd

if __name__ == '__main__':
    da_fiis_raw = pd.read_csv(glob("data/ranked_fiis_*.csv")[0])

    da_fiis = pd.DataFrame({
        'Código': f"[{da_fiis_raw['ticker']}](https://www.fundsexplorer.com.br/funds/{da_fiis_raw['ticker'].str.lower()})",
        'Score': f"{(float(da_fiis_raw['score']) * 100):.1f}%",
        'Setor(es)': da_fiis_raw['setor'],
        'DY (12M)': f"{da_fiis_raw['dy_12m_acumulado']:.2f}"
    }).head(15) # top 15

    markdown_table = da_fiis.to_markdown(index=False, numalign="left", stralign="left")

    with open('.github/templates/README.md', 'r') as f:
        readme_template = f.read()

    updated_readme = readme_template.replace('{{fii_ranking_table}}', markdown_table)
    print(updated_readme)

    with open('README.md', 'w') as f:
        f.write(updated_readme)