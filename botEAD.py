from sys import displayhook
import pyautogui
import time
from selenium import webdriver
import keyboard
from selenium.webdriver.common.keys import Keys
import os
from sys import exit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime


def enviar_email(situacao):

    email_from = 'enviar@gmail.com'#email usado para enviar 
    email_password = 'senha'#senha desse email que vai enviar
    email_sever = 'smtp.gmail.com'
    destinacion = ['receber@gmail.com']#email o qual vai receber a mensagem

    data_atual = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())#pega a data e horario do pc para enviar no email
    #pegar a data e hora atual do pc
    dia_atual = (data_atual[:11]) 
    hora_atual = (data_atual[11:]) 

    subject = 'Bot - Meet Python'
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['Subject'] = subject
    #a palavra situaçao refere-se a qual ele manda quando 'entra' e quando 'sai'
    text = f'''
    <p>Notificação de conclusão</p>
    <p>{situacao} aula nesse horário: </p>
    <p>Dia: {dia_atual}</p>
    <p>Hora: {hora_atual}</p>'''
    msg_text  = MIMEText(text, 'html')
    msg.attach(msg_text)

    try:
        smtp = smtplib.SMTP(email_sever, 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_from, email_password)
        smtp.sendmail(email_from, ','.join(destinacion), msg.as_string())
        smtp.quit()
        print("email enviado com sucesso")
    except Exception as err:
        print(f'Falha ao enviar email: {err}')


def entrar(aula):
    time.sleep(6)
    pyautogui.moveTo(x=464, y=1010, duration=0.5)#clica no navegador desejado
    pyautogui.click()

    time.sleep(2)


    pyautogui.moveTo(x=191, y=50, duration=0.5)#clica na barra de pesquisa
    pyautogui.click()

    time.sleep(2)

    pyautogui.write(aula)#adiciona o link da aula
    pyautogui.press("enter")#aperta enter

    time.sleep(10)

    pyautogui.keyDown('ctrl')
    pyautogui.press('e')#atalho para desativar a camera
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.moveTo(x=364, y=718, duration=0.5)#aqui ele clica para mutar o microfone\ tambem pode alterar para o exemplo de cima, utilizando o 'crtl+D'
    pyautogui.click()

    time.sleep(2)

    pyautogui.moveTo(x=936, y=565, duration=0.5)#clica em 'participar da aula'
    pyautogui.click()

    time.sleep(1)
    while keyboard.is_pressed('q') == False:#o programa vai encerrar a qualquer momento que voce precionar a tecla 'q'
        if pyautogui.locateOnScreen('meet.png', confidence=0.5):#quando voce é aceito em uma aula, a imagem do meet some, então ele so continua se a imagem do meet nao estiver mais aparecendo
            time.sleep(1)
            #print("Ainda não fui aceito")     
        else:
            #print("Fui aceito")
            time.sleep(2)
            pyautogui.moveTo(x=1142, y=940, duration=0.5)#clica onde fica o chat
            pyautogui.click()

            time.sleep(3)

            pyautogui.write("Bom dia")#mensagem que deseja enviar no chat ao entrar na aula
            pyautogui.press("enter")

            situacao = 'Entramos na'
            enviar_email(situacao)#envia um email indicando que entrou na aula
            #print("Estou no Assintindo a aula agora")
            while keyboard.is_pressed('q') == False:
                sairhora = datetime.now().hour #é usado para fazer a verifição de quando sair da aula
                sairmin = datetime.now().minute #é usado para fazer a verifição de quando sair da aula
                if pyautogui.locateOnScreen('sair.png', confidence=0.5) or (sairhora >= sh and sairmin >= sm):#ele sai dentro do horario desejado ou quando alguem designado por voce mandar uma mensagem no discord e ela aparecer na tela, ele vai sair(usado para sair da aula quando ela acabar mais cedo)
                    pyautogui.moveTo(x=763, y=938, duration=0.5)#clica no botao de sair da aula
                    pyautogui.click()
                    time.sleep(1)
                    situacao = 'Saimos da'#muda a mensagem para 'saimos'
                    enviar_email(situacao)#envia o email indicando que saiu da aula
                    exit()#sai do programa
    print("Precionou o q para sair")
    exit()



semana = datetime.now().weekday() #pega a hora, semana e min do computador
horas = datetime.now().hour
min = datetime.now().minute

sh = 0 
sm = 0
#semana em python vai de 0 ate 6, envez de 1 ate 7
#Segunda feira
if semana == 0:
    if horas == 8 and min >= 0: #horario que a aula começa
        aula ="Link da aula" #exemplo: "https://meet.google.com/cct-nauk-mpq"
        sh = 9 #hora que acaba a aula
        sm = 30 #min que acaba a aula
        entrar(aula)#chama a função de entrar na aula, passando o link correspondente
    elif horas == 9 and min >= 30:
        aula ="Link da aula"
        sh = 11
        sm = 0
        entrar(aula)

# Terça:
elif semana == 1:
    if horas == 8 and min >= 0:
        aula ="Link da aula"
        sh = 9
        sm = 28
        entrar(aula)
    elif horas == 9 and min >= 30:
        aula ="Link da aula"
        sh = 11
        sm = 0
        entrar(aula)


# Quarta:
elif semana == 2:
    if horas == 8 and min >= 0:
        aula ="Link da aula"
        sh = 9
        sm = 28
        entrar(aula)
    elif horas == 9 and min >= 30:
        aula ="Link da aula"
        sh = 11
        sm = 0
        entrar(aula)


# Quinta:
elif semana == 3:
    if horas == 8 and min >= 0:
        aula ="Link da aula"
        sh = 9
        sm = 28
        entrar(aula)
    elif horas == 9 and min >= 30:
        aula ="Link da aula"
        sh = 11
        sm = 0
        entrar(aula)

#causo tenha aula em mais horarios ou mais dias, é so copiar a função e alterar o elif semana == 'dia da semana que deseja'
#causo tenha aula em mais horarios é so dar mais um elif horas == '' min >=  '' e adicionar o horario de entrar e sair 
# Sabado/Domingo/Sexta:
elif semana == 4 or semana == 5 or semana == 6:
    print(f'Não temos aula hoje chefia')





