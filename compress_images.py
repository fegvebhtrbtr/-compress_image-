import os
import sys
from PIL import Image
from io import BytesIO

def compress_image(input_path, output_path, max_size_mb, quality=85, max_resolution=None):
    """
    压缩图片到指定大小以下
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    :param max_size_mb: 最大大小(MB)
    :param quality: 初始质量(1-100)
    :param max_resolution: 最大分辨率(宽, 高)，可选
    """
    max_size_bytes = max_size_mb * 1024 * 1024
    
    with Image.open(input_path) as img:
        # 如果有最大分辨率限制，先调整尺寸
        if max_resolution:
            img.thumbnail(max_resolution, Image.LANCZOS)
        
        # 检查是否需要压缩
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        current_size = buffer.tell()
        
        # 如果已经小于目标大小，直接保存
        if current_size <= max_size_bytes:
            with open(output_path, 'wb') as f:
                f.write(buffer.getvalue())
            return
        
        # 否则调整质量
        min_quality = 10
        max_quality = quality
        best_quality = quality
        
        # 二分查找最佳质量参数
        for _ in range(10):  # 最多尝试10次
            mid_quality = (min_quality + max_quality) // 2
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=mid_quality)
            current_size = buffer.tell()
            
            if current_size <= max_size_bytes:
                best_quality = mid_quality
                min_quality = mid_quality + 1
            else:
                max_quality = mid_quality - 1
        
        # 保存最佳质量图片
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=best_quality)
        with open(output_path, 'wb') as f:
            f.write(buffer.getvalue())

def batch_compress_images(input_dir, output_dir, max_size_mb, max_width=None, max_height=None):
    """
    批量压缩图片
    :param input_dir: 输入目录
    :param output_dir: 输出目录
    :param max_size_mb: 最大大小(MB)
    :param max_width: 最大宽度，可选
    :param max_height: 最大高度，可选
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    max_resolution = None
    if max_width or max_height:
        max_resolution = (max_width or float('inf'), max_height or float('inf'))
    
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                print(f"正在处理: {filename}")
                compress_image(input_path, output_path, max_size_mb, max_resolution=max_resolution)
                original_size = os.path.getsize(input_path) / (1024 * 1024)
                compressed_size = os.path.getsize(output_path) / (1024 * 1024)
                print(f"完成: {filename} (原始大小: {original_size:.2f}MB -> 压缩后: {compressed_size:.2f}MB)")
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("用法: python compress_images.py <输入目录> <最大大小(MB)> [最大宽度] [最大高度]")
        print("示例: python compress_images.py ./photos 2 1920 1080")
        return
    
    input_dir = sys.argv[1]
    try:
        max_size_mb = float(sys.argv[2])
    except ValueError:
        print("错误: 最大大小必须是数字")
        return
    
    max_width = None
    max_height = None
    
    if len(sys.argv) > 3:
        try:
            max_width = int(sys.argv[3])
        except ValueError:
            print("警告: 最大宽度不是有效整数，将忽略")
    
    if len(sys.argv) > 4:
        try:
            max_height = int(sys.argv[4])
        except ValueError:
            print("警告: 最大高度不是有效整数，将忽略")
    
    output_dir = os.path.join(input_dir, "compressed")
    batch_compress_images(input_dir, output_dir, max_size_mb, max_width, max_height)

if __name__ == "__main__":
    main()