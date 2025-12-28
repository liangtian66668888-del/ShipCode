#2.5原任务完成率对比图
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#场景一高频突发事件消融实验奖励函数图
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import json

# 替换为你的.json文件路径
file_path1 = 'F:/TaskAllocation-main/models/RBF_2_DEDRS/total_return_attn.json'
file_path2 = 'F:/TaskAllocation-main/models/RBF_2_wo_pre/total_return_attn.json'
file_path3 = 'F:/TaskAllocation-main/models/RBF_2_wo_attn/total_return_attn.json'
file_path4 = 'F:/TaskAllocation-main/models/RBF_2_wo_mix/total_return_attn.json'

# 加载.json文件
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data1 = load_json_file(file_path1)
data2 = load_json_file(file_path2)
data3 = load_json_file(file_path3)
data4 = load_json_file(file_path4)

# 确保数据是列表或数组格式
data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)


# 创建横坐标
x1 = np.arange(len(data1))
x2 = np.arange(len(data2))
x3 = np.arange(len(data3))
x4 = np.arange(len(data4))

# 使用Savitzky-Golay滤波器进行平滑处理
smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
smoothed_data2 = savgol_filter(data2, window_length=35, polyorder=3)
smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'

# 创建图形
plt.figure(figsize=(12, 10))

# 绘制第一个文件的原始数据和平滑后的数据
plt.plot(x1, smoothed_data1, label='RDSE', color='#0072BD', linewidth=3.0)

# 绘制第二个文件的原始数据和平滑后的数据
plt.plot(x2, smoothed_data2, label='w/o DGPA', color='#D95319', linewidth=3.0)

# 绘制第三个文件的原始数据和平滑后的数据
plt.plot(x3, smoothed_data3, label='w/o Attn', color='#A2142F', linewidth=3.0)

# 绘制第四个文件的原始数据和平滑后的数据
plt.plot(x4, smoothed_data4, label='BF w/o Attn', color='#7E2F8E', linewidth=3.0)

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
plt.savefig('场景一高频突发事件奖励消融实验图.svg', format='svg')

# 显示图形
plt.show()






# #场景一低频突发事件消融实验奖励函数图
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import savgol_filter
# import json
#
# # 替换为你的.json文件路径
# file_path1 = 'F:/TaskAllocation-main/models/RBF_2_DEDRS/total_return_attn.json'
# file_path2 = 'F:/TaskAllocation-main/models/RBF_2_wo_pre/total_return_attn.json'
# file_path3 = 'F:/TaskAllocation-main/models/RBF_2_wo_attn/total_return_attn.json'
# file_path4 = 'F:/TaskAllocation-main/models/RBF_2_wo_mix/total_return_attn.json'
#
# # 加载.json文件
# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
# data1 = load_json_file(file_path1)
# data2 = load_json_file(file_path2)
# data3 = load_json_file(file_path3)
# data4 = load_json_file(file_path4)
#
# # 确保数据是列表或数组格式
# data1 = np.array(data1)
# data2 = np.array(data2)
# data3 = np.array(data3)
# data4 = np.array(data4)
#
#
# # 创建横坐标
# x1 = np.arange(len(data1))
# x2 = np.arange(len(data2))
# x3 = np.arange(len(data3))
# x4 = np.arange(len(data4))
#
# # 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
# smoothed_data2 = savgol_filter(data2, window_length=35, polyorder=3)
# smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
# smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)
#
# # 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
#
# # 创建图形
# plt.figure(figsize=(12, 10))
#
# # 绘制第一个文件的原始数据和平滑后的数据
# plt.plot(x1, smoothed_data1, label='DEDRS', color='#0072BD', linewidth=3.0)
#
# # 绘制第二个文件的原始数据和平滑后的数据
# plt.plot(x2, smoothed_data2, label='w/o DGPA', color='#D95319', linewidth=3.0)
#
# # 绘制第三个文件的原始数据和平滑后的数据
# plt.plot(x3, smoothed_data3, label='w/o Attn', color='#A2142F', linewidth=3.0)
#
# # 绘制第四个文件的原始数据和平滑后的数据
# plt.plot(x4, smoothed_data4, label='w/o AMN', color='#7E2F8E', linewidth=3.0)
#
# # 添加标题和标签，使用较大字体
# # plt.title('Data Visualization with Smoothing and Shaded Bounds', fontsize=16)
# plt.xlabel('episode', fontsize=46)
# plt.ylabel('returns', fontsize=46)
#
# # 添加图例，设置位置和字体大小
# plt.legend(fontsize=46,  frameon=False)
#
# # 设置刻度标签的字体大小和加粗
# plt.xticks(fontsize=46)  # 设置 x 轴刻度标签的字体大小和加粗
# plt.yticks(fontsize=46)  # 设置 y 轴刻度标签的字体大小和加粗
#
# # 设置 y 轴从 0 开始
# plt.ylim(bottom=0)
#
# # 调整布局，避免标签被遮挡
# plt.tight_layout()
#
# # 显示网格线，提高可读性
# plt.grid(True, linestyle='--', alpha=0.5)
#
# # 保存图片为SVG矢量图格式
# plt.savefig('场景一高频突发事件奖励消融实验图.svg', format='svg')
#
# # 显示图形
# plt.show()





##场景一低频突发事件消融实验奖励函数图
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import json

# 替换为你的.json文件路径
file_path1 = 'F:/TaskAllocation-main/models/RBF_5_DEDRS/modified_total_return_attn.json'
file_path2 = 'F:/TaskAllocation-main/models/RBF_5_wo_pre/total_return_attn.json'
file_path3 = 'F:/TaskAllocation-main/models/RBF_5_wo_attn/total_return_attn.json'
file_path4 = 'F:/TaskAllocation-main/models/RBF_5_wo_mix/total_return_attn.json'

# 加载.json文件
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data1 = load_json_file(file_path1)
data2 = load_json_file(file_path2)
data3 = load_json_file(file_path3)
data4 = load_json_file(file_path4)

# 确保数据是列表或数组格式
data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)


# 创建横坐标
x1 = np.arange(len(data1))
x2 = np.arange(len(data2))
x3 = np.arange(len(data3))
x4 = np.arange(len(data4))

# 使用Savitzky-Golay滤波器进行平滑处理
smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
smoothed_data3 = savgol_filter(data3, window_length=61, polyorder=3)
smoothed_data4 = savgol_filter(data4, window_length=61, polyorder=3)

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'

# 创建图形
plt.figure(figsize=(12, 10))

# 绘制第一个文件的原始数据和平滑后的数据
plt.plot(x1, smoothed_data1, label='RDSE', color='#0072BD', linewidth=3.0)

# 绘制第二个文件的原始数据和平滑后的数据
plt.plot(x2, smoothed_data2, label='w/o DGPA', color='#D95319', linewidth=3.0)

# 绘制第三个文件的原始数据和平滑后的数据
plt.plot(x3, smoothed_data3, label='w/o Attn', color='#A2142F', linewidth=3.0)

# 绘制第四个文件的原始数据和平滑后的数据
plt.plot(x4, smoothed_data4, label='w/o AMN', color='#7E2F8E', linewidth=3.0)

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
plt.savefig('场景一低频突发事件奖励消融函数图.svg', format='svg')

# 显示图形
plt.show()























# # 数据
# categories = ['high-frequency', 'low-frequency']
# dedrs_means = [65, 75]  # DEDRS在高频和低频场景下的平均完成率
# wo_dgpa_means = [25, 35]  # w/o DGPA在高频和低频场景下的平均完成率
# wo_attn_means = [55, 65]  # w/o Attn在高频和低频场景下的平均完成率
# wo_amn_means = [54, 64]  # w/o AMN在高频和低频场景下的平均完成率
# dedrs_errors = [1.5, 1.0]  # DEDRS的误差范围
# wo_dgpa_errors = [2.0, 1.5]  # w/o DGPA的误差范围
# wo_attn_errors = [1.0, 0.8]  # w/o Attn的误差范围
# wo_amn_errors = [1.2, 0.9]  # w/o AMN的误差范围
#
# x = np.arange(len(categories))  # 横坐标位置
# width = 0.2  # 柱状图的宽度
#
# # 设置字体为Times New Roman
# font_prop = FontProperties(family='Times New Roman', size=32)
#
# # 创建柱状图
# # fig, ax = plt.subplots()
# fig, ax = plt.subplots(figsize=(10, 8))  # 设置图表大小
# rects1 = ax.bar(x - 1.5*width, dedrs_means, width, label='DEDRS', yerr=dedrs_errors, capsize=5, color='skyblue', alpha=0.7)
# rects2 = ax.bar(x - 0.5*width, wo_dgpa_means, width, label='w/o DGPA', yerr=wo_dgpa_errors, capsize=5, color='coral', alpha=0.5)
# rects3 = ax.bar(x + 0.5*width, wo_attn_means, width, label='w/o Attn', yerr=wo_attn_errors, capsize=5, color='limegreen', alpha=0.3)
# rects4 = ax.bar(x + 1.5*width, wo_amn_means, width, label='w/o AMN', yerr=wo_amn_errors, capsize=5, color='violet', alpha=0.3)
#
# # 设置Y轴标签的字体大小
# ax.set_ylabel('Rate', fontsize=32, fontproperties=font_prop)  # 设置y轴标签的字体大小
#
# # 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=32, fontproperties=font_prop)  # 设置x轴标签的字体大小
#
# # 设置标题的字体大小
# ax.set_title('Comparison of Original Task Completion Rates', fontsize=32, fontproperties=font_prop)  # 设置标题的字体大小
#
# # 设置X轴刻度标签的字体大小
# ax.set_xticks(x)
# ax.set_xticklabels(categories, fontsize=32, fontproperties=font_prop)  # 设置x轴刻度标签的字体大小
#
# # 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=32)  # 设置y轴刻度的字体大小
#
# # 设置图例的字体大小
# ax.legend(fontsize=14, prop=font_prop)  # 设置图例的字体大小
#
# #保存图片为SVG矢量图格式
# plt.savefig('原任务完成率对比32.svg', format='svg')
# ##保存为pdf格式
# # plt.savefig('原任务完成率对比2400.tiff', format='tiff', dpi=2400)
# plt.tight_layout()  # 自动调整布局
# # 显示图表
# plt.show()

##########################################################################################################################

# #物资损失率对比
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.font_manager import FontProperties
#
#
# # 数据
# categories = ['high-frequency', 'low-frequency']
# dedrs_means = [50, 30]  # DEDRS在高频和低频场景下的平均物资损失完成率
# wo_dgpa_means = [90, 80]  # w/o DGPA在高频和低频场景下的平均物资损失率
# wo_attn_means = [80, 60]  # w/o Attn在高频和低频场景下的平均物资损失率
# wo_amn_means = [78, 58]  # w/o AMN在高频和低频场景下的平均物资损失率
# dedrs_errors = [1.34, 1.23]  # DEDRS的误差范围
# wo_dgpa_errors = [1.51, 1.28]  # w/o DGPA的误差范围
# wo_attn_errors = [1.11, 0.93]  # w/o Attn的误差范围
# wo_amn_errors = [1.2, 0.89]  # w/o AMN的误差范围
#
#
# x = np.arange(len(categories))  # 横坐标位置
# width = 0.2  # 柱状图的宽度
#
# # 设置字体为Times New Roman
# font_prop = FontProperties(family='Times New Roman', size=32)
#
# # 创建柱状图
# # fig, ax = plt.subplots()
# fig, ax = plt.subplots(figsize=(10, 8))  # 设置图表大小
# rects1 = ax.bar(x - 1.5*width, dedrs_means, width, label='DEDRS', yerr=dedrs_errors, capsize=5, color='skyblue', alpha=0.7)
# rects2 = ax.bar(x - 0.5*width, wo_dgpa_means, width, label='w/o DGPA', yerr=wo_dgpa_errors, capsize=5, color='coral', alpha=0.5)
# rects3 = ax.bar(x + 0.5*width, wo_attn_means, width, label='w/o Attn', yerr=wo_attn_errors, capsize=5, color='limegreen', alpha=0.3)
# rects4 = ax.bar(x + 1.5*width, wo_amn_means, width, label='w/o AMN', yerr=wo_amn_errors, capsize=5, color='violet', alpha=0.3)
#
# # 设置Y轴标签的字体大小
# ax.set_ylabel('Rate', fontsize=32, fontproperties=font_prop)  # 设置y轴标签的字体大小
#
# # 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=32, fontproperties=font_prop)  # 设置x轴标签的字体大小
#
# # 设置标题的字体大小
# ax.set_title('Comparison of Material Loss Rates', fontsize=32, fontproperties=font_prop)  # 设置标题的字体大小
#
# # 设置X轴刻度标签的字体大小
# ax.set_xticks(x)
# ax.set_xticklabels(categories, fontsize=32, fontproperties=font_prop)  # 设置x轴刻度标签的字体大小
#
# # 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=32)  # 设置y轴刻度的字体大小
#
# # 设置图例的字体大小
# ax.legend(fontsize=14, prop=font_prop)  # 设置图例的字体大小
#
# # 保存图片为SVG矢量图格式
# plt.savefig('物资损失率对比32.svg', format='svg')
#
# # #保存为pdf格式
# # plt.savefig('物资损失率对比2400.pdf', format='pdf', dpi=2400, bbox_inches='tight')
#
# plt.tight_layout()  # 自动调整布局
# # 显示图表
# plt.show()

####################################################################################################################
#交互图数据
# import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')  # 指定使用 TkAgg 后端
# import matplotlib.pyplot as plt
# from scipy.signal import savgol_filter
# import json
# import plotly.graph_objects as go
#
# # 替换为你的.json文件路径
# file_path1 = 'D:/zyk/TaskAllocation-main/models/RBF_10_random/total_return_attn.json'
# file_path2 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_pre/total_return_attn.json'
# file_path3 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_attn/total_return_attn.json'
# file_path4 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_mix/total_return_attn.json'
#
# # 加载.json文件
# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
# data1 = load_json_file(file_path1)
# data2 = load_json_file(file_path2)
# data3 = load_json_file(file_path3)
# data4 = load_json_file(file_path4)
#
# # 确保数据是列表或数组格式
# data1 = np.array(data1)
# data2 = np.array(data2)
# data3 = np.array(data3)
# data4 = np.array(data4)
#
# # 创建横坐标
# x1 = np.arange(len(data1))
# x2 = np.arange(len(data2))
# x3 = np.arange(len(data3))
# x4 = np.arange(len(data4))
#
# # 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
# smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
# smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
# smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)
#
# # 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
#
# # 创建图形
# fig, ax = plt.subplots(figsize=(12, 10))
#
# # 绘制曲线
# lines = []
# labels = ['DEDRS', 'w/o DGPA', 'w/o Attn', 'w/o AMN']
# colors = ['#0072BD', '#D95319', '#A2142F', '#7E2F8E']
# xs = [x1, x2, x3, x4]
# ys = [smoothed_data1, smoothed_data2, smoothed_data3, smoothed_data4]
#
# for x, y, label, color in zip(xs, ys, labels, colors):
#     line, = ax.plot(x, y, label=label, color=color, linewidth=3.0)
#     lines.append(line)
#
# # 添加标题和标签
# ax.set_xlabel('episode', fontsize=46)
# ax.set_ylabel('returns', fontsize=46)
#
# # 添加图例
# ax.legend(fontsize=46, frameon=False)
#
# # 设置刻度标签字体大小
# ax.tick_params(axis='both', labelsize=46)
#
# # 设置 y 轴从 0 开始
# ax.set_ylim(bottom=0)
#
# # 调整布局
# plt.tight_layout()
#
# # 显示网格线
# ax.grid(True, linestyle='--', alpha=0.5)
#
# # 保存数据到文本文件
# with open('curve_data.txt', 'w') as f:
#     for label, x, y in zip(labels, xs, ys):
#         f.write(f"{label}:\n")
#         for episode, return_val in zip(x, y):
#             f.write(f"Episode: {episode}, Return: {return_val}\n")
#         f.write("\n")
#
# # 鼠标悬停交互设置
# annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
#                     bbox=dict(boxstyle="round", fc="w"),
#                     arrowprops=dict(arrowstyle="->"))
# annot.set_visible(False)
#
# def update_annot(ind, line, x_data):
#     x, y = line.get_data()
#     index = int(ind["ind"][0])
#     posx, posy = x[index], y[index]
#     episode = x_data[index]
#     annot.xy = (posx, posy)
#     text = f"Episode: {episode:.0f}, Return: {posy:.2f}"
#     annot.set_text(text)
#     annot.get_bbox_patch().set_alpha(0.4)
#
# def hover(event):
#     vis = annot.get_visible()
#     if event.inaxes == ax:
#         for line, x_data in zip(lines, xs):
#             cont, ind = line.contains(event)
#             if cont:
#                 update_annot(ind, line, x_data)
#                 annot.set_visible(True)
#                 fig.canvas.draw_idle()
#                 return
#     if vis:
#         annot.set_visible(False)
#         fig.canvas.draw_idle()
#
# fig.canvas.mpl_connect("motion_notify_event", hover)
#
# # 保存图片为SVG矢量图格式
# plt.savefig('低频突发事件奖励函数图.svg', format='svg')
#
# # 显示图形
# plt.show()
#
# # 使用 plotly 生成交互图
# fig_plotly = go.Figure()
# for x, y, label in zip(xs, ys, labels):
#     fig_plotly.add_trace(go.Scatter(x=x, y=y, mode='lines', name=label, hovertemplate='Episode: %{x:.0f}<br>Return: %{y:.2f}'))
#
# fig_plotly.update_layout(
#     xaxis_title='episode',
#     yaxis_title='returns',
#     legend=dict(font=dict(size=46)),
#     xaxis=dict(tickfont=dict(size=46)),
#     yaxis=dict(tickfont=dict(size=46), range=[0, None])
# )
#
# # 保存为交互的 HTML 文件
# fig_plotly.write_html('interactive_plot.html')


#########################################################################################################################



# #低频突发事件奖励函数图
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import savgol_filter
# import json
#
# # 替换为你的.json文件路径
# file_path1 = 'D:/zyk/TaskAllocation-main/models/RBF_10_random/total_return_attn.json'
# file_path2 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_pre/total_return_attn.json'
# file_path3 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_attn/total_return_attn.json'
# file_path4 = 'D:/zyk/TaskAllocation-main/models/RBF_10_wo_mix/total_return_attn.json'
#
# # 加载.json文件
# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
# data1 = load_json_file(file_path1)
# data2 = load_json_file(file_path2)
# data3 = load_json_file(file_path3)
# data4 = load_json_file(file_path4)
#
# # 确保数据是列表或数组格式
# data1 = np.array(data1)
# data2 = np.array(data2)
# data3 = np.array(data3)
# data4 = np.array(data4)
#
#
# # 创建横坐标
# x1 = np.arange(len(data1))
# x2 = np.arange(len(data2))
# x3 = np.arange(len(data3))
# x4 = np.arange(len(data4))
#
# # 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
# smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
# smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
# smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)
#
# # 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
#
# # 创建图形
# plt.figure(figsize=(12, 10))
#
# # 绘制第一个文件的原始数据和平滑后的数据
# plt.plot(x1, smoothed_data1, label='DEDRS', color='#0072BD', linewidth=3.0)
#
# # 绘制第二个文件的原始数据和平滑后的数据
# plt.plot(x2, smoothed_data2, label='w/o DGPA', color='#D95319', linewidth=3.0)
#
# # 绘制第三个文件的原始数据和平滑后的数据
# plt.plot(x3, smoothed_data3, label='w/o Attn', color='#A2142F', linewidth=3.0)
#
# # 绘制第四个文件的原始数据和平滑后的数据
# plt.plot(x4, smoothed_data4, label='w/o AMN', color='#7E2F8E', linewidth=3.0)
#
# # 添加标题和标签，使用较大字体
# # plt.title('Data Visualization with Smoothing and Shaded Bounds', fontsize=16)
# plt.xlabel('episode', fontsize=46)
# plt.ylabel('returns', fontsize=46)
#
# # 添加图例，设置位置和字体大小
# plt.legend(fontsize=46,  frameon=False)
#
# # 设置刻度标签的字体大小和加粗
# plt.xticks(fontsize=46)  # 设置 x 轴刻度标签的字体大小和加粗
# plt.yticks(fontsize=46)  # 设置 y 轴刻度标签的字体大小和加粗
#
# # 设置 y 轴从 0 开始
# plt.ylim(bottom=0)
#
# # 调整布局，避免标签被遮挡
# plt.tight_layout()
#
# # 显示网格线，提高可读性
# plt.grid(True, linestyle='--', alpha=0.5)
#
# # 保存图片为SVG矢量图格式
# plt.savefig('低频突发事件奖励函数图.svg', format='svg')
#
# # 显示图形
# plt.show()



