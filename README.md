# Proje CLI7
Python ile geliştirilmiş, komut satırında çalışan OBS (obs.yeditepe.edu.tr) portu.
<pre>

               _   _ ______
              | | (_)____  |
         ___  | |  _    / /
        / __| | | | |  / /
       | (__  | | | | / /
        \___| |_| |_|/_/

</pre>
CLI7 (Command-Line7) Emrecan ÖKSÜM tarafından Proof-of-Concept amaçlı 2022 tarihinde geliştirilmiştir.
Yeditepe M7 API Endpointleri üzerinden OBS ile iletişime geçip talep edilen öğrenci bilgilerini getirebilen
bu uygulama tamamen deneysel olup, herkes tarafından kullanılması doğal olarak amaçlanmamıştır. Fakat belirtilen
özellikleri tam anlamıyla sağlayabilmektedir. İlerleyen zamanlarda API Endpointler üzerinde yapılacak bir
değişiklik, CLI7'nin işleyişini bozabilir. Bu durumda projenin kodlarını düzenleyip pull request iletebilirsiniz.

**ÖZELLİKLER
* Akademik Bilgileri, Dersleri, Harf Notlarını komut satırında görebilme
* Ders programını komut satırında görebilme
* OBS Mesajlarını komut satırından okuyabilme
* Öğrenci bilgilerini (CGPA, ECTS, Krediler gibi) komut satırından görebilme

**GEREKSİNİMLER
* \>=Python 3.8
* Urllib3 (pip3 install urllib3)
* Requests (pip3 install requests)
* Colorama (pip3 install colorama)

Bu proje geliştirmeye açıktır.