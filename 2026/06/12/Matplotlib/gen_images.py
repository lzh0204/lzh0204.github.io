import matplotlib.pyplot as plt
import numpy as np
import os

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

out = r'E:\MyBlog\blog\source\_posts\Matplotlib'
os.makedirs(out, exist_ok=True)

def ts(i):
    """生成唯一时间戳文件名"""
    base = 20260612120000000 + i * 1000
    return f'image-{base}.png'

idx = 0  # 递增索引，保证文件名唯一

# ====== 散点图 ======
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(10)
y = np.random.randn(10)
ax.scatter(x, y, color='red', marker='+')
ax.set_title('散点图示例')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'scatter -> {fname}')

# ====== 简单柱状图 ======
x = ['A', 'B', 'C', 'D']
y = [23, 45, 56, 78]
plt.bar(x, y, color='steelblue', width=0.6)
plt.title('简单柱状图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'simple bar -> {fname}')

# ====== 分组柱状图 ======
x = np.arange(3)
width = 0.3
men = [20, 35, 30]
women = [25, 32, 34]
plt.bar(x - width/2, men, width, label='男')
plt.bar(x + width/2, women, width, label='女')
plt.xticks(x, ['A组', 'B组', 'C组'])
plt.legend()
plt.title('分组柱状图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'grouped bar -> {fname}')

# ====== 堆叠柱状图 ======
plt.bar(x, men, label='男')
plt.bar(x, women, bottom=men, label='女')
plt.xticks(x, ['A组', 'B组', 'C组'])
plt.legend()
plt.title('堆叠柱状图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'stacked bar -> {fname}')

# ====== 水平柱状图 ======
x = ['A', 'B', 'C', 'D']
y = [23, 45, 56, 78]
plt.barh(x, y, color='coral')
plt.title('水平柱状图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'horizontal bar -> {fname}')

# ====== 直方图 ======
data = np.random.randn(1000)
plt.hist(data, bins=30, color='steelblue', edgecolor='white', alpha=0.7)
plt.title('直方图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'histogram -> {fname}')

# ====== 饼图 ======
labels = ['Python', 'Java', 'C++', 'JavaScript', '其他']
sizes = [35, 25, 20, 12, 8]
explode = (0.1, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')
plt.title('饼图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'pie -> {fname}')

# ====== 箱线图 ======
data = [np.random.randn(100) for _ in range(4)]
plt.boxplot(data, labels=['A组', 'B组', 'C组', 'D组'],
            patch_artist=True, showmeans=True, meanline=True)
plt.title('箱线图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'boxplot -> {fname}')

# ====== 标题与轴标签 ======
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('正弦函数', fontsize=14, fontweight='bold')
plt.xlabel('x 轴', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'title labels -> {fname}')

# ====== 图例 ======
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin')
plt.plot(x, np.cos(x), label='cos')
plt.legend(loc='upper right', fontsize=10, frameon=True, ncol=2)
plt.title('图例示例')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'legend -> {fname}')

# ====== 网格 ======
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.grid(True, linestyle='--', alpha=0.5, color='gray')
plt.title('网格示例')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'grid -> {fname}')

# ====== 坐标轴范围与刻度 ======
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x))
plt.xlim(0, 2*np.pi)
plt.ylim(-1.5, 1.5)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])
plt.title('自定义坐标轴')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'axis ticks -> {fname}')

# ====== 文字注释 ======
x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.plot(x, y)
plt.text(5, 0.5, '峰值区域', fontsize=12, color='red')
plt.annotate('局部最低点',
    xy=(3*np.pi/2, -1),
    xytext=(4, -0.5),
    arrowprops=dict(arrowstyle='->', color='blue'),
    fontsize=11)
plt.title('文字注释')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'annotation -> {fname}')

# ====== 线型颜色标记 ======
x = np.linspace(0, 10, 20)
plt.plot(x, x+0,  'r-o',  label='实线圆点')
plt.plot(x, x+5,  'g--s', label='虚线方块')
plt.plot(x, x+10, 'b:^',  label='点线上三角')
plt.plot(x, x+15, 'k-.',  label='点划线无标记')
plt.legend()
plt.title('线型/颜色/标记示例')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'line styles -> {fname}')

# ====== 面积图 ======
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.fill_between(x, y1, alpha=0.3, label='sin')
plt.fill_between(x, y2, alpha=0.3, label='cos')
plt.legend()
plt.title('面积图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'fill between -> {fname}')

# ====== 等高线图 ======
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)
plt.contour(X, Y, Z, levels=15, cmap='viridis')
plt.contourf(X, Y, Z, levels=15, cmap='viridis', alpha=0.7)
plt.colorbar(label='值')
plt.title('等高线图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'contour -> {fname}')

# ====== 热力图 ======
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('热力图')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'heatmap -> {fname}')

# ====== 面向对象多子图 ======
x = np.linspace(0, 10, 100)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('sin')
axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('cos')
axes[1, 0].bar(['A', 'B', 'C'], [3, 7, 5])
axes[1, 0].set_title('bar')
axes[1, 1].scatter(np.random.randn(20), np.random.randn(20))
axes[1, 1].set_title('scatter')
plt.tight_layout()
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'OOP subplots -> {fname}')

# ====== 双Y轴 ======
x = np.linspace(0, 10, 100)
fig, ax1 = plt.subplots()
ax1.plot(x, np.sin(x), 'b-', label='sin')
ax1.set_ylabel('sin', color='b')
ax2 = ax1.twinx()
ax2.plot(x, np.exp(x/3), 'r-', label='exp')
ax2.set_ylabel('exp(x/3)', color='r')
plt.title('双Y轴')
fname = ts(idx); idx += 1
plt.savefig(os.path.join(out, fname), dpi=150, bbox_inches='tight')
plt.close()
print(f'twin axis -> {fname}')

print('\n=== Done ===')
print(f'Generated {idx} images in {out}')
