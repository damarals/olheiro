<img alt="Olheiro banner" src=".github/banner.png" style="border-radius: 15px; max-width: 100%; height: auto; display: block; margin: 0 0 16px 0;"/>
<div align="center">
    <img src="https://img.shields.io/github/v/tag/damarals/olheiro?color=success&label=" alt="Latest Tag" />
    <img src="https://img.shields.io/github/last-commit/damarals/olheiro/main?path=README.md&label=%C3%BAltima%20atualiza%C3%A7%C3%A3o&color=blue" alt="Latest Update" >
</div>
<br />
<div align="center"><strong>Análise e Classificação Automatizada de Ativos</strong></div>
<div align="center">Uma ferramenta Python para raspar, analisar e classificar Fundos de Investimento Imobiliário (FIIs)<br/> e outros ativos variáveis.</div>
<br />
<div align="center">
  <sub>Desenvolvido por <a href="https://github.com/damarals">Daniel Amaral</a> 👨‍💻</sub>
</div>
<br />

## Introdução

O Olheiro é uma aplicação Python projetada para automatizar a análise e classificação de ativos financeiros. Atualmente focado em Fundos de Investimento Imobiliário (FIIs), o Olheiro raspa dados, aplica métricas personalizáveis e fornece classificações para auxiliar investidores em suas decisões.

## Características

- Raspagem automatizada de dados de FIIs do fundsexplorer.com.br
- Sistema de classificação personalizável baseado em múltiplas métricas
- Filtragem de FIIs por Dividend Yield (DY) e Valor Patrimonial da Cota (P/VP)
- Exportação de dados brutos e classificados para arquivos CSV
- Exibição dos FIIs mais bem classificados em uma tabela formatada
- Extensibilidade planejada para incluir outros ativos variáveis, como ações

## Top 15 FIIs

A tabela abaixo apresenta os 15 FIIs mais bem classificados de acordo com as [configurações padrões](#personalização). Esta tabela é atualizada diariamente às 12:00 PM (horário de Brasília).

| Score   | Código   | Setor                            | DY (12M)   | P/VPA   | Ativos   | Links                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------|:---------|:---------------------------------|:-----------|:--------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 83.2%   | MXRF11   | Papéis                           | 12.04%     | 1.01    | 21       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/mxrf11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/mxrf11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 79.8%   | XPML11   | Shoppings                        | 9.74%      | 0.9     | 25       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/xpml11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/xpml11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 78.8%   | BTLG11   | Imóveis Industriais e Logísticos | 9.27%      | 0.94    | 40       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/btlg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/btlg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 78.5%   | TGAR11   | Fundo de Desenvolvimento         | 13.31%     | 0.98    | 27       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/tgar11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/tgar11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 77.7%   | PVBI11   | Lajes Corporativas               | 8.21%      | 0.79    | 25       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/pvbi11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/pvbi11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 76.4%   | VISC11   | Shoppings                        | 9.81%      | 0.84    | 47       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/visc11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/visc11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 75.8%   | TRXF11   | Imóveis Comerciais - Outros      | 11.04%     | 0.98    | 49       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/trxf11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/trxf11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 75.4%   | KNCR11   | Papéis                           | 11.96%     | 1.03    | 18       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/kncr11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/kncr11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 75.0%   | CPTS11   | Papéis                           | 10.72%     | 0.87    | 18       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/cpts11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/cpts11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 72.1%   | KNHY11   | Papéis                           | 12.75%     | 1.04    | 18       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/knhy11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/knhy11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 71.2%   | RZTR11   | Misto                            | 12.52%     | 0.91    | 34       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/rztr11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/rztr11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 71.1%   | HGLG11   | Imóveis Industriais e Logísticos | 8.24%      | 1       | 31       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/hglg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/hglg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 69.6%   | HGRU11   | Misto                            | 9.18%      | 0.97    | 86       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/hgru11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/hgru11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 69.5%   | KNIP11   | Papéis                           | 10.63%     | 0.97    | 18       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/knip11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/knip11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |
| 67.7%   | XPLG11   | Imóveis Industriais e Logísticos | 8.9%       | 0.88    | 35       | <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;"><a href="https://www.fundsexplorer.com.br/funds/xplg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/fundsexplorer-logo.png" alt="Fundsexplorer" height="32"></a><div style="width:80px;height:1px;background-color:#ccc;"></div><a href="https://www.investidor10.com.br/fiis/xplg11" target="_blank"><img src="https://raw.githubusercontent.com/damarals/olheiro/main/.github/investidor10-logo.png" alt="Investidor10" height="12"></a></div> |

## Personalização

Você pode ajustar os pesos e filtros de classificação no arquivo `main.py`:

```python
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
```

Por padrão, é utilizada a configuração acima.

## Como Usar

### 1. Usando Docker
Docker é uma maneira fácil e rápida de rodar o projeto sem precisar configurar dependências localmente.

   - Construa a imagem:
      ```bash
      docker build -t olheiro .
      ```

   - Execute o container:
      ```bash
      docker run --rm -v $(pwd)/data:/app/data olheiro
      ```
      Caso não queira armazenar os dados localmente, remova a opção de volume:
      ```bash
      docker run --rm olheiro
      ```

   Os resultados serão exibidos no console e salvos no diretório `data` (se optar pelo compartilhamento de volume). 

### 2. Usando Poetry
Se preferir executar o projeto localmente, sem Docker, use o gerenciador de dependências Poetry.

   - Instale as dependências:
      ```bash
      poetry install
      ```

   - Execute o script principal:
      ```bash
      poetry run python main.py
      ```

   Os resultados serão exibidos no console e salvos no diretório `data`.

### 3. Usando DevContainer (Para Contribuidores)
O DevContainer é ideal para quem deseja contribuir com o projeto, pois oferece um ambiente de desenvolvimento pré-configurado com todas as dependências e configurações necessárias.

1. Certifique-se de ter o Docker e o VSCode instalados, junto com a extensão Dev Containers.

2. Abra o projeto no VSCode. Quando solicitado, escolha a opção "Open in Container".

3. Uma vez no container, você pode instalar dependências e rodar o projeto com os mesmos comandos descritos na subseção [Usando Poetry](#2-usando-poetry).

Este ambiente facilita o desenvolvimento, especialmente para quem está contribuindo, garantindo consistência e compatibilidade entre as configurações de todos os desenvolvedores.

## Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Se encontrar algum problema ou quiser sugerir uma melhoria, não hesite em contribuir.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Aviso Legal

Esta ferramenta é apenas para fins educacionais. Sempre faça sua própria pesquisa antes de tomar decisões de investimento.