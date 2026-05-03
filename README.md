# Free Fire Player Info API

## English
### Description
A high-performance Python API designed to fetch Garena Free Fire player statistics and information. It features secure AES encryption, Protobuf decoding, and a robust background token management system.

### Features
- **Token Auto-Refresh**: Background thread ensures credentials never expire without memory leaks.
- **Encryption**: Built-in AES-CBC encryption/decryption for secure API communication.
- **Data Parsing**: Converts Protobuf binary responses into human-readable JSON.
- **Production Ready**: Flask-based with error handling and PEP 8 compliance.

### Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Configure keys in `config.py`.
3. Run: `python main.py`

---

## العربية
### الوصف
واجهة برمجة تطبيقات عالية الأداء لجلب بيانات لاعبي فري فاير. تتميز بتشفير AES ومعالجة Protobuf ونظام تحديث تلقائي للرموز.

### المميزات
- **تحديث التوكن**: خيط خلفي (ثريد) لضمال استمرارية العمل.
- **تشفير آمن**: استخدام خوارزمية AES-CBC.
- **تحليل Protobuf**: تحويل البيانات الثنائية إلى JSON قابل للقراءة.

### التثبيت
1. `pip install -r requirements.txt`
2. تعديل المفاتيح في `config.py`.
3. `python main.py`