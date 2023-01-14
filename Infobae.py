import requests
page = requests.get('https://www.infobae.com/')
page_2 = requests.get('https://dolarhoy.com/')
page_3 = requests.get ('https://www.pagina12.com.ar/')
page_4 = requests.get ('https://tn.com.ar/')
page_5 = requests.get ('https://vandal.elespanol.com/')
page_6 =requests.get ('https://espndeportes.espn.com/basquetbol/') 

import bs4
infobae = bs4.BeautifulSoup(page.text, 'lxml')
dolar_hoy = bs4.BeautifulSoup(page_2.text, 'lxml')
pagina_12 = bs4.BeautifulSoup(page_3.text, 'lxml')
tn = bs4.BeautifulSoup(page_4.text, 'lxml')
vandal = bs4.BeautifulSoup(page_5.text, 'lxml')
espn = bs4.BeautifulSoup(page_6.text, 'lxml')

#Preguntar al usuario que quiere saber: 

while True: 
    try:
        mode = int(input ('Que quiere saber: \n 1. Precio de dolares \n 2. Titular \n 3. Mandar un mail con toda la información \n Elija: '))
    except:
        print ('Inserte un numero')
    else:
        if mode  > 3 or mode < 0:
            print ('Parece que no inserto una opción disponible')
        else:
            break

if mode == 1:
    
    dolares = infobae.select('.exc-tit')
    precios_dolares = infobae.select('.exc-val')
    
    for index in range (len(dolares)):
        print (f'\n El precio de {dolares[index].getText()}: {precios_dolares[index].getText()}')
    
elif  mode == 2: 
    titulo = infobae.select ('.cst_hl.dktfs38')
    titular = infobae.select('.cst_deck.dktfs19.dktlh150')
    
    from colorama import Fore
    print (Fore.RED, f'{titulo[0].getText()}: ')
    print (Fore.BLACK, f'\n {titular[0].getText()}')

elif mode == 3: 
    import smtplib
    
    #smt_obj = smtplib.SMTP('smtp.gmail.com',587)
    #smt_obj.ehlo()
    #smt_obj.starttls
    
    import getpass
    #email = input ('Ingrese su dirección de correo: ')
    #contraseña = getpass.getpass('Ingrese contraseña: ')
    #smt_obj.login (email, contraseña)
    
    titulo = infobae.select ('.cst_hl.dktfs36')
    titular = infobae.select('.cst_deck.dktfs19.dktlh150')
    titulo_2 = pagina_12.select('.element.title-prefix')
    titular_2 = pagina_12.select('.element.title-suffix')
    titulo_3 = tn.select ('.card__headline')
    titular_3 = tn.select ('.card__subheadline')
    
    noti_vandal = vandal.select('.titulo_portada')
    noticias_vandal= ''''''
    for numero in range (4):
        noticias_vandal += ' ' + f'{numero+1}. {noti_vandal[numero].getText()}\n\n'
    
    titulares_nba = espn.select('.contentItem__title.contentItem__title--hero.contentItem__title--video')
    noticias_nba = ''''''
    for titular_nba in range(len(titulares_nba)):
        noticias_nba += ' ' + f'{titular + 1}. {titulares_nba[titular_nba].getText()}\n\n'
            
    
    dolares_compra = dolar_hoy.select ('.val')
    dolar_blue_compra = dolares_compra[0].getText()
    dolares_venta = dolar_hoy.select ('.val')
    dolar_blue_venta = dolares_venta[1].getText()    

    import datetime
    
    #desde = email
    #destinatario = input ('Ingrese una la dirección a donde la quiera enviar: ')

    asunto = f'Anuncios del día: {datetime.date.today()}'
    message = f''' Actualidad Argentina:
    Infobae: 
    {titulo[0].getText()}: 
{titular[0].getText()}

    Pagina12:
    {titulo_2[0].getText()}:
{titular_2[0].getText()}

    Todo Noticias: 
    {titulo_3[0].getText()}:    
{titular_3[0].getText()}
    
                Actualidad vandal:
{noticias_vandal}
                Actualidad Nba:
{noticias_nba}
                
Precio de dolares blue:
    Compra: {dolar_blue_compra}
    Venta: {dolar_blue_venta}
    '''
    print (message)
    msg = 'Asunto: ' + asunto + '\n' + message
    
    #smt_obj.sendmail(desde, destinatario, msg)