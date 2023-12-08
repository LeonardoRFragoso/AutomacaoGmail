# Automatização de Envio de Email

Este script Python automatiza o envio de e-mails utilizando a biblioteca smtplib para se conectar a um servidor SMTP (Gmail neste caso).

## Uso

1. Configure as credenciais de e-mail:
   - Abra o script e substitua os valores de `msg['From']` (seu endereço de e-mail), `msg['To']` (o destinatário) e `password` (a senha do seu e-mail).

2. Execute o script:
   - Certifique-se de ter instalado as bibliotecas necessárias do Python. Consulte o arquivo `requirements.txt` para obter detalhes.
   - Execute o script em um ambiente Python.

3. Resultados:
   - O script enviará um e-mail com o assunto "Teste Note RWE" e um corpo contendo informações pessoais.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
