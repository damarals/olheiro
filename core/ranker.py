import datetime
import os
import pandas as pd
from typing import Dict, Any

class Ranker:
    """
    A class for ranking FIIs (Fundos de Investimento Imobiliário) based on a custom scoring system.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the Ranker with a configuration object.

        Args:
            config (Dict[str, Any]): A configuration object containing weights and filters. 
                                     The sum of weights should be approximately 1.0.
        """
        self.config = config
        if not (0.99 < sum(self.config['weights'].values()) < 1.01):
            raise ValueError("The sum of weights should be approximately 1.0")

    def calculate_score(self, fii: Dict[str, Any]) -> float:
        """
        Calculate the score for a single FII based on the weighted metrics.

        Args:
            fii (Dict[str, Any]): A dictionary containing FII data.

        Returns:
            float: The calculated score for the FII.
        """
        score = 0.0

        if 'dy_12m_acumulado' in fii and 'dy_12m_acumulado' in self.config['weights']:
            score += (fii['dy_12m_acumulado']/20) * self.config['weights']['dy_12m_acumulado']

        if 'p_vpa' in fii and 'p_vpa' in self.config['weights']:
            if pd.notna(fii['p_vpa']):
                score += (1 / (fii['p_vpa'])) * self.config['weights']['p_vpa']
            else:
                score += 0.5 * self.config['weights']['p_vpa']

        if 'liquidez_diaria' in fii and 'liquidez_diaria' in self.config['weights']:
            if pd.notna(fii['liquidez_diaria']):
                score += min(float(fii['liquidez_diaria']) / 10000000, 1) * self.config['weights']['liquidez_diaria']
            else:
                score += 0.5 * self.config['weights']['liquidez_diaria']

        if 'patrimonio_liquido' in fii and 'patrimonio_liquido' in self.config['weights']:
            if pd.notna(fii['patrimonio_liquido']):
                score += min(float(fii['patrimonio_liquido']) / 10000000, 1) * self.config['weights']['patrimonio_liquido']
            else:
                score += 0.5 * self.config['weights']['patrimonio_liquido']

        if 'numero_cotistas' in fii and 'numero_cotistas' in self.config['weights']:
            if pd.notna(fii['numero_cotistas']):
                score += min(fii['numero_cotistas'] / 1000000, 1) * self.config['weights']['numero_cotistas']
            else:
                score += 0.5 * self.config['weights']['numero_cotistas']

        if 'quantidade_ativos' in fii and 'quantidade_ativos' in self.config['weights']:
            if pd.notna(fii['quantidade_ativos']):
                score += min(int(fii['quantidade_ativos'])/50, 1) * self.config['weights']['quantidade_ativos']
            else:
                score += 0.5 * self.config['weights']['quantidade_ativos']

        return score

    def rank_fiis(self, fiis_data: pd.DataFrame) -> pd.DataFrame:
        """
        Rank FIIs based on their calculated scores and apply filters from the config.

        Args:
            fiis_data (pd.DataFrame): A DataFrame containing FII data.

        Returns:
            pd.DataFrame: A DataFrame with FIIs and their scores, sorted by score in descending order.
        """
        for var, filter_range in self.config['filters'].items():
            if 'min' in filter_range:
                fiis_data = fiis_data[fiis_data[var] >= filter_range['min']]
            if 'max' in filter_range:
                fiis_data = fiis_data[fiis_data[var] <= filter_range['max']]

        fiis_data['score'] = fiis_data.apply(self.calculate_score, axis=1)
        return fiis_data.sort_values('score', ascending=False).reset_index(drop=True)
    
    def save_to_csv(self, ranked_fiis: pd.DataFrame):
        """
        Save the ranked FIIs to a CSV file with the cached timestamp in the filename.

        Args:
            ranked_fiis (pd.DataFrame): A DataFrame with ranked FIIs data.
        """
        os.makedirs('data', exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'data/ranked_fiis_{timestamp}.csv'
        ranked_fiis.to_csv(filename, index=False)