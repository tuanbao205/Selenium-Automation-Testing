# Selenium Automation Testing

Dự án thực hành kiểm thử tự động giao diện web bằng **Selenium WebDriver**, **Python** và **pytest** trên website demo [SauceDemo](https://www.saucedemo.com/).

## 1. Mục tiêu

- Làm quen với Selenium WebDriver để tự động hóa thao tác trên trình duyệt.
- Viết và tổ chức test case bằng pytest.
- Kiểm tra các chức năng đăng nhập và thao tác giỏ hàng.
- Ghi nhận kết quả kiểm thử và đánh giá hoạt động của các chức năng.

## 2. Công nghệ sử dụng

- **Python 3.10+**
- **Selenium WebDriver 4**
- **pytest**
- **Google Chrome**

## 3. Các test case

| ID | Test case | Kết quả mong đợi |
|---|---|---|
| TC01 | Đăng nhập với tài khoản hợp lệ | Chuyển đến trang Products |
| TC02 | Đăng nhập với mật khẩu không hợp lệ | Hiển thị thông báo lỗi đăng nhập |
| TC03 | Kiểm tra danh sách sản phẩm | Hiển thị tiêu đề Products và danh sách sản phẩm |
| TC04 | Thêm sản phẩm vào giỏ hàng | Số lượng trên biểu tượng giỏ hàng là 1 |
| TC05 | Xóa sản phẩm khỏi giỏ hàng | Sản phẩm được xóa và biểu tượng số lượng biến mất |

**Tài khoản demo SauceDemo:**

- Username: `standard_user`
- Password: `secret_sauce`

## 4. Cấu trúc dự án

```text
Selenium-Automation-Testing/
├── tests/
│   └── test_saucedemo.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Cài đặt và chạy chương trình

### Bước 1: Clone repository

```bash
git clone https://github.com/tuanbao205/Selenium-Automation-Testing.git
cd Selenium-Automation-Testing
```

### Bước 2: Tạo môi trường ảo

Trên Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Bước 3: Cài đặt thư viện

```bash
python -m pip install -r requirements.txt
```

### Bước 4: Chạy kiểm thử

Đảm bảo Google Chrome đã được cài đặt, sau đó chạy:

```bash
pytest -v
```

Hoặc chỉ chạy file test:

```bash
pytest -v tests/test_saucedemo.py
```

## 6. Kết quả kiểm thử

Dự án bao gồm 5 test case tập trung vào chức năng đăng nhập, hiển thị sản phẩm và quản lý giỏ hàng.

| Nội dung | Mô tả |
|---|---|
| Tổng số test case | 5 |
| Công cụ thực thi | pytest |
| Công cụ tự động hóa | Selenium WebDriver |
| Kết quả thực tế | Cập nhật sau khi chạy kiểm thử |

**Lưu ý:** Chạy `pytest -v` để xác định số lượng test thành công hoặc thất bại trong môi trường thực tế.

## 7. Kết luận

Dự án giúp làm quen với kiểm thử tự động giao diện web bằng Selenium WebDriver và tổ chức test case bằng pytest. Các test case được xây dựng nhằm kiểm tra những chức năng cơ bản của website SauceDemo, đồng thời tạo nền tảng để mở rộng kiểm thử các chức năng như thanh toán, sắp xếp sản phẩm và đăng xuất.
