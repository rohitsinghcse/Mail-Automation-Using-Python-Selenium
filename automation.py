from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from generic import readlines_file,read_file, writeFile

path_to_sender = 'sender.txt'
path_to_receiver= 'receiver.txt'
path_to_mailbody = 'mailbody.txt'
path_to_attachment = os.path.join(os.path.dirname(os.path.abspath(__file__)),'attachment.txt')

URL = 'https://gmail.com'

sender_credentials = [p.strip() for p in readlines_file(path_to_sender)] 
receiver_credentails = [p.strip() for p in readlines_file(path_to_receiver)] 
mailbody = read_file(path_to_mailbody)

# Launch browser
driver = webdriver.Chrome()
driver.get(URL)
senderCount = 1
for record in sender_credentials:
    
    username = record.split(',')[0]
    password = record.split(',')[1]
    print(username,password)
    mailInputBox = driver.find_element_by_xpath('//*[@id="identifierId"]')
    mailInputBox.send_keys(username)
    # Click next button
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    # wait 
    time.sleep(5)
    pwdInputBox = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pwdInputBox.send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(8) #time in seconds
    
    receiverCount = 1
    for receiver in receiver_credentails:


        driver.find_element_by_xpath('//*[text()="Compose"]').click()
        
        time.sleep(10)
    
        toField = driver.find_element_by_xpath('//*[@name="to"]')
        toField.send_keys(receiver)
        
        print('receiver----|', receiver)

        subject = driver.find_element_by_xpath('//*[@name="subjectbox"]')
        subject.send_keys(str(senderCount) + ' ROHIT SINGH ' + str(receiverCount))
        
        mailbodyField = driver.find_element_by_xpath('//*[@aria-label="Message Body"][@role="textbox"]')
        mailbodyField.send_keys(mailbody)
       
        writeFile(path_to_attachment, str(senderCount) + ' ROHIT SINGH ' + str(receiverCount))

        attachment = driver.find_element_by_xpath('//*[@name="Filedata"]')
              
        attachment.send_keys(path_to_attachment)
        time.sleep(5)
        sendBtn = driver.find_element_by_xpath('//*[text()="Send"]')
        sendBtn.click()
        time.sleep(10)
       
        receiverCount = receiverCount + 1 
        
    driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a/img').click() 
    driver.find_element_by_xpath('//*[@id="gb_71"] ').click() 
    time.sleep(10)
    driver.find_element_by_xpath('//div[contains(text(),"Use another account")]').click() 
    senderCount = senderCount + 1 
    time.sleep(10)
