# Selenium Automation Testing

Dự án thực hành kiểm thử tự động giao diện web bằng **Selenium WebDriver**, **Python** và **pytest** trên website demo [SauceDemo](https://www.saucedemo.com/).

## 1. Mục tiêu
- Làm quen với Selenium WebDriver để tự động hóa thao tác trên trình duyệt.
- Viết và tổ chức test case bằng pytest.
- Kiểm tra các luồng đăng nhập và thao tác giỏ hàng cơ bản.
- Ghi nhận kết quả chạy kiểm thử và có thể mở rộng thêm test case.

## 2. Công nghệ sử dụng
- Python 3.10 trở lên (khuyến nghị)
- Selenium WebDriver 4
- pytest
- Google Chrome

Selenium Manager có thể tự xử lý việc tìm/tải driver phù hợp trong nhiều môi trường phổ biến; cần có kết nối Internet nếu driver chưa sẵn có.

## 3. Các test case

| ID | Test case | Kết quả mong đợi |
|---|---|---|
| TC01 | Đăng nhập với tài khoản hợp lệ | Chuyển đến trang Products |
| TC02 | Đăng nhập với mật khẩu không hợp lệ | Hiển thị thông báo lỗi đăng nhập |
| TC03 | Kiểm tra danh sách sản phẩm | Tiêu đề Products và danh sách sản phẩm được hiển thị |
| TC04 | Thêm một sản phẩm vào giỏ hàng | Badge giỏ hàng hiển thị số lượng 1 |
| TC05 | Xóa sản phẩm khỏi giỏ hàng | Sản phẩm không còn trong giỏ và badge số lượng biến mất |

Tài khoản demo:
- Username: `standard_user`
- Password: `secret_sauce`

Đây là tài khoản demo công khai của SauceDemo, không dùng mật khẩu cá nhân.

## 4. Cấu trúc dự án

```text
Selenium-Automation-Testing/
├── tests/
│   └── test_saucedemo.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Cài đặt và chạy

### Bước 1: Clone repository

```bash
git clone https://github.com/tuanbao205/Selenium-Automation-Testing.git
cd Selenium-Automation-Testing
```

### Bước 2: Tạo môi trường ảo (khuyến nghị)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn kích hoạt môi trường ảo, có thể chạy trong Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### Bước 3: Cài thư viện

```bash
python -m pip install -r requirements.txt
```

### Bước 4: Chạy kiểm thử

Đảm bảo Google Chrome đã được cài đặt, sau đó chạy:

```bash
pytest -v
```

Chỉ chạy file test:

```bash
pytest -v tests/test_saucedemo.py
```

Mặc định trình duyệt chạy ở chế độ có giao diện để dễ quan sát. Mỗi test tạo và đóng một phiên trình duyệt riêng.

## 6. Kết quả kiểm thử

Chạy `pytest -v` để xem kết quả thực tế trong terminal. **Không ghi trước số lượng test PASS/FAIL** vì kết quả phụ thuộc môi trường, trình duyệt và kết nối mạng.

Sau khi chạy, cập nhật:
- Ngày giờ chạy:
- Môi trường (Python / Chrome):
- Kết quả: ___ passed, ___ failed
- Ảnh chụp terminal: lưu trong thư mục `screenshots/` rồi thêm liên kết ảnh tại đây.

## 7. Kết luận

Bài thực hành minh họa cách dùng Selenium để tự động hóa các thao tác web phổ biến và dùng pytest để tổ chức, thực thi nhiều test case. Có thể phát triển thêm kiểm thử sắp xếp sản phẩm, trang chi tiết, checkout và đăng xuất.
