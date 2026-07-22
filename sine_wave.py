import math
import svgwrite

def create_sine_wave_svg(filename="sine_wave.svg", width=800, height=400):
    """生成正弦波的 SVG 图像"""
    
    dwg = svgwrite.Drawing(filename, profile='tiny', size=(f"{width}px", f"{height}px"))
    
    # 添加背景
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))
    
    # 坐标轴参数
    center_y = height / 2
    margin = 50
    axis_length = width - 2 * margin
    
    # 绘制 X 轴
    dwg.add(dwg.line(start=(margin, center_y), end=(width - margin, center_y), 
                     stroke='black', stroke_width=2))
    
    # 绘制 Y 轴
    dwg.add(dwg.line(start=(margin, center_y - 150), end=(margin, center_y + 150), 
                     stroke='black', stroke_width=2))
    
    # 生成正弦波路径
    amplitude = 100  # 振幅
    frequency = 2    # 频率（周期数）
    points = []
    
    for x in range(margin, width - margin + 1, 2):
        # 将 x 映射到 0 到 2π*frequency 范围
        t = (x - margin) / axis_length * 2 * math.pi * frequency
        y = center_y - amplitude * math.sin(t)
        points.append((x, y))
    
    # 创建路径字符串
    path_data = f"M {points[0][0]},{points[0][1]}"
    for x, y in points[1:]:
        path_data += f" L {x},{y}"
    
    # 添加正弦波路径
    dwg.add(dwg.path(d=path_data, stroke='blue', stroke_width=2, fill='none'))
    
    # 添加标签
    dwg.add(dwg.text("X", insert=(width - margin + 10, center_y + 20), 
                     font_size=16, fill='black'))
    dwg.add(dwg.text("Y", insert=(margin - 20, center_y - 150), 
                     font_size=16, fill='black'))
    dwg.add(dwg.text("Sine Wave: y = sin(x)", insert=(width/2 - 100, 30), 
                     font_size=18, fill='blue', font_weight='bold'))
    
    dwg.save()
    print(f"正弦波 SVG 已保存到 {filename}")

if __name__ == "__main__":
    create_sine_wave_svg()
