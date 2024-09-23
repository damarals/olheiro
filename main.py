from core.scraper import Scraper
from core.ranker import Ranker

from rich.table import Table

from core.utils import CLI

if __name__ == "__main__":
    cli = CLI()

    # Initialize scraper
    scraper = Scraper(cli=cli)

    # Get FII data (either from cache or by scraping)
    fii_data = scraper.get_fii_data()
    cli.info(f"Working with data for {len(fii_data)} FIIs.")

    # Define ranker configuration
    config = {
        'weights': {
            'dy_12m_acumulado': 0.2,
            'p_vpa': 0.2,
            'liquidez_diaria': 0.2,
            'patrimonio_liquido': 0.15,
            'numero_cotistas': 0.1,
            'quantidade_ativos': 0.15,
        },
        'filters': {
            'dy_12m_acumulado': {'min': 8, 'max': 20},
            'p_vpa': {'min': 0.75, 'max': 1.25},
        }
    }

    # Rank FIIs
    ranker = Ranker(config)
    ranked_fiis = ranker.rank_fiis(fii_data)
    ranker.save_to_csv(ranked_fiis)

    # Display top FIIs
    top_n = 15
    table = cli.create_fii_table(ranked_fiis, num_rows=top_n)
    cli.print(f"\nTop {top_n}:", style="bold green")
    cli.print(table)