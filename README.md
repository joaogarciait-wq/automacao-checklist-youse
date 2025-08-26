# 🚀 Automação Checklist - Youse x Car10

Sistema de automação que monitora uma planilha Google Sheets e gera automaticamente PDFs do checklist de credenciamento de oficinas sempre que uma nova linha for adicionada.

## 📋 Funcionalidades

- **Monitoramento automático** da planilha Google Sheets
- **Geração automática de PDF** com dados do checklist
- **Inserção automática do link** do PDF na planilha
- **Interface web** para controle e monitoramento
- **API REST** para integração com outros sistemas

## 🛠️ Configuração Inicial

### 1. Configurar Credenciais do Google Sheets API

#### Opção A: Service Account (Recomendado para automação)

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a **Google Sheets API**
4. Vá em **IAM & Admin > Service Accounts**
5. Crie uma nova conta de serviço
6. Baixe a chave JSON e salve como `service_account.json` na pasta do projeto
7. **Importante**: Compartilhe sua planilha Google Sheets com o email da service account

#### Opção B: OAuth2 (Para uso pessoal)

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie credenciais OAuth 2.0 para aplicação desktop
3. Baixe o arquivo JSON e salve como `credentials.json` na pasta do projeto
4. Execute o script de configuração:

```bash
python setup_credentials.py oauth
```

### 2. Obter ID da Planilha Google Sheets

O ID da planilha está na URL do Google Sheets:
```
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                    Este é o ID da planilha
```

### 3. Instalar Dependências

```bash
cd checklist-automation
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Como Usar

### 1. Iniciar o Sistema

```bash
cd checklist-automation
source venv/bin/activate
python src/main.py
```

O sistema estará disponível em: http://localhost:5000

### 2. Configurar via Interface Web

1. Acesse http://localhost:5000
2. Insira o **ID da planilha** Google Sheets
3. Clique em **"Configurar Automação"**
4. Teste o sistema com **"Testar Sistema"**
5. Inicie o monitoramento com **"Iniciar Monitoramento"**

### 3. Configurar via API

#### Configurar automação:
```bash
curl -X POST http://localhost:5000/api/checklist/automation/setup \
  -H "Content-Type: application/json" \
  -d '{"spreadsheet_id": "SEU_ID_DA_PLANILHA"}'
```

#### Iniciar monitoramento:
```bash
curl -X POST http://localhost:5000/api/checklist/automation/start \
  -H "Content-Type: application/json" \
  -d '{"interval": 30}'
