#!/usr/bin/env python3
"""
Script para configurar credenciais do Google Sheets API
"""

import os
import json
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopos necessários para a API do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def create_credentials_template():
    """
    Cria um template do arquivo credentials.json
    """
    template = {
        "installed": {
            "client_id": "SEU_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "seu-projeto-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "SEU_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(template, f, indent=2)
    
    print("✅ Template criado: credentials_template.json")
    print("\n📋 Instruções:")
    print("1. Acesse: https://console.cloud.google.com/")
    print("2. Crie um novo projeto ou selecione um existente")
    print("3. Ative a API do Google Sheets")
    print("4. Crie credenciais OAuth 2.0 para aplicação desktop")
    print("5. Baixe o arquivo JSON e renomeie para 'credentials.json'")
    print("6. Execute este script novamente")

def setup_oauth_credentials():
    """
    Configura credenciais OAuth2 para Google Sheets API
    """
    creds = None
    
    # Verificar se já existe token salvo
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Se não há credenciais válidas, fazer login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ Arquivo credentials.json não encontrado!")
                create_credentials_template()
                return False
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salvar credenciais para próxima execução
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    print("✅ Credenciais OAuth2 configuradas com sucesso!")
    return True

def create_service_account_template():
    """
    Cria template para service account
    """
    template = {
        "type": "service_account",
        "project_id": "seu-projeto-id",
        "private_key_id": "key-id",
        "private_key": "-----BEGIN PRIVATE KEY-----\nSUA_CHAVE_PRIVADA\n-----END PRIVATE KEY-----\n",
        "client_email": "seu-service-account@seu-projeto.iam.gserviceaccount.com",
        "client_id": "client-id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/seu-service-account%40seu-projeto.iam.gserviceaccount.com"
    }
    
    with open('service_account_template.json', 'w') as f:
        json.dump(template, f, indent=2)
    
    print("✅ Template de Service Account criado: service_account_template.json")
    print("\n📋 Instruções para Service Account:")
    print("1. Acesse: https://console.cloud.google.com/")
    print("2. Vá em IAM & Admin > Service Accounts")
    print("3. Crie uma nova conta de serviço")
    print("4. Baixe a chave JSON e renomeie para 'service_account.json'")
    print("5. Compartilhe a planilha com o email da service account")

def test_connection(spreadsheet_id):
    """
    Testa conexão com uma planilha específica
    """
    try:
        creds = None
        
        # Tentar service account primeiro
        if os.path.exists('service_account.json'):
            from google.oauth2 import service_account
            creds = service_account.Credentials.from_service_account_file(
                'service_account.json', scopes=SCOPES
            )
            print("🔑 Usando Service Account")
        
        # Fallback para OAuth2
        elif os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            print("🔑 Usando OAuth2")
        
        if not creds:
            print("❌ Nenhuma credencial encontrada!")
            return False
        
        # Construir serviço
        service = build('sheets', 'v4', credentials=creds)
        
        # Testar acesso à planilha
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range='A1:A1'
        ).execute()
        
        print("✅ Conexão com Google Sheets bem-sucedida!")
        print(f"📊 Planilha acessível: {spreadsheet_id}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar conexão: {e}")
        return False

def main():
    """
    Função principal
    """
    print("🚀 Configuração de Credenciais Google Sheets API")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "oauth":
            setup_oauth_credentials()
        
        elif command == "service":
            create_service_account_template()
        
        elif command == "test":
            if len(sys.argv) < 3:
                print("❌ Uso: python setup_credentials.py test SPREADSHEET_ID")
                return
            
            spreadsheet_id = sys.argv[2]
            test_connection(spreadsheet_id)
        
        else:
            print("❌ Comando inválido!")
            print("Comandos disponíveis:")
            print("  oauth   - Configurar OAuth2")
            print("  service - Criar template Service Account")
            print("  test ID - Testar conexão com planilha")
    
    else:
        print("Comandos disponíveis:")
        print("  python setup_credentials.py oauth")
        print("  python setup_credentials.py service")
        print("  python setup_credentials.py test SPREADSHEET_ID")
        print("\n💡 Recomendação: Use Service Account para automação")

if __name__ == '__main__':
    main()

