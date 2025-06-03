# 批量图片压缩工具

一个基于Python的批量图片压缩工具，可指定目标文件大小和分辨率限制。

## 功能特性

- ✅ 批量压缩指定目录下的所有图片  
- ✅ 支持多种图片格式（JPG/JPEG/PNG/BMP/TIFF/WEBP）  
- ✅ 可设置最大文件大小（MB为单位）  
- ✅ 可选设置最大宽度/高度限制  
- ✅ 智能质量调整算法保持最佳视觉效果  
- ✅ 非破坏性压缩（原始文件保持不变）  

## 安装指南

### 前置要求

- Python 3.6或更高版本  
- pip包管理工具  

### 安装步骤

1. 克隆或下载本项目代码  
2. 安装依赖项：  

```bash
pip install -r requirements.txt
```

## 使用说明

### 基本用法

```bash
python compress_images.py <输入目录> <最大大小(MB)>
```

示例：压缩`photos`目录下所有图片到2MB以下  

```bash
python compress_images.py ./photos 2
```

### 高级用法

```bash
python compress_images.py <输入目录> <最大大小(MB)> [最大宽度] [最大高度]
```

示例1：压缩图片到1MB以下，并限制最大宽度为1920像素  

```bash
python compress_images.py ./photos 1 1920
```

示例2：压缩图片到0.5MB以下，并限制最大分辨率为1920x1080  

```bash
python compress_images.py ./photos 0.5 1920 1080
```

## 编译为可执行程序

### 方法一：使用PyInstaller（推荐）

1. 安装编译工具：
```bash
pip install pyinstaller
```

2. 执行编译（生成单个exe文件）：
```bash
pyinstaller --onefile --icon=app.ico compress_images.py
```
*注：`app.ico`为可选的应用图标文件*

3. 编译完成后：
   - Windows系统：在`dist/`目录生成`compress_images.exe`
   - Linux系统：在`dist/`目录生成可执行文件

### 方法二：使用auto-py-to-exe（图形界面）

1. 安装工具：
```bash
pip install auto-py-to-exe
```

2. 启动图形界面：
```bash
auto-py-to-exe
```
在界面中选择：
- Python文件：`compress_images.py`
- 勾选"One File"模式
- 可添加ICO图标文件
- 点击"CONVERT .PY TO .EXE"

### 编译注意事项

1. **图标文件要求**：
   - 必须是`.ico`格式
   - 推荐包含16x16/32x32/48x48/256x256多尺寸
   - 可使用在线工具将PNG转换为ICO

2. **跨平台编译**：
   - Windows系统编译Windows版本
   - Linux系统编译Linux版本
   - Mac系统需使用`py2app`工具

## 输出说明

程序会在输入目录下创建`compressed`子目录，所有压缩后的图片将保存在此目录中。  

处理过程中会显示：  
- 当前正在处理的文件  
- 原始文件大小  
- 压缩后文件大小  

## 注意事项

1. 程序不会修改原始图片文件  
2. 对于已经小于目标大小的图片，程序会跳过压缩  
3. 建议对大尺寸图片同时设置分辨率限制以获得更好的压缩效果  
4. 压缩质量在85-10之间自动调整以符合大小限制  

## 常见问题

**Q: 程序支持哪些图片格式？**  
A: 支持JPG、JPEG、PNG、BMP、TIFF和WEBP格式  

**Q: 压缩后的图片会降低分辨率吗？**  
A: 只有在指定了最大宽度/高度参数时才会调整分辨率，否则仅调整压缩质量  

**Q: 为什么编译后的exe文件很大？**  
A: 这是PyInstaller打包Python解释器的正常现象，可用UPX压缩减小体积：
```bash
pyinstaller --onefile --upx-dir=path/to/upx compress_images.py
```

## 许可证

本项目使用MIT许可证  