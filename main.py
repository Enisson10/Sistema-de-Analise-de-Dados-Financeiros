#!/usr/bin/env python3
"""
Sistema de Análise de Dados Financeiros
Arquivo principal para execução do sistema
"""

import sys
import os
from pathlib import Path

# Adicionar pasta src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from analyzer import FinancialAnalyzer
except ImportError:
    print("❌ Erro: Módulo analyzer não encontrado!")
    print("📁 Verifique se o arquivo src/analyzer.py existe")
    sys.exit(1)

def main():
    """Função principal do sistema"""
    print("💰 Sistema de Análise Financeira - v1.0")
    print("="*50)
    
    # Verificar argumentos
    if len(sys.argv) < 2:
        print("📋 Uso: python main.py <arquivo_dados.csv>")
        print("📝 Exemplo: python main.py data/sample_data.csv")
        return
    
    arquivo = sys.argv[1]
    
    # Verificar se arquivo existe
    if not os.path.exists(arquivo):
        print(f"❌ Erro: Arquivo '{arquivo}' não encontrado!")
        return
    
    try:
        print(f"📊 Carregando dados de: {arquivo}")
        
        # Inicializar analisador
        analyzer = FinancialAnalyzer(arquivo)
        data = analyzer.load_data()
        
        if data.empty:
            print("❌ Erro: Arquivo vazio ou formato inválido!")
            return
        
        print(f"✅ {len(data)} transações carregadas com sucesso!")
        
        # Análises
        print("\n📈 Executando análises...")
        total_gastos = analyzer.get_total_expenses()
        periodo = analyzer.get_date_range()
        categoria_analysis = analyzer.analyze_by_category()
        top_gastos = analyzer.get_top_expenses(5)
        
        # Exibir resultados
        print("\n" + "="*50)
        print("📊 RESUMO FINANCEIRO")
        print("="*50)
        
        print(f"💰 Total de Gastos: R$ {total_gastos:.2f}")
        print(f"📅 Período: {periodo}")
        print(f"🏷️  Categorias: {len(categoria_analysis)}")
        
        print("\n🔝 GASTOS POR CATEGORIA:")
        for categoria, valor in categoria_analysis.head().items():
            print(f"   • {categoria}: R$ {valor:.2f}")
        
        print("\n💸 TOP 5 MAIORES GASTOS:")
        for _, gasto in top_gastos.iterrows():
            data_gasto = gasto['data'].strftime('%d/%m/%Y') if hasattr(gasto['data'], 'strftime') else str(gasto['data'])
            print(f"   • {data_gasto} - {gasto['descricao']}: R$ {gasto['valor']:.2f}")
        
        print("\n✅ Análise concluída com sucesso!")
        print("🚀 Projeto funcionando perfeitamente!")
        
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        return 1

if __name__ == "__main__":
    main()