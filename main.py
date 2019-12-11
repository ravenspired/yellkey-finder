#(c) Anton V, ravenspired

#This program was written without the intention of abuse and by using it you agree to not misuse the program. Abuse includes: Attempting to exploit yellkey, attempted "ddos", or to find personal information.



#Yellkey finder: This script finds yellkeys by taking a common word list, parsing the url, and testing for a 403 error. If one is found, then it records the url in foundyellkeys.txt



import random #Imports random library
import urllib.request #Imports urllib
numberinlist =0 #Variable to keep track of how many we looped
def locatekeys(): #Function definition to recall it
  global numberinlist #Make tracker variable global
  try:#Try loop
    while True:#loop forever until an error
      mywords = open("20k.txt").read().split() #take common english words file and split up the words into an array
      myword = mywords[numberinlist]#define the word from the array using the loop tracker
      print(numberinlist,"/200000")#display progress for impatient users
      numberinlist+=1;#add 1 to the tracker loop
      urllib.request.urlretrieve ('http://yellkey.com/'+myword, "temp.html")#download the webpage of yellkey.com/thewordthatwaschosen
  except:#test if an error occurs. one will occur if yellkey will attempt to redirect the page.
    print("Yellkey found: yellkey.com/"+myword)#print that a yellkey was found
    with open('foundyellkeys.txt', 'a') as file:
      file.write("http://yellkey.com/"+myword+"\n")#save the url of the yellkey in a file
    locatekeys()#rerun the function again

print("Now searching for yellkeys. This will take a while, about an hour if you search all of them.")
locatekeys()