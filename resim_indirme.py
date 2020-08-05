from imutils import paths
import argparse
import requests
import cv2
import os

# argümanları yani urlleri bölecek yapıyı oluşturur ve argümanları 
# ayrıştırır 
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="JavaScript koduyla ürettiğimiz URL’leri içeren txt dosyasının yolu.")
ap.add_argument("-o", "--output", required=True,
	help="Google görsellerden indirilecek olan resimlerin indirileceği klasörün yolu.")
args = vars(ap.parse_args())
# girdi dosyasındaki URL lsitesini alır ve toplam indirilen resim sayısını 
# sıfıra eşitleyerek çalışmaya başlar
rows = open(args["urls"]).read().strip().split("\n")
total = 0

# URL'lerin döngüsü
for url in rows:
	try:
		# resim indirmeyi dener
		r = requests.get(url, timeout=60)
		# resmi 00000000.jpg olarak adlandırıp diske kaydeder
		p = os.path.sep.join([args["output"], "{}.jpg".format(
			str(total).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
		# sayacı günceller
		print("[BİLGİ] indirildi: {}".format(p))
		total += 1
    # herhangi bir hatayla karşılaşıldığında alttaki hatayı basar
	except:
		print("[BİLGİ] indirme hatası {}...es geçildi".format(p))

