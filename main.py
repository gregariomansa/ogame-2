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
    game = OGame('antares', 'godjo', 'polkaudio')
    
    mailserver='smtp.gmail.com:587'
    fromaddr='poloplop6@gmail.com'
    toaddr='stephane.dorre@gmail.com'
    passwd='poiuazer'
    obj="[OGAME ALERTE]"
    msg="Attention, vous etes attaque par qqun? arrivee prevue : xxxx"
  
#surveillance of your account
    #if game.is_under_attack():
    #send_mail(mailserver, fromaddr, passwd, toaddr, obj, msg)
    
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
