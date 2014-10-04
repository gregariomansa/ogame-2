from ogame import OGame
import smtplib 

def send_mail(mailserver, fromaddr, passwd, toaddr, obj, msg):

    headers=["from: Anonymous <plop@inconnu.com>",
	    "subject: "+obj,
	    "content-type: text/html"]
    headers = "\r\n".join(headers)

    server = smtplib.SMTP(mailserver)
    server.starttls()
    server.login(fromaddr, passwd)
    server.sendmail(fromaddr,toaddr, headers+ "\r\n\r\n" + msg)
    server.quit()

if __name__=="__main__":

#global configuration
    game = OGame('', '', '')
    
    mailserver='smtp.gmail.com:587'
    fromaddr=''
    toaddr=''
    passwd=''
    obj="[OGAME ALERTE] attaque a %s"
    msg="""Attention, vous etes attaque par un joueur
    <br/>origine : %s
    <br/>destination : %s
    <br/>arrivee prevue : %s
    <br/>%s"""
  
#surveillance of your account
    if game.is_under_attack():
        attacks = game.get_attacks()
        for attack in attacks:
            origin = attack.get('origin')
            dest = attack.get('destination')
            arrival = attack.get('arrival_time')
            compo = attack.get('composition')
            msgFinal = msg%(origin, dest, arrival, compo)
            objFinal = obj%arrival
            #print msgFinal
            send_mail(mailserver, fromaddr, passwd, toaddr, objFinal, msgFinal)
    
#watch all vailable resources
    s = game.get_planet_ids()
    print s
    
    metal=0
    cristal=0
    deuterium=0
    for i in s:
	res=game.get_resources(i)
	metal+=res['metal']
	cristal+=res['crystal']
	deuterium+=res['deuterium']

    print "metal:"+str(metal)+" - cristal:"+str(cristal)+" - deuterium:"+str(deuterium)
    
    print "Logout"
    game.logout()    
