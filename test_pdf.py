#!/usr/bin/env python3
import requests
import json

# Dados de exemplo para teste
dados_teste = {
    'nome_fantasia': 'Oficina Car10 Teste',
    'razao_social': 'Car10 Funilaria e Pintura LTDA',
    'cnpj': '12.345.678/0001-90',
    'nome_responsavel': 'João Silva',
    'email_telefone_responsavel': 'joao@car10.com.br / (11) 99999-9999',
    'inscricao_estadual_municipal': 'IE: 123456789 / IM: 987654321',
    'estado_uf': 'SP',
    'cidade': 'São Paulo',
    'endereco': 'Rua das Oficinas, 123 | Centro | 01234-567',
    'assinatura_cilia': 'Sim',
    'parcela_franquia': '3 vezes sem juros',
    'telefone_whatsapp': '(11) 98888-7777',
    'email_orcamentos': 'orcamentos@car10.com.br',
    'conta_bancaria': 'Conta Corrente | Agência 1234 | Conta 56789-0',
    'quantidade_funcionarios': '15 funcionários',
    'funcionarios_registrados': 'Sim, todos registrados',
    'seguro_responsabilidade': 'Sim, possui seguro',
    'seguradoras_credenciadas': 'Porto Seguro, Bradesco Seguros, Allianz',
    'recepcao_clientes': 'Sim',
    'banheiro_clientes': 'Sim',
    'estacionamento_clientes': 'Sim, 10 vagas',
    'checklist_recepcao': 'Sim, sempre realizado',
    'volume_veiculos': '50-80 veículos por mês',
    'divisoes_producao': 'Sim, setor de funilaria e pintura separados',
    'estrutura_eletricos': 'Sim, equipamentos para veículos elétricos',
    'itens_disponiveis': 'Cabine de pintura, Estufa, Equipamentos de solda, Compressor',
    'tipo_solicitacao': 'Credenciamento inicial',
    'validacao_joao': 'Aprovado',
    'acordo_regras': 'Sim',
    'carimbo_data_hora': '26/08/2025 14:30:00'
}

def test_pdf_generation():
    """
    Testa a geração de PDF via API
    """
    url = 'http://localhost:5000/api/checklist/generate-pdf'
    
    try:
        response = requests.post(url, json=dados_teste)
        
        if response.status_code == 200:
            # Salvar o PDF
            with open('teste_checklist.pdf', 'wb') as f:
                f.write(response.content)
            print("✅ PDF gerado com sucesso! Arquivo salvo como 'teste_checklist.pdf'")
        else:
            print(f"❌ Erro na geração do PDF: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao servidor. Certifique-se de que a aplicação Flask está rodando.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == '__main__':
    test_pdf_generation()