```

#### Verificar status:
```bash
curl http://localhost:5000/api/checklist/automation/status
```

## 📊 Estrutura da Planilha

O sistema espera que a planilha tenha as seguintes colunas (baseado no checklist fornecido):

- NOME FANTASIA
- RAZÃO SOCIAL
- Validação João
- Carimbo de data/hora
- ESTÁ DE ACORDO COM AS REGRAS ACIMA?
- CNPJ
- NOME DO RESPONSÁVEL PELA OFICINA
- E-MAIL E TELEFONE DO RESPONSÁVEL
- INSCRIÇÃO ESTADUAL E MUNICIPAL
- ESTADO (UF) DA OFICINA
- CIDADE DA OFICINA
- ENDEREÇO (RUA | Nº | BAIRRO | CEP)
- POSSUI ASSINATURA DO CILIA?
- PARCELA A FRANQUIA EM QUANTAS VEZES SEM JUROS?
- TELEFONE OU WHATSAPP DE ATENDIMENTO
- E-MAIL PARA DÚVIDAS OU ENVIO DE ORÇAMENTOS
- CONTA BANCÁRIA VINCULADA AO CNPJ
- QUANTOS FUNCIONÁRIOS A OFICINA POSSUI?
- TODOS SÃO REGISTRADOS?
- A OFICINA POSSUI SEGURO DE RESPONSABILIDADE CIVIL?
- EM QUAIS SEGURADORAS A OFICINA É CREDENCIADA?
- POSSUI RECEPÇÃO DE CLIENTES?
- POSSUI BANHEIRO PARA OS CLIENTES?
- POSSUI ESTACIONAMENTO PARA CLIENTES?
- É FEITO CHECK LIST NA RECEPÇÃO DO VEÍCULO?
- QUAL É O VOLUME DE VEÍCULOS ATENDIDOS MENSALMENTE?
- HÁ DIVISÕES NO SETOR DE PRODUÇÃO?
- A OFICINA POSSUI ESTRUTURA E EQUIPAMENTOS NECESSÁRIOS PARA ATENDER VEÍCULOS ELÉTRICOS?
- SELECIONE OS ÍTENS DISPONÍVEIS NA OFICINA
- TIPO DE SOLICITAÇÃO

O sistema automaticamente adicionará uma coluna **"Link PDF"** se ela não existir.

## 🔧 API Endpoints

### Geração de PDF
- `POST /api/checklist/generate-pdf` - Gera PDF manualmente
- `GET /api/checklist/pdf/{filename}` - Serve arquivos PDF

### Automação
- `POST /api/checklist/automation/setup` - Configura automação
- `POST /api/checklist/automation/start` - Inicia monitoramento
- `POST /api/checklist/automation/stop` - Para monitoramento
- `GET /api/checklist/automation/status` - Status do sistema
- `POST /api/checklist/automation/test` - Testa sistema

### Teste
- `GET /api/checklist/test` - Endpoint de teste

## 📁 Estrutura do Projeto

```
checklist-automation/
├── src/
│   ├── main.py                 # Aplicação Flask principal
│   ├── routes/
│   │   ├── checklist.py        # Rotas da API
│   │   └── user.py            # Rotas de usuário (template)
│   ├── services/
│   │   ├── sheets_monitor.py   # Monitor do Google Sheets
│   │   └── automation_service.py # Serviço principal
│   ├── models/
│   │   └── user.py            # Modelos de dados
│   └── static/
│       └── index.html         # Interface web
├── venv/                      # Ambiente virtual
├── requirements.txt           # Dependências
├── setup_credentials.py       # Script de configuração
├── test_pdf.py               # Script de teste
└── README.md                 # Esta documentação
```

## 🔍 Solução de Problemas

### Erro de Autenticação
- Verifique se o arquivo `service_account.json` ou `credentials.json` está presente
- Confirme que a planilha foi compartilhada com a service account
- Execute `python setup_credentials.py test SEU_ID_PLANILHA` para testar

### Erro de Conexão
- Verifique se a aplicação Flask está rodando
- Confirme que a porta 5000 não está sendo usada por outro processo
- Teste a conectividade com `curl http://localhost:5000/api/checklist/test`

### PDF não é gerado
- Verifique se há dados na nova linha da planilha
- Confirme que o monitoramento está ativo
- Verifique os logs da aplicação para erros

## 📝 Logs e Monitoramento

O sistema gera logs detalhados que podem ser visualizados no terminal onde a aplicação está rodando. Para logs persistentes, redirecione a saída:

```bash
python src/main.py > app.log 2>&1 &
```

## 🔒 Segurança

- **Nunca** compartilhe arquivos de credenciais (`service_account.json`, `credentials.json`)
- Use HTTPS em produção
- Configure firewall adequadamente
- Monitore logs de acesso

## 🚀 Deploy em Produção

Para deploy em produção, considere:

1. Usar um servidor WSGI como Gunicorn
2. Configurar proxy reverso (Nginx)
3. Usar HTTPS
4. Configurar monitoramento e logs
5. Backup das credenciais

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique os logs da aplicação
2. Teste a conectividade com Google Sheets
3. Confirme que a estrutura da planilha está correta
4. Execute os testes do sistema

## 📄 Licença

Este projeto foi desenvolvido para automação interna da Youse x Car10.

