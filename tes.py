from time import sleep
print(' .......   .        .........  .......  .........  ....... ') 
sleep(0.5)
print('(  ...  ) ( \       \..   ../ (  .... \ \..   ../ (  ...  )')
sleep(0.5)
print('| (   ) | | (          ) (    | (    \/    ) (    | (   ) |')
sleep(0.5)
print('| (...) | | |          | |    | |          | |    | (...) |')
sleep(0.5)
print('|  ...  | | |          | |    | |          | |    |  ...  |')
sleep(0.5)
print('| (   ) | | |          | |    | |          | |    | (   ) |')
sleep(0.5)
print('| )   ( |_| (..../\....) (....| (..../\....) (....| )   ( |')
sleep(0.5)
print('|/     \(_|.......(_).......(_|.......(_).......(_)/     \|')
sleep(1)                                                        

print ("import module")
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import wikipedia
import datetime
import sys
import re
import random,os
import smtplib

print("import module selesai!!")

def alicia(text):
	sn = gTTS(text,lang="id")
	sn.save("sound.mp3")
	playsound("sound.mp3")
	print("Alicia :",text)

print("Salam..")
def greeting():
	ch = int(datetime.datetime.now().hour)
	if (ch >= 0 and ch < 12):
		alicia("Selamat pagi!")
	if (ch >= 12 and ch < 18):
		alicia("Selamat siang!")
	if (ch >= 18 and ch != 0):
		alicia("Selamat malam!")
greeting()

alicia("namaku alicia, ada yang bisa saya bantu ?")

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:

		print("\nMendengarkan...")
		r.pause_threshold = 1
		audio = r.listen(source)
		try:
			query = r.recognize_google(audio,language="id-ID")
			print("Kamu:",query)
		except:
			alicia("Maaf, aku tidak mengerti apa yang kamu katakan , tolong ketikkan perintah ")
			query = input("Perintah : ")
	return query
#credential email
def send_email(recipient,subject,pesan):
	user = "username@gmail.com" # ganti jadi username gmail kalian
	pawd = "password" #ganti jadi password gmail kalian
	From = user
	to = recipient if isinstance(recipient, list) else [recipient]
	subj = subject
	body = pesan
	try:
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (From, ", ".join(to), subj, body)
		server_ssl = smtplib.SMTP_SSL("smtp.gmail.com",465)
		server_ssl.ehlo()
		server_ssl.login(user,pawd)
		server_ssl.sendmail(From,to,message)
		server_ssl.close()
		alicia('berhasil mengirim email')
	except Exception as a:
		print(a)
		alicia('gagal mengirim email')
		pass

def wiki(kt):
	wikipedia.set_lang("id")
	res = wikipedia.summary(kt,sentences=2)
	alicia(res)

def predict(kata):
	kabar = ['kabarmu','kabar','keadaanmu','keadaan']
	umur = ['umurmu','umur']
	pembuat = ['pembuat mu','pencipta mu','developer mu','programmer mu','program','bahasa']
	jawabP = ['aku dibuat dengan bahasa program python, pembuatku adalah security007','program python, dengan itulah aku dibuat, security007 adalah orang yang mengembangkanku','aku dibuat dengan menggunakan bahasa pemrograman python, security007 adalah orang yang mengembangkanku']
	jawabU = ['maaf itu rahasia','yang pasti aku lebih muda darimu','tanyakan saja kepada pembuatku']
	jawabK = ["hem aku tidak pernah seceria ini","kabarku baik baik saja","aku merasa bahagia hari ini"]
	for ta in kabar:
		if ta in kata:
			alicia(random.choice(jawabK))
	for um in umur:
		if um in kata:
			alicia(random.choice(jawabU))
	for pem in pembuat:
		if pem in kata:
			alicia(random.choice(jawabP))	
				
	if 'musik' in kata:
		alicia("Ketikkan letak direktori musikmu")
		dir = input("Direktori : ")
		try:
			for play in os.listdir(dir):
				if play.endswith('mp3'):
					try:
						alicia('memutar musik !')
						alicia('selamat mendengarkan')
						playsound(dir+"/"+play)
					except Exception as a:
						print(a)
				else:
					alicia("mencari file lagu !")
		except Exception as a:
			print("Direktori tidak ditemukan")
	if 'email' in kata:
		alicia("siapa penerima emailnya ?")
		pen = input("Penerima : ")
		alicia("tuliskan subjectnya ")
		sub = input('subject : ')
		alicia("tuliskan pesan yang ingin dikirim")
		pes = input('Pesan : ')	
		alicia("sedang mengirim email")
		send_email(pen,sub,pes)		
			
	if 'buka' in kata and 'exploit database' not in kata:	
		pecah = kata.split()
		if len(pecah) != 1:
			alicia('oke')
			webbrowser.open("http://"+pecah[1]+".com")
		else:
			alicia('tidak bisa membuka mesin pencari')
			pass
	if 'wiki' in kata:	
		pecah = kata.split('wiki')
		if len(pecah) != 1:
			alicia('oke')
			wiki(pecah[1])
		else:
			alicia('tidak bisa membuka wikipedia')
			pass
	if 'exploit database' in kata:
		alicia('oke')
		webbrowser.open("http://exploit-db.com")
	if 'cari' in kata:
		pecah = kata.split('cari')
		if len(pecah) != 1:
			alicia('oke')
			webbrowser.open("https://www.google.com/search?q="+pecah[1]+"&ie=utf-8&oe=utf-8&client=firefox-b-ab")
		else:
			alicia('tidak bisa membuka mesin pencari')
	
	alicia("menunggu perintah selanjutnya")
def main():
	
	a = 1
	while a > 0:
		qr = command()
		if "stop" in qr:
			alicia("Sampai jumpa lagi")
			sys.exit()
		predict(qr.lower())
		
if __name__ == "__main__":
	main()
		
			
