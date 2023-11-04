#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Oi, meu nome é Leonardo</p>
    <p>Sou Desenvolvedor Python, em breve vou postar mais algumas automações legais</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Teste Note RWE"
    msg['From'] = 'leonardorfragoso@gmail.com'
    msg['To'] = 'aesvalentim@gmail.com'
    password = 'olkdrblvpjbxffqr' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()

