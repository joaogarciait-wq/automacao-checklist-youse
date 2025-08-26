# Deploy da Automação Checklist Youse no Render.com

## Pré-requisitos

1. Conta no GitHub (gratuita)
2. Conta no Render.com (gratuita)
3. Arquivo `service_account.json` do Google Cloud

## Passos para Deploy

### 1. Criar Repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique em "New repository"
3. Nome: `automacao-checklist-youse`
4. Marque como "Public" (necessário para conta gratuita do Render)
5. Clique em "Create repository"

### 2. Fazer Upload do Código

1. Baixe todos os arquivos do projeto
2. **IMPORTANTE:** Adicione o arquivo `service_account.json` na pasta raiz
3. Faça upload de todos os arquivos para o repositório GitHub

### 3. Deploy no Render

1. Acesse [render.com](https://render.com) e faça login
2. Clique em "New +" → "Web Service"
3. Conecte sua conta GitHub
4. Selecione o repositório `automacao-checklist-youse`
5. Configure:
   - **Name:** `automacao-checklist-youse`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python src/main.py`
6. Clique em "Create Web Service"

### 4. Configurar Variáveis de Ambiente

No painel do Render, vá em "Environment" e adicione:

- `FLASK_ENV` = `production`
- `PORT` = `10000` (ou deixe vazio para usar o padrão do Render)

### 5. Aguardar Deploy

O deploy pode levar alguns minutos. Você verá os logs em tempo real.

### 6. Testar a Aplicação

1. Acesse a URL fornecida pelo Render (ex: `https://automacao-checklist-youse.onrender.com`)
2. Configure a automação com o ID da sua planilha
3. Teste o sistema

## Limitações da Conta Gratuita

- **Sleep:** A aplicação "dorme" após 15 minutos de inatividade
- **Bandwidth:** 100GB por mês
- **Build time:** 500 horas por mês
- **Storage:** Limitado (PDFs são temporários)

## Troubleshooting

### Aplicação não inicia
- Verifique se o `service_account.json` está no repositório
- Verifique os logs no painel do Render

### Erro de credenciais
- Certifique-se de que o `service_account.json` é válido
- Verifique se a planilha foi compartilhada com o email da service account

### Links de PDF não funcionam
- Os PDFs são armazenados temporariamente
- Em caso de sleep, os PDFs podem ser perdidos

## Manutenção

Para atualizar a aplicação:
1. Faça as alterações no código
2. Faça commit no GitHub
3. O Render fará redeploy automaticamente

## Suporte

Em caso de problemas, verifique:
1. Logs no painel do Render
2. Status da aplicação
3. Configuração das variáveis de ambiente

