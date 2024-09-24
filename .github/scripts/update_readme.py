from glob import glob
import pandas as pd

def generate_links(tickers) -> list:
    """
    Generate links for tickers.
    Args:
        tickers (list): A list of tickers.
    Returns:
        list: A list of ticker links.
    """
    fundsexp_img = 'https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png'
    investidor10_img = 'https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png'

    links = []
    for ticker in tickers:
        ticker_links = f'[![Fundsexplorer]({fundsexp_img})](https://www.fundsexplorer.com.br/funds/{ticker.lower()})\n'
        ticker_links += f'[![Investidor10]({investidor10_img})](https://www.investidor10.com.br/fiis/{ticker.lower()})'
        links.append(ticker_links)
    return links

if __name__ == '__main__':
    da_fiis_raw = pd.read_csv(glob("data/ranked_fiis_*.csv")[0])

    da_fiis = pd.DataFrame({
        'Código': f'[' + da_fiis_raw['ticker'] + '](https://www.fundsexplorer.com.br/funds/' + da_fiis_raw['ticker'].str.lower() + ')',
        'Score': (da_fiis_raw['score'] * 100).round(1).astype(str) + '%',
        'Setor': da_fiis_raw['setor'],
        'DY (12M)': da_fiis_raw['dy_12m_acumulado'].round(2).astype(str) + '%',
        'P/VPA': da_fiis_raw['p_vpa'].round(2).astype(str),
        'Ativos': da_fiis_raw['quantidade_ativos'].astype(str),
        'Links': generate_links(da_fiis_raw['ticker'])
    }).head(15) # top 15

    markdown_table = da_fiis.to_markdown(index=False, numalign="left", stralign="left")

    with open('.github/templates/README.md', 'r') as f:
        readme_template = f.read()

    updated_readme = readme_template.replace('{{fii_ranking_table}}', markdown_table)
    print(updated_readme)

    with open('README.md', 'w') as f:
        f.write(updated_readme)