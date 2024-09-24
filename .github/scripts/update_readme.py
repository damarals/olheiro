from glob import glob
import pandas as pd

def generate_links(tickers) -> list:
    """
    Generate links for tickers with images and a divider using HTML tags.
    Args:
        tickers (list): A list of tickers.
    Returns:
        list: A list of ticker links with images and a divider.
    """
    fundsexp_img = 'https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png'
    investidor10_img = 'https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png'

    links = []
    for ticker in tickers:
        ticker_links = '<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;">'
        ticker_links += f'<a href="https://www.fundsexplorer.com.br/funds/{ticker.lower()}" target="_blank"><img src="{fundsexp_img}" alt="Fundsexplorer" height="32"></a>'
        ticker_links += '<div style="width:80px;height:1px;background-color:#ccc;"></div>'
        ticker_links += f'<a href="https://www.investidor10.com.br/fiis/{ticker.lower()}" target="_blank"><img src="{investidor10_img}" alt="Investidor10" height="12"></a>'
        ticker_links += '</div>'
        links.append(ticker_links)
    return links

if __name__ == '__main__':
    da_fiis_raw = pd.read_csv(glob("data/ranked_fiis_*.csv")[0])

    da_fiis = pd.DataFrame({
        'Score': (da_fiis_raw['score'] * 100).round(1).astype(str) + '%',
        'Código': da_fiis_raw['ticker'],
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