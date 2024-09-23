from io import StringIO
import os
import pandas as pd
import requests

from core.utils import CLI

class Scraper:
    """A class for fetching FII (Fundos de Investimento Imobiliário) data from fundsexplorer.com.br API."""

    def __init__(self, cli: CLI = CLI()):
        """Initialize the FIIScraper with headers for HTTP requests."""
        self.cli = cli
        self.api_url = 'https://www.fundsexplorer.com.br/wp-json/funds/v1/get-ranking'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'x-funds-nonce': '61495f60b533cc40ad822e054998a3190ea9bca0d94791a1da'
        }

    def fetch_fii_data(self) -> pd.DataFrame:
        """
        Fetch FII data from the API.

        Returns:
            pd.DataFrame: A DataFrame containing FII data.
        """
        response = requests.get(self.api_url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        df = pd.read_json(StringIO(data), dtype=True)

        # Replace empty strings with NA
        df.replace('', pd.NA, inplace=True)
        
        # Rename columns to snake_case with better names
        column_mapping = {
            'post_id': 'id',
            'ticker': 'ticker',
            'dividendo': 'ultimo_dividendo',
            'yeld': 'dividend_yield',
            'media_yield_3m': 'dy_3m_media',
            'soma_yield_3m': 'dy_3m_acumulado',
            'media_yield_6m': 'dy_6m_media',
            'soma_yield_6m': 'dy_6m_acumulado',
            'media_yield_12m': 'dy_12m_media',
            'soma_yield_12m': 'dy_12m_acumulado',
            'variacao_cotacao_mes': 'variacao_preco_mes',
            'rentabilidade': 'rentabilidade_total',
            'rentabilidade_mes': 'rentabilidade_mes',
            'cotacao_fechamento': 'preco_atual',
            'soma_yield_ano_corrente': 'dy_ano_corrente',
            'ano': 'ano',
            'vpa_yield': 'dy_patrimonial',
            'vpa': 'valor_patrimonial_cota',
            'vpa_change': 'variacao_vpa',
            'pl': 'preco_lucro',
            'vpa_rent': 'rentabilidade_patrimonial',
            'vpa_rent_m': 'rentabilidade_patrimonial_mes',
            'yield_vpa_3m_sum': 'dy_patrimonial_3m_acumulado',
            'yield_vpa_3m': 'dy_patrimonial_3m',
            'yield_vpa_6m_sum': 'dy_patrimonial_6m_acumulado',
            'yield_vpa_6m': 'dy_patrimonial_6m',
            'yield_vpa_12m_sum': 'dy_patrimonial_12m_acumulado',
            'yield_vpa_12m': 'dy_patrimonial_12m',
            'setor': 'setor',
            'setor_slug': 'setor_slug',
            'valor': 'valor_cota',
            'liquidezmediadiaria': 'liquidez_diaria',
            'patrimonio': 'patrimonio_liquido',
            'pvp': 'p_vp',
            'p_vpa': 'p_vpa',
            'post_title': 'nome_fundo',
            'ativos': 'quantidade_ativos',
            'volatility': 'volatilidade',
            'numero_cotista': 'numero_cotistas',
            'tx_gestao': 'taxa_gestao',
            'tx_admin': 'taxa_administracao',
            'tx_performance': 'taxa_performance'
        }
        
        df = df.rename(columns=column_mapping)
        return df[column_mapping.values()]

    def get_fii_data(self) -> pd.DataFrame:
        """
        Get FII data from the API.

        Returns:
            pd.DataFrame: A DataFrame containing FII data.
        """
        self.cli.info("Fetching data from API.")
        scraped_data = self.fetch_fii_data()
        self.save_to_csv(scraped_data)

        return scraped_data

    def save_to_csv(self, data: pd.DataFrame):
        """
        Save the fetched FII data to a CSV file.

        Args:
            data (pd.DataFrame): A DataFrame containing FII data.
        """
        os.makedirs('data', exist_ok=True)
        timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
        filename = f'data/fiis_data_{timestamp}.csv'
        data.to_csv(filename, index=False)
        self.cli.info(f"Data saved to [bold cyan]{filename}[/bold cyan]")