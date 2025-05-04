1.Kamera Görüntüsü Yakalama (cv2.VideoCapture)
→ Kameradan anlık görüntü alınarak işleniyor.
→ Kamera açılıyor, bir kare okunuyor ve hemen işleniyor.
→ Bu adım, görüntü işlemeye girişin ilk adımıdır.
2.BGR'den RGB'ye Renk Dönüşümü (cv2.cvtColor(frame,
cv2.COLOR_BGR2RGB))
→ OpenCV kameradan görüntüleri BGR (Mavi-Yeşil-Kırmızı) formatında alır.
→ Ancak PIL ve tkinter gibi araçlar RGB (Kırmızı-Yeşil-Mavi) formatını ister.
→ Bu yüzden görüntü işlenmeden önce renk kanalları doğru sıralanıyor.
→ Bu bir renk alanı dönüşüm işlemidir.
3.Görüntü Yeniden Boyutlandırma (img.resize((300,
300)))
→ Kameradan alınan görüntüler sabit boyutta (300x300) gösteriliyor.
→ Bu işlemle farklı çözünürlüklerdeki kareler GUI'ye düzgün oturuyor.
→ Ölçekleme (Resizing) işlemi yapılıyor.
4.Görüntüden Yüz Özelliklerini Çıkarma ve Karşılaştırma
(DeepFace.find)
→ DeepFace, verilen bir görüntüdeki yüzleri tespit eder ve yüzün karakteristik
özelliklerini çıkarır (embedding işlemi).
→ Daha sonra veritabanındaki kayıtlı yüzlerle karşılaştırır.
→ Bu arka planda bir yüz tespiti (face detection) ve özellik çıkarımı (feature
extraction) işlemi yapar.
→ Ayrıca bir benzerlik ölçümü yapılarak yüzün eşleşip eşleşmediği hesaplanır.
5.Geçici Görüntü Kaydetme (cv2.imwrite)
→ Kameradan alınan kare geçici olarak temp.jpg olarak kaydediliyor.
→ Bu dosya daha sonra tanıma için kullanılıyor.
→ Bu adım, görüntü dosyası oluşturma ve görüntüyü diske yazma işlemi içerir
Sistem Gereksinimleri
Bileşen Gereken Özellik
İşletim Sistemi Windows 10 veya üstü, Linux,
macOS
Python Sürümü Python 3.7 veya üstü
RAM Minimum 4 GB (8 GB önerilir)
Kamera USB veya dahili web kamera
Gerekli
Kütüphaneler
OpenCV, face_recognition, numpy
Sistem Mimarisi
Aşağıdaki adımlardan oluşan modüler bir yapı kullanılmıştır:
1. Veri Toplama: Kullanıcının yüz fotoğrafları kameradan alınarak
"dataset/" klasörüne kaydedilir.
2. Yüz Kodlaması: face_recognition ile bu yüzlerin matematiksel
karşılıkları çıkarılır ve .pkl dosyasına kaydedilir.
3. Gerçek Zamanlı Tanıma: Kamera akışı OpenCV ile başlatılır, algılanan
yüzler daha önce kaydedilmiş kodlamalarla karşılaştırılır.
4. Sonuç Gösterimi: Eşleşen kişinin adı görüntü üzerine yazılır. Eşleşme
yoksa “Bilinmeyen” ibaresi gösterilir.
