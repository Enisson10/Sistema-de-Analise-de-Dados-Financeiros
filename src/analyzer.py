"""
Módulo principal de análise de dados financeiros
"""

import pandas as pd
import numpy as np
from datetime import datetime

class FinancialAnalyzer:
    def __init__(self, csv_file=None):
        """Inicializa o analisador financeiro"""
        self.csv_file = csv_file
        self.data = None
        
    def load_data(self):
        """Carrega dados do arquivo CSV"""
        try:
            if self.csv_file:
                self.data = pd.read_csv(self.csv_file)
                # Converter coluna de data
                if 'data' in self.data.columns:
                    self.data['data'] = pd.to_datetime(self.data['data'])
            return self.data if self.data is not None else pd.DataFrame()
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()
    
    def get_total_expenses(self):
        """Calcula total de gastos"""
        if self.data is None or self.data.empty:
            return 0
        
        # Assumindo que gastos são valores negativos
        gastos = self.data['valor'][self.data['valor'] < 0].sum()
        return abs(gastos)
    
    def analyze_by_category(self):
        """Análise por categoria"""
        if self.data is None or self.data.empty:
            return pd.Series()
        
        # Agrupar por categoria (apenas gastos)
        gastos_categoria = self.data[self.data['valor'] < 0].groupby('categoria')['valor'].sum()
        return gastos_categoria.abs().sort_values(ascending=False)
    
    def get_date_range(self):
        """Retorna período dos dados"""
        if self.data is None or self.data.empty or 'data' not in self.data.columns:
            return "Não disponível"
        
        inicio = self.data['data'].min().strftime('%d/%m/%Y')
        fim = self.data['data'].max().strftime('%d/%m/%Y')
        return f"{inicio} a {fim}"
    
    def analyze_monthly_trends(self):
        """Análise de tendências mensais"""
        if self.data is None or self.data.empty:
            return pd.DataFrame()
        
        # Criar coluna mês-ano
        self.data['mes_ano'] = self.data['data'].dt.to_period('M')
        
        # Agrupar gastos por mês
        monthly = self.data[self.data['valor'] < 0].groupby('mes_ano')['valor'].sum()
        return monthly.abs()
    
    def get_top_expenses(self, n=10):
        """Top N maiores gastos"""
        if self.data is None or self.data.empty:
            return pd.DataFrame()
        
        gastos = self.data[self.data['valor'] < 0].copy()
        gastos['valor'] = gastos['valor'].abs()
        return gastos.nlargest(n, 'valor')[['data', 'descricao', 'valor', 'categoria']]