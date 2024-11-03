import numpy as np
import plotly.graph_objects as go

# 创建数据
x_values = np.arange(-10, 11, 0.5)  # x 方向的离散值，从 -10 到 10，间隔为 0.5
y_values = np.arange(-10, 11, 0.5)  # y 方向的离散值，从 -10 到 10，间隔为 0.5
y = np.linspace(-10, 10, 100)       # y 的连续值范围
x = np.linspace(-10, 10, 100)       # x 的连续值范围

# 创建图形对象
fig = go.Figure()

# 绘制顶部曲线（沿 x 固定，y 变化）
for x_val in x_values:
    z = x_val**2 + y**2 + 100
    fig.add_trace(go.Scatter3d(x=[x_val] * len(y), y=y, z=z, mode='lines',
                               line=dict(color="#32CD32", width=1)))

# 绘制顶部曲线（沿 y 固定，x 变化）
for y_val in y_values:
    z = x**2 + y_val**2 + 100
    fig.add_trace(go.Scatter3d(x=x, y=[y_val] * len(x), z=z, mode='lines',
                               line=dict(color="#32CD32", width=1)))

# 在 x-y 平面上绘制圆形（半径逐渐递增）
radii = np.arange(1, 20, 0.5)
for r in radii:
    theta = np.linspace(0, 2 * np.pi, 100)  # 角度从 0 到 2π
    x_circle = r * np.cos(theta)  # 圆的 x 坐标
    y_circle = r * np.sin(theta)  # 圆的 y 坐标
    z_circle = np.full_like(x_circle, 0)  # 将 z 值固定在 0
    fig.add_trace(go.Scatter3d(x=x_circle, y=y_circle, z=z_circle, mode='lines',
                               line=dict(color="#32CD32", width=1)))  # 圆的颜色为绿色

# 添加 x=5 的平面
y_plane = np.linspace(-10, 10, 100)  # y 方向范围
z_plane = np.linspace(0, 300, 100)   # z 方向范围
y_plane, z_plane = np.meshgrid(y_plane, z_plane)
x_plane = np.full_like(y_plane, 5)   # 将 x 值固定在 5

fig.add_trace(go.Surface(
    x=x_plane, y=y_plane, z=z_plane,
    colorscale=[[0, 'white'], [1, 'white']],
    opacity=1,
    showscale=False
))

# 在 x=5 的平面上绘制横线（固定 z，沿 y 变化）
for z_val in np.linspace(0, 300, 10):
    fig.add_trace(go.Scatter3d(
        x=[5] * 100,  # 固定 x
        y=np.linspace(-10, 10, 100),
        z=[z_val] * 100,  # 固定 z
        mode='lines',
        line=dict(color='#32CD32', width=1)
    ))

# 在 x=5 的平面上绘制竖线（固定 y，沿 z 变化）
for y_val in np.linspace(-10, 10, 10):
    fig.add_trace(go.Scatter3d(
        x=[5] * 100,  # 固定 x
        y=[y_val] * 100,  # 固定 y
        z=np.linspace(0, 300, 100),
        mode='lines',
        line=dict(color='#32CD32', width=1)
    ))

# 在 x=5 时绘制顶部曲面的直线，颜色为红色
z_red = 5**2 + y**2 + 100  # 计算当 x=5 时的 z 值
fig.add_trace(go.Scatter3d(
    x=[5] * len(y),  # 固定 x
    y=y,  # 变化 y
    z=z_red,  # 对应的 z 值
    mode='lines',
    line=dict(color='red', width=2)  # 红色线
))

# 绘制两条新的红色直线
# 直线1: x=5, y=-5, z=x**2 + y**2 + 100
y_val1 = -5
z_val1 = 5**2 + y_val1**2 + 100
fig.add_trace(go.Scatter3d(
    x=[5] * 2,  # 固定 x
    y=[y_val1] * 2,  # 固定 y
    z=[0, z_val1],  # 从 z=0 到计算的 z 值
    mode='lines',
    line=dict(color='red', width=2)  # 红色线
))

# 直线2: x=5, y=0, z=x**2 + y**2 + 100
y_val2 = 0
z_val2 = 5**2 + y_val2**2 + 100
fig.add_trace(go.Scatter3d(
    x=[5] * 2,  # 固定 x
    y=[y_val2] * 2,  # 固定 y
    z=[0, z_val2],  # 从 z=0 到计算的 z 值
    mode='lines',
    line=dict(color='red', width=2)  # 红色线
))

# 设置布局和视角，将背景颜色设置为白色
fig.update_layout(
    title="Interactive 3D Model with x=5 Plane and Grid Lines",
    scene=dict(
        xaxis=dict(title="X", range=[-10, 10]),
        yaxis=dict(title="Y", range=[-10, 10]),
        zaxis=dict(title="Z", range=[-50, 300]),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),  # 初始视角
        bgcolor='rgb(255,255,255)'  # 设置背景为纯白色
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

# 保存图形为 HTML 文件
fig.write_html("interactive_3d_model_with_grid_lines.html")

# 显示图形（在浏览器中可以交互）
fig.show()