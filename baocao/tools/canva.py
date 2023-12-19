from PIL import Image
import os

def process_images(folder_path):
    # Lấy danh sách tất cả các tệp trong thư mục
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # Xác định đường dẫn đầy đủ của tệp ảnh
        image_path = os.path.join(folder_path, file_name)

        # Chỉ xử lý các tệp ảnh (loại bỏ các tệp không phải ảnh)
        if os.path.isfile(image_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Mở ảnh sử dụng Pillow
            image = Image.open(image_path)

            # Kiểm tra kích thước ảnh
            width, height = image.size
            new_size = (500, 500)

            # Tính toán kích thước mới và vị trí để chèn ảnh vào hình vuông
            new_width = max(width, new_size[0])
            new_height = max(height, new_size[1])
            left = (new_width - width) // 2
            top = (new_height - height) // 2

            # Tạo hình vuông mới với kích thước 500x500 và màu nền trắng
            new_image = Image.new("RGB", new_size, (255, 255, 255))

            # Chèn ảnh gốc vào vị trí đã tính toán
            new_image.paste(image, (left, top))

            # Lưu ảnh mới
            new_image.save(image_path)

            print(f"Processed: {file_name}")

# Đường dẫn đến thư mục chứa ảnh
folder_path = r'C:\Users\vvn20206205\Desktop\solutions\document\baocao\pictures\DaNgonNguVaCSDL\data'

# Gọi hàm xử lý ảnh
process_images(folder_path)
