
# Apartman Yönetim Sistemi
![5](https://github.com/user-attachments/assets/04cbb472-8575-4cc4-85db-1247282b92c6)
![gider](https://github.com/user-attachments/assets/95d4e3ce-c68b-497c-8ec5-baab887250ae)
![2](https://github.com/user-attachments/assets/113c943a-b535-48f0-9d03-45cb49804750)
![Gelir](https://github.com/user-attachments/assets/1446a43a-49cb-4239-87cb-73a4198f1281)
![7](https://github.com/user-attachments/assets/11cabe7c-4e94-461e-8542-a64224f37261)


Bu proje, apartman ve sitelerin gelir-gider takibini yapmak için oluşturulmuş basit bir fullstack uygulamadır. FastAPI backend, PostgreSQL veritabanı ve HTML/JS frontend ile hazırlanmıştır.

## Özellikler

- Apartman/site kayıt yönetimi
- Gelir takibi (aidat, kira, vb.)
- Gider takibi (elektrik, su, bakım, vb.)
- Özet rapor ve bakiye görüntüleme
- Basit ve kullanıcı dostu arayüz

## Gereksinimler

- Python 3.7+
- PostgreSQL
- pip

## Kurulum

1. Projeyi bilgisayarınıza klonlayın veya indirin

2. Gerekli Python paketlerini yükleyin:

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

3. PostgreSQL veritabanı oluşturun:

```
CREATE DATABASE apartment_management;
```

4. `database.py` dosyasındaki veritabanı bağlantı bilgilerini düzenleyin:

```python
DATABASE_URL = "postgresql://kullanıcı_adı:şifre@localhost/apartment_management"
```

## Çalıştırma

1. Backend'i başlatın:

```
uvicorn main:app --reload
```

2. Frontend için index.html dosyasını bir web sunucusu üzerinden (örn: Live Server VSCode eklentisi) veya doğrudan tarayıcıda açın.

3. Eğer backend farklı bir portta çalışıyorsa, frontend kodundaki API_URL değişkenini uygun şekilde güncelleyin.

## Kullanım

1. İlk olarak "Yeni Apartman Ekle" butonu ile bir apartman kaydı oluşturun.

2. Sol menüden oluşturduğunuz apartmanı seçin.

3. "Gelir Ekle" ve "Gider Ekle" butonları ile yeni gelir ve gider kayıtları ekleyin.

4. Üst kısımda toplam gelir, gider ve bakiye bilgilerini görüntüleyin.

5. "Gelirler" ve "Giderler" sekmeleri arasında geçiş yaparak detaylı listeleri görüntüleyin.

## Proje Yapısı

```
apartment_management/
│
├── backend/
│   ├── database.py     # Veritabanı bağlantısı ve oturum yönetimi
│   ├── models.py       # SQLAlchemy ORM modelleri
│   ├── schemas.py      # Pydantic şemaları (veri doğrulama)
│   └── main.py         # FastAPI uygulaması ve endpoint'ler
│
├── frontend/
│   └── index.html      # HTML, CSS ve JavaScript içeren tek sayfa uygulama
│
└── README.md           # Projeyi açıklayan dokümantasyon
```
#   a p a r t m e n t _ a n d _ s i t e _ m a n a g e m e n t 
 
 
