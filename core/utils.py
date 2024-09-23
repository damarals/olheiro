from rich.console import Console
from rich.table import Table

class CLI:
    def __init__(self):
        self.console = Console(width=140)

    def info(self, message: str):
        self.console.print(f"[bold blue]INFO[/bold blue] {message}")

    def print(self, *args, **kwargs):
        self.console.print(*args, **kwargs)

    def create_fii_table(self, ranked_fiis, num_rows: int = 10) -> Table:
        """
        Create a Rich Table with the top FIIs.

        Args:
            ranked_fiis (pd.DataFrame): A DataFrame with ranked FIIs.
            num_rows (int, optional): Number of rows to display. Defaults to 10.

        Returns:
            Table: A Rich Table with the top FIIs.
        """
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Score", justify="right")
        table.add_column("Ticker")
        table.add_column("Setor", width=36)
        table.add_column("DY (12M)", justify="right", width=10)
        table.add_column("Liquidez D. (R$)", justify="right", width=18)
        table.add_column("Patrimônio L. (R$)", justify="right", width=20)
        table.add_column("P/VPA", justify="right")
        table.add_column("Ativos", justify="right")

        for _, row in ranked_fiis.head(num_rows).iterrows():
            table.add_row(
                f"{(row['score'] * 100):.1f}%",
                row['ticker'],
                row['setor'],
                f"{row['dy_12m_acumulado']:.2f}%",
                f"{row['liquidez_diaria']}",
                f"{row['patrimonio_liquido']}",
                f"{row['p_vpa']:.2f}",
                str(row['quantidade_ativos'])
            )

        return table