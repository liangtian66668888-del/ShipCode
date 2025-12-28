#场景一的对比实验两个可视化代码

#场景一高频突发事件奖励函数对比图
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import json

# 替换为你的.json文件路径
# file_path1 = 'F:/TaskAllocation-main/models/RBF_5_DEDRS/modified_total_return_attn.json'
file_path2 = 'F:/TaskAllocation-main/models/RBF_2_DEDRS/total_return_attn.json'
file_path3 = 'F:/TaskAllocation-main/models/RBF_2_ppo/total_return_attn.json'
file_path4 = 'F:/TaskAllocation-main/models/RBF_2_a2c/total_return_attn.json'

# 加载.json文件
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# data1 = load_json_file(file_path1)
data2 = load_json_file(file_path2)
data3 = load_json_file(file_path3)
data4 = load_json_file(file_path4)

# 确保数据是列表或数组格式
# data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)


# 创建横坐标
# x1 = np.arange(len(data1))
x2 = np.arange(len(data2))
x3 = np.arange(len(data3))
x4 = np.arange(len(data4))

# 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'

# 创建图形
plt.figure(figsize=(12, 10))

# 绘制第一个文件的原始数据和平滑后的数据
# plt.plot(x1, smoothed_data1, label='DEDRS', color='#0072BD', linewidth=3.0)

# 绘制第二个文件的原始数据和平滑后的数据
plt.plot(x2, smoothed_data2, label='RDSE', color='#7E2F8E', linewidth=3.0)

# 绘制第三个文件的原始数据和平滑后的数据
plt.plot(x3, smoothed_data3, label='PPO', color='#A2142F', linewidth=3.0)

# 绘制第四个文件的原始数据和平滑后的数据
plt.plot(x4, smoothed_data4, label='A2C', color='#D95319', linewidth=3.0)

# 添加标题和标签，使用较大字体
# plt.title('Data Visualization with Smoothing and Shaded Bounds', fontsize=16)
plt.xlabel('episode', fontsize=46)
plt.ylabel('returns', fontsize=46)

# 添加图例，设置位置和字体大小
plt.legend(fontsize=46,  frameon=False)

# 设置刻度标签的字体大小和加粗
plt.xticks(fontsize=46)  # 设置 x 轴刻度标签的字体大小和加粗
plt.yticks(fontsize=46)  # 设置 y 轴刻度标签的字体大小和加粗

# 设置 y 轴从 0 开始
plt.ylim(bottom=0)

# 调整布局，避免标签被遮挡
plt.tight_layout()

# 显示网格线，提高可读性
plt.grid(True, linestyle='--', alpha=0.5)

# 保存图片为SVG矢量图格式
plt.savefig('场景一高频突发事件奖励对比实验图.svg', format='svg')

# 显示图形
plt.show()



#场景一低频突发事件奖励函数对比图
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import json

# 替换为你的.json文件路径
# file_path1 = 'F:/TaskAllocation-main/models/RBF_5_DEDRS/modified_total_return_attn.json'
file_path2 = 'F:/TaskAllocation-main/models/RBF_5_DEDRS/modified_total_return_attn.json'
file_path3 = 'F:/TaskAllocation-main/models/RBF_5_ppo/total_return_attn.json'
file_path4 = 'F:/TaskAllocation-main/models/RBF_5_a2c/total_return_attn.json'

# 加载.json文件
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# data1 = load_json_file(file_path1)
data2 = load_json_file(file_path2)
data3 = load_json_file(file_path3)
data4 = load_json_file(file_path4)

# 确保数据是列表或数组格式
# data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)


# 创建横坐标
# x1 = np.arange(len(data1))
x2 = np.arange(len(data2))
x3 = np.arange(len(data3))
x4 = np.arange(len(data4))

# 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'

# 创建图形
plt.figure(figsize=(12, 10))

# 绘制第一个文件的原始数据和平滑后的数据
# plt.plot(x1, smoothed_data1, label='DEDRS', color='#0072BD', linewidth=3.0)

# 绘制第二个文件的原始数据和平滑后的数据
plt.plot(x2, smoothed_data2, label='RDSE', color='#7E2F8E', linewidth=3.0)

# 绘制第三个文件的原始数据和平滑后的数据
plt.plot(x3, smoothed_data3, label='PPO', color='#A2142F', linewidth=3.0)

# 绘制第四个文件的原始数据和平滑后的数据
plt.plot(x4, smoothed_data4, label='A2C', color='#D95319', linewidth=3.0)

# 添加标题和标签，使用较大字体
# plt.title('Data Visualization with Smoothing and Shaded Bounds', fontsize=16)
plt.xlabel('episode', fontsize=46)
plt.ylabel('returns', fontsize=46)

# 添加图例，设置位置和字体大小
plt.legend(fontsize=46,  frameon=False)

# 设置刻度标签的字体大小和加粗
plt.xticks(fontsize=46)  # 设置 x 轴刻度标签的字体大小和加粗
plt.yticks(fontsize=46)  # 设置 y 轴刻度标签的字体大小和加粗

# 设置 y 轴从 0 开始
plt.ylim(bottom=0)

# 调整布局，避免标签被遮挡
plt.tight_layout()

# 显示网格线，提高可读性
plt.grid(True, linestyle='--', alpha=0.5)

# 保存图片为SVG矢量图格式
plt.savefig('场景一低频突发事件奖励对比实验图.svg', format='svg')

# 显示图形
plt.show()