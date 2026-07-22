# Hello World Collection & Graphics Generator

一个包含多种编程语言 "Hello, World!" 示例的集合项目，同时提供图形生成功能，适合编程初学者快速上手或作为参考模板。

## 📁 项目结构

```
.
├── hello.c          # C 语言 Hello World 示例
├── hello.cpp        # C++ Hello World 示例
├── hello.go         # Go 语言 Hello World 示例
├── Hello.java       # Java Hello World 示例
├── hello.py         # Python Hello World 示例
├── hello.js         # JavaScript Hello World 示例
├── sine_wave.py     # Python 正弦波 SVG 生成器
├── sine_wave.svg    # 生成的正弦波图像
├── cylinder.svg     # SVG 圆柱体图形
└── README.md        # 项目说明文档
```

## 🚀 快速开始

### C 语言
```bash
gcc hello.c -o hello
./hello
```

### C++
```bash
g++ hello.cpp -o hello
./hello
```

### Go
```bash
go run hello.go
```

### Java
```bash
javac Hello.java
java Hello
```

### Python Hello World
```bash
python hello.py
```

### JavaScript
```bash
node hello.js
```

## 🎨 图形生成

### 正弦波 SVG 图像
使用 Python 生成正弦波的 SVG 图像：

```bash
# 安装依赖
pip install svgwrite

# 运行生成器
python sine_wave.py
```

生成的 `sine_wave.svg` 文件将包含一个蓝色的正弦波曲线，带有坐标轴和标签。

### 圆柱体 SVG 图像
项目已包含一个使用纯 SVG 代码绘制的圆柱体图形 `cylinder.svg`，可以直接在浏览器中打开查看。

## 💡 输出示例
所有 Hello World 程序运行后都将输出：
```
Hello, World!
```

## 📝 说明
- Hello World 示例：每个文件都是独立的可运行示例，代码遵循各语言的最佳实践和简洁风格
- 图形生成：提供 Python 脚本生成正弦波 SVG，以及纯 SVG 代码绘制的圆柱体
- 适合作为学习新语言的第一个程序参考或 SVG 图形绘制的入门示例

## 🤝 贡献
欢迎提交 Issue 或 Pull Request 来添加更多语言示例、图形生成器或改进现有代码！

## 📄 许可证
本项目采用 MIT 许可证 - 详见 LICENSE 文件（如有）
