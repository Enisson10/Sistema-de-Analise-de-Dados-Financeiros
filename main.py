#!/usr/bin/env python3
"""
Sistema de Análise de Dados Financeiros
Arquivo principal para execução do sistema
"""

import argparse
import sys
from pathlib import Path

def main():
    """Função principal do sistema"""
    print("🔄 Sistema de Análise Financeira - v1.0")
    print("📊 Projeto criado com sucesso!")
    print("⚠️  Para usar: instale as dependências com 'pip install -r requirements.txt'")
    
    # Verificar se arquivo foi fornecido
    if len(sys.argv) < 2:
        print("\n📋 Uso: python main.py <arquivo_dados.csv>")
        print("📝 Exemplo: python main.py data/sample_data.csv")
        return
    
    arquivo = sys.argv[1]
    print(f"📁 Arquivo especificado: {arquivo}")
    print("🚧 Funcionalidade completa em desenvolvimento...")

if __name__ == "__main__":
    main()