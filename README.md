# 🍛 ระบบจัดการเมนูอาหาร "อร่อยเกินเบอร์"

เว็บแอปพลิเคชัน Django สำหรับกรณีศึกษา **ระบบจัดการเมนูอาหาร + ระบบสั่งอาหาร (Order)** ของร้านผัดกะเพรารวมมิตร

## ✨ ฟีเจอร์

| ฟีเจอร์ | รายละเอียด |
|---|---|
| 🍽️ CRUD เมนูอาหาร | เพิ่ม / แสดง / แก้ไข / ลบ ผ่าน Django ModelForm |
| 🔍 ค้นหา + กรอง | ค้นหาจากชื่อ/รายละเอียด + กรองตามหมวดหมู่ |
| 👀 หน้ารายละเอียดเมนู | ดูข้อมูลเต็มของแต่ละเมนู + เมนูแนะนำใกล้เคียง |
| 🖼️ อัปโหลดรูปภาพ | ImageField + Pillow พร้อมแสดงบนหน้าเว็บ |
| 🧾 ระบบสั่งอาหาร | เปิดออเดอร์ตามโต๊ะ เพิ่ม/ลด/ลบรายการ + เครื่องเคียง |
| 🛵 ระบบเดลิเวอร์รี่ | เปิดออเดอร์แบบส่งถึงบ้าน — เก็บชื่อ/ที่อยู่/เบอร์ + ค่าจัดส่ง |
| 📦 สถานะการจัดส่ง | แยกสถานะไรเดอร์ (รอจัดส่ง → กำลังจัดส่ง → จัดส่งแล้ว) + ระบุชื่อไรเดอร์ |
| 📋 แดชบอร์ดเดลิเวอร์รี่ | หน้าเฉพาะ Staff ดู/จัดการ/ติดตามออเดอร์เดลิเวอร์รี่ทั้งหมด |
| 🔢 รหัสออเดอร์รายวัน | รหัสแสดงผลสั้น `#001` รีเซ็ตใหม่ทุกวัน (เก็บเต็ม `YYYYMMDD-001` ไม่ซ้ำแม้ลบออเดอร์) |
| 💰 คำนวณราคารวม | Subtotal ต่อรายการ + ยอดรวมทั้งโต๊ะอัตโนมัติ |
| 🖨️ ใบเสร็จรับเงิน | หน้ายกตัวอย่างใบเสร็จ + ปุ่มพิมพ์ (Print) |
| 📊 Dashboard + กราฟ | สถิติยอดขายวันนี้/สัปดาห์/เดือน + กราฟ Chart.js 7 วัน |
| 📤 ส่งออกรายงาน | Export ยอดขายเป็น CSV และ Excel (.xlsx) |
| 📱 QR โต๊ะ | QR Code ประจำโต๊ะ เชื่อมเข้าหน้ารายงานสั่งอาหาร |
| 🔔 Notification | badge แจ้งเตือนออเดอร์ค้างให้ Staff ในแถบเมนู |
| 🔗 REST API | Django REST Framework — `/api/menus/`, `/api/orders/`, ... |
| 🗺️ แผนที่ร้าน | แผนที่ Google Maps (embed ฟรี ไม่ต้องใช้ Key) ในหน้าติดต่อ / ตั้งค่าเดลิเวอร์รี่ / หน้าออเดอร์ |
| 📄 SEO | `robots.txt` + `sitemap.xml` |
| 🛡️ Validation | ราคา > 0, ชื่อเมนูไม่ซ้ำ, ไฟล์รูป ≤ 10MB, เลขโต๊ะ 1-999 |
| 🔐 Backend Admin | จัดการข้อมูลทั้งหมดผ่าน Django Admin |
| ✅ Automated tests | 27 test cases (Model / Form / View / Export / API / Delivery) |
| 🐳 Docker | พร้อม Dockerfile + docker-compose สำหรับ deploy |

## 🛠️ เทคโนโลยี

Python 3.14 · Django 6.0 · SQLite · Bootstrap 5 · Google Maps Embed · Chart.js · Django REST Framework · Pillow · openpyxl · gunicorn

## 🔌 การเชื่อมต่อ API ภายนอก

ระบบมีการเชื่อมต่อ API ภายนอก (ใช้เพื่อแจ้งเตือน + คำนวณพิกัดจัดส่ง)

| API | ใช้ทำอะไร | เจอได้ที่ |
|---|---|---|
| **Google Maps Embed** (`https://maps.google.com/maps?output=embed`) | แสดงแผนที่ตำแหน่งร้าน/ปลายทางบนหน้าเว็บ (ฟรี ไม่ต้องใช้ API Key) | `myapp/templates/` → `contact.html`, `delivery/delivery_settings.html`, `order/order_detail.html` |
| **Line Notify** (`https://notify-api.line.me`) | ส่งแจ้งเตือนออเดอร์/จองโต๊ะ/รีวิวใหม่ไปที่ Line | `myapp/services.py` → `notify_line()` / `notify_email()` |
| **Nominatim / OpenStreetMap** (`https://nominatim.openstreetmap.org`) | เปลี่ยนที่อยู่จัดส่ง → พิกัด GPS แล้วคำนวณระยะทาง/ค่าส่งอัตโนมัติ | `myapp/services.py` → `geocode_address()` + ปุ่ม "ค้นหาพิกัดที่อยู่" |

**หลักการเขียน (ในโปรเจกต์นี้):**

1. เรียกผ่านไลบรารี `requests` เสมอ และจำกัด `timeout` ระยะสั้น (เช่น 8 วินาที)
2. จับ error ทั้งหมดแล้วคืนค่าแบบ "ไม่พังระบบ" (เช่น คืน `False`/`None` แทนการ raising)
3. เซฟงานด้านธุรกิจไว้ตั้งแต่แรก — ตัวอย่าง: `notify_line()` ตัดสินใจล้มเหลวก็แค่ข้ามการแจ้งเตือน ไม่ทำให้สั่งอาหารพัง
4. API ข้างนอกไม่ได้ถูกยิงในเทสต์ — เทสต์จะ `mock` `requests.get/post` ทั้งหมด (ดู `myapp/tests.py`)
5. ตั้งค่าการเชื่อมต่อ (token/key) ผ่าน Database หรือตัวแปรสภาพแวดล้อม ไม่ฝังในโค้ด

**วิธีเพิ่ม API ภายนอกตัวใหม่:** เขียนฟังก์ชันใน `myapp/services.py` (ใช้ `requests` + timeout), ผูกใช้งานใน `views.py`, แล้วครอบด้วยเทสต์แบบ mock — pattern เดียวกับ `geocode_address()`

## 🚀 วิธีติดตั้งและรัน (Dev)

```bash
# 1. สร้าง virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows

# 2. ติดตั้ง packages
pip install -r requirements.txt

# 3. สร้างฐานข้อมูล
python manage.py migrate

# 4. (ทางเลือก) สร้างข้อมูลเมนูตัวอย่าง 12 เมนูพร้อมรูป
python manage.py seed_menu

# 5. สร้างผู้ใช้ admin
python manage.py createsuperuser

# 6. รันระบบ
python manage.py runserver
```

เปิดเบราว์เซอร์ที่ `http://127.0.0.1:8000/`

## 🔐 ล็อกอินด้วย Google (OAuth 2.0)

ระบบใช้ **django-allauth** ร่วมกับปุ่ม Google บนหน้าเข้าสู่ระบบ/สมัครสมาชิก ซึ่งถือว่า
บัญชีจาก Google ผ่านการยืนยันอีเมลแล้ว จึงไม่ต้องรอผู้ดูแลอนุมัติ (ต่างจากการสมัครด้วยฟอร์ม)

**ขั้นตอนตั้งค่า:**

1. สร้าง OAuth Client ที่ [Google Cloud Console → Credentials](https://console.cloud.google.com/apis/credentials)
   - ประเภท: **Web application**
   - Authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`
     (Production เปลี่ยนเป็น `https://<โดเมนของคุณ>/accounts/google/login/callback/`)
2. ตั้งค่าตัวแปรสภาพแวดล้อม (คัดลอกจาก `.env.example`):
   - `GOOGLE_OAUTH_CLIENT_ID` — เช่น `xxxxx.apps.googleusercontent.com`
   - `GOOGLE_OAUTH_CLIENT_SECRET` — เช่น `GOCSPX-xxxxxxxx`
3. สร้าง `SocialApp` ในฐานข้อมูล (รันอัตโนมัติตอน Docker start):
   ```bash
   python manage.py create_google_app
   ```
4. ทดสอบ: เปิด `/login/` แล้วกด **เข้าสู่ระบบด้วย Google**

**adapter** อยู่ที่ `myapp/accounts.py` ทำงานเพิ่มเติมให้อัตโนมัติ:

| สถานการณ์ | พฤติกรรม |
|---|---|
| ยังไม่มีบัญชีในระบบ | สร้างบัญชีใหม่ทันที (อีเมลยืนยันแล้ว ไม่ต้องรออนุมัติ) |
| อีเมล Google ตรงกับบัญชี username/รหัสผ่าน ที่สมัครไว้แล้ว | เชื่อมบัญชีเข้ากัน ไม่สร้างบัญชีซ้ำซ้อน แล้วเข้าสู่ระบบทันที |
| บัญชีเดิมค้าง "รออนุมัติ" และอีเมลตรงกับ Google | เปิดใช้งานบัญชีโดยอัตโนมัติ (Google ยืนยันอีเมลแล้ว) |
| ยกเลิก/เกิดข้อผิดพลาดจากหน้า Google | แสดงหน้าข้อความภาษาไทย พร้อมลิงก์กลับหน้าเข้าสู่ระบบ |

## 🐳 วิธีรันด้วย Docker (Production)

```bash
docker compose up --build
```

ตัวแปรสภาพแวดล้อมที่ใช้: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_SECURE`

## 🗺️ URL หลัก

| URL | หน้า |
|---|---|
| `/` | หน้าหลัก |
| `/menu/` | รายการเมนู (ค้นหา/กรอง/แบ่งหน้า) |
| `/menu/<id>/detail/` | รายละเอียดเมนู |
| `/orders/` | ระบบสั่งอาหาร — เปิดออเดอร์ (ทานในร้าน / เดลิเวอร์รี่) |
| `/orders/<id>/` | จัดการออเดอร์ (เพิ่ม/ลบรายการ + ราคารวม + ข้อมูลจัดส่ง) |
| `/orders/<id>/receipt/` | ใบเสร็จรับเงิน (พิมพ์ได้) |
| `/delivery/` | แดชบอร์ดจัดการเดลิเวอร์รี่ (Staff) |
| `/table/<no>/qr/` | QR code ประจำโต๊ะ |
| `/export/orders/csv/` | Export ยอดขาย CSV (Staff) |
| `/export/orders/xlsx/` | Export ยอดขาย Excel (Staff) |
| `/api/menus/` | REST API — รายการเมนู (JSON) |
| `/api/orders/` | REST API — ออเดอร์ + ใช้คูปอง (`apply_coupon` / `remove_coupon`) |
| `/api/deliveries/` | REST API — ข้อมูลเดลิเวอร์รี่ (ข้อมูลส่วนตัวถูกซ่อน) |
| `/api/reservations/` | REST API — จองโต๊ะ (สร้างได้ไม่ต้องล็อกอิน, จำกัด 5 ครั้ง/ชม.) |
| `/api/coupons/` | REST API — คูปอง + ตรวจสอบรหัส (`validate`) |
| `/api/ingredients/` | REST API — วัตถุดิบ/สต็อก (Staff เท่านั้นที่แก้) |
| `/api/recipes/` | REST API — สัดส่วนวัตถุดิบของเมนู (Staff) |
| `/api/reviews/` | REST API — รีวิว/ให้คะแนนเมนู |
| `/api/points/rewards/` | REST API — สิทธิ์แลกคะแนน + `redeem` (แลกเป็นคูปอง) |
| `/api/points/transactions/` | REST API — ประวัติคะแนนของตัวเอง |
| `/api/notifications/` | REST API — แจ้งเตือน + `read` / `read_all` |
| `/api/profile/me/` | REST API — โปรไฟล์ตัวเอง (คะแนน/สิทธิ์สมาชิก) |
| `/api/store/` | REST API — ข้อมูลร้าน/ค่าส่ง/แผนที่ (สาธารณะ) |
| `/api/` | DRF browsable API (เปิดดู endpoint ทั้งหมดในเบราว์เซอร์) |
| `/sitemap.xml`, `/robots.txt` | SEO |
| `/admin/` | Backend Admin |

## 🧩 โครงสร้าง Model

- **MenuItem** — ชื่อเมนู, หมวดหมู่ (Choices), ราคา (Decimal), ระดับความเผ็ด (Choices), รายละเอียด (Text), สถานะขาย (Boolean), วันที่เพิ่ม (Date), รูปภาพ (Image)
- **Order** — เลขโต๊ะ (ไม่จำเป็นสำหรับเดลิเวอร์รี่), ประเภทออเดอร์ (ทานในร้าน/เดลิเวอร์รี่), สถานะ (Choices), วิธีชำระ, เวลาชำระ, เวลาสั่ง + property `total_price` (รวมค่าส่ง), `item_count`, `is_paid`, `table_display`, `delivery_fee`
- **OrderItem** — FK Order, FK MenuItem, จำนวน, หมายเหตุ, M2M เครื่องเคียง + property `subtotal`
- **Delivery** — ข้อมูลจัดส่ง 1:1 กับ Order: ชื่อผู้รับ, เบอร์โทร, ที่อยู่, ค่าจัดส่ง, สถานะการจัดส่ง (รอจัดส่ง/กำลังจัดส่ง/จัดส่งแล้ว/ยกเลิก), ชื่อไรเดอร์, เบอร์ไรเดอร์, หมายเหตุ, เวลาจัดส่งสำเร็จ
- **Category** — หมวดหมู่หลัก (FK จาก MenuItem)
- **AddOn** — เครื่องเคียง (ข้าวเพิ่ม, ไข่ดาว, ...)
- **Profile** — รูปโปรไฟล์/รูปปก ของผู้ใช้

## 🧪 รัน Test

```bash
python manage.py test
```

---
พัฒนาโดย นักศึกษา KPRU © 2026