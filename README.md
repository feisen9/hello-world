# 图形与可视化项目 (Graphics & Visualization Collection)

一个包含多种图形生成和可视化示例的集合项目，包括使用 Python 生成正弦波图像和使用 SVG 绘制 3D 圆柱体。

## 📁 项目结构

```
.
├── sine_wave.py       # Python 正弦波生成脚本
├── sine_wave.svg      # 生成的正弦波 SVG 图像
├── cylinder.svg       # SVG 绘制的 3D 圆柱体
├── hello.c            # C 语言示例
├── hello.cpp          # C++ 示例
├── hello.go           # Go 语言示例
├── Hello.java         # Java 示例
├── hello.py           # Python 示例
└── README.md          # 项目说明文档
```

## 🚀 快速开始

### 生成正弦波图像

**依赖安装：**
```bash
pip install matplotlib numpy
```

**运行脚本：**
```bash
python sine_wave.py
```

这将生成 `sine_wave.svg` 文件，包含一个漂亮的正弦波图像。

### 查看圆柱体 SVG

直接在任何现代浏览器中打开 `cylinder.svg` 文件即可查看 3D 圆柱体插图。

```bash
# Linux/Mac
open cylinder.svg        # Mac
xdg-open cylinder.svg    # Linux

# Windows
start cylinder.svg
```

## 📝 文件说明

### sine_wave.py
- 使用 Python 的 matplotlib 库绘制正弦波
- 输出格式：SVG（可缩放矢量图形）
- 特点：
  - 显示 0 到 4π 范围的正弦波
  - x 轴刻度以 π 的倍数标注
  - 包含网格线和图例
  - 支持保存为 SVG 和 PNG 格式

### cylinder.svg
- 纯 SVG 代码绘制的 3D 圆柱体
- 特点：
  - 使用渐变填充模拟光照效果
  - 包含高度和半径标注
  - 具有立体感的视觉效果
  - 可直接在浏览器中查看

## 💡 输出示例

### 正弦波图像特征
- 蓝色曲线表示 sin(x) 函数
- x 轴范围：0 到 4π
- y 轴范围：-1.5 到 1.5
- 包含水平参考线 y=0

### 圆柱体视觉特征
- 灰色渐变模拟金属质感
- 顶部椭圆表现透视效果
- 尺寸标注清晰展示几何参数

## 🛠️ 技术要求

- **Python 版本**: 3.6+
- **依赖库**: 
  - matplotlib >= 3.0
  - numpy >= 1.15
- **浏览器**: 任何支持 SVG 的现代浏览器

## 🤝 贡献

欢迎提交 Issue 或 Pull Request 来添加更多图形示例或改进现有代码！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件（如有）

Just for try.
Good morning.
