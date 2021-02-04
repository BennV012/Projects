
#Manipulation en selenium/webdriver pour faire les étapes d'actualiser la page de la ps5 d'amazon toutes les 5 secondes, puis acheter lorsque disponible au prix souhaité.


from selenium import webdriver
from datetime import datetime
import winsound
import time
def make_noise():
  duration = 1000# milliseconds
  freq = 440  # Hz
  winsound.Beep(freq, duration)

email='email'
mdp='mdp'

n=0
print('Programme disque débuté à: ', datetime.now())

driver = webdriver.Chrome('chromedriver')
while n==0:
    driver.get('https://www.amazon.ca/-/3005720/dp/B08GSC5D9G')
    try:
      a= float(driver.find_element_by_id('priceblock_ourprice').text[4: ])  
      if a<=631:
        driver.find_element_by_xpath('//*[@id="buy-now-button"]').click() #buynow
        print('la ps5 est sortie à: ', datetime.now())
        n=1
      else:
        time.sleep(5)
    except :
      #winsound.Beep(200,500)
      #winsound.Beep(300,500)
      #winsound.Beep(400,500)
      time.sleep(5)

winsound.Beep(700,500)
try:
  driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('email') #email
  driver.find_element_by_xpath('//*[@id="continue"]').click() #continue
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('mdp') #mot de passe
  driver.find_element_by_xpath('//*[@id="signInSubmit"]').click() #sign-in
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input').click() #passer la commande ---- ACHAT!!!
  print('la commande est passée à: ', datetime.now())
  winsound.Beep(200,500)
  winsound.Beep(300,500)
  winsound.Beep(400,500)
  winsound.Beep(500,500)
  winsound.Beep(600,5500)
except:
    print('ERREUR SURVENUE À: ', datetime.now())
    winsound.Beep(800,10000)

 