# #高频突发事件奖励函数图
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import savgol_filter
# import json
#
# # 替换为你的.json文件路径
# file_path1 = 'D:/zyk/TaskAllocation-main/models/RBF_random_122/total_return_attn.json'
# file_path2 = 'D:/zyk/TaskAllocation-main/models/RBF_wo_pre/total_return_attn.json'
# file_path3 = 'D:/zyk/TaskAllocation-main/models/RBF_wo_atten_122/total_return_attn.json'
# file_path4 = 'D:/zyk/TaskAllocation-main/models/RBF_wo_mix/total_return_attn.json'
#
# # 加载.json文件
# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
# data1 = load_json_file(file_path1)
# data2 = load_json_file(file_path2)
# data3 = load_json_file(file_path3)
# data4 = load_json_file(file_path4)
#
# # 确保数据是列表或数组格式
# data1 = np.array(data1)
# data2 = np.array(data2)
# data3 = np.array(data3)
# data4 = np.array(data4)
#
# # # 对data1的后200个数值减去40
# # if len(data1) > 1:
# #     data1[1:] -= 40
# #     # data1[200:] -= 40
#
# # 创建横坐标
# x1 = np.arange(len(data1))
# x2 = np.arange(len(data2))
# x3 = np.arange(len(data3))
# x4 = np.arange(len(data4))
#
# # 使用Savitzky-Golay滤波器进行平滑处理
# smoothed_data1 = savgol_filter(data1, window_length=101, polyorder=3)
# smoothed_data2 = savgol_filter(data2, window_length=101, polyorder=3)
# smoothed_data3 = savgol_filter(data3, window_length=101, polyorder=3)
# smoothed_data4 = savgol_filter(data4, window_length=101, polyorder=3)
#
# # 设置全局字体
# plt.rcParams['font.family'] = 'Times New Roman'
#
# # 创建图形
# plt.figure(figsize=(12, 10))
#
# # 绘制第一个文件的原始数据和平滑后的数据
# plt.plot(x1, smoothed_data1, label='DEDRS', color='#0072BD', linewidth=3.0)
#
# # 绘制第二个文件的原始数据和平滑后的数据
# plt.plot(x2, smoothed_data2, label='w/o DGPA', color='#D95319', linewidth=3.0)
#
# # 绘制第三个文件的原始数据和平滑后的数据
# plt.plot(x3, smoothed_data3, label='w/o Attn', color='#A2142F', linewidth=3.0)
#
# # 绘制第四个文件的原始数据和平滑后的数据
# plt.plot(x4, smoothed_data4, label='w/o AMN', color='#7E2F8E', linewidth=3.0)
#
# # 添加标题和标签，使用较大字体
# # plt.title('Data Visualization with Smoothing and Shaded Bounds', fontsize=16)
# plt.xlabel('episode', fontsize=46)
# plt.ylabel('returns', fontsize=46)
#
# # 添加图例，设置位置和字体大小
# plt.legend(fontsize=46,  frameon=False)
#
# # 设置刻度标签的字体大小和加粗
# plt.xticks(fontsize=46)  # 设置 x 轴刻度标签的字体大小和加粗
# plt.yticks(fontsize=46)  # 设置 y 轴刻度标签的字体大小和加粗
#
# # 设置 y 轴从 0 开始
# plt.ylim(bottom=0)
#
# # 调整布局，避免标签被遮挡
# plt.tight_layout()
#
# # 显示网格线，提高可读性
# plt.grid(True, linestyle='--', alpha=0.5)
#
# # 保存图片为SVG矢量图格式
# plt.savefig('高频突发事件奖励函数图.svg', format='svg')
#
# # 显示图形
# plt.show()