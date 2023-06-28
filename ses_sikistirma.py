
"""
MUSTAFA YILDIRIM - 190905029 - ÖRÜNTÜ TANIMA PROJE ÖDEVİ

"""

# Ses dosyasında işlem yapmak için gerekli olan pydub kütüphanesinin AudioSegment sınıfını ve grafik çizimleri 
# için gerekli olan matplotlib.pyplot kütüphanesini islem takma adıyla yüklüyorum.

from pydub import AudioSegment
import os
import matplotlib.pyplot as islem

# Ses dosyalarının yolunu ve Sıkıştırılmış ses dosyalarının gideceği yolu belirtiyorum.

sesler = 'Google Speech Commands/_background_noise_/'
sikistirilmisSesler = 'sikistirilmis_sesler/'

# sesler klasöründeki ses dosyalarının listesini döndürüyorum ve sırayla ses değişkenine yüklüyorum.

for ses in os.listdir(sesler):
    
    # Sadece .wav uzantılı ses dosyalarını seçiyorum.
    
    if ses.endswith('.wav'):
        
        # Orijinal ses dosyasını sesDosyasi değişkenine yüklüyorum.
        
        sesDosyasi = AudioSegment.from_wav(os.path.join(sesler, ses))
        
        # Orijinal ses dosyasının grafiğini çiziyorum.
        
        # Grafiğin genişliğini 20, yüksekliğini 4 olarak ayarlıyorum.
        
        islem.figure(figsize=(20,4)) 
        
        # Grafiğin ismini ayarlıyorum.
        
        islem.title("Orijinal Ses Dosyası: {}".format(ses))
        
        # Ses dosyasının frekans grafiğini çiziyorum.
        
        islem.plot(sesDosyasi.get_array_of_samples())
        
        # Ses dosyasının grafiğini gösteriyorum.
        
        islem.show()
        
        # Ses dosyasının örnekleme frekansını yarıya indiriyorum. 
        # Sesin frekansı yarı oranında sıkışınca sesin kapladığı boyut yarıya düşmüş oluyor.
        
        sikistirilmisSesDosyasi = sesDosyasi.set_frame_rate(sesDosyasi.frame_rate // 2)
        
        # Orijinal ses dosyasının grafiğini çiziyorum.
        
        # Grafiğin genişliğini 20, yüksekliğini 4 olarak ayarlıyorum.
        
        islem.figure(figsize=(20,4))
        
        # Grafiğin ismini ayarlıyorum.
        
        islem.title("Sıkıştırılmış Ses Dosyası: {}".format(ses))
        
        # Sıkışıtırılmış ses dosyasının frekans grafiğini çiziyorum.
        
        islem.plot(sikistirilmisSesDosyasi.get_array_of_samples())
        
        # Sıkıştırılmış ses dosyasının grafiğini gösteriyorum.
        
        islem.show()
        
        # Sıkıştırılmış ses dosyalarını sikistirilmisSesler klasörüne  .wav uzantılı olarak kaydediyorum.
        
        ciktiSesAdi = os.path.join(sikistirilmisSesler, ses)
        
        sikistirilmisSesDosyasi.export(ciktiSesAdi, format='wav')


