#场景一大论文物资受损率
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
categories = [ '低频','高频']
dedrs_means = [35.3, 47.9]  # DEDRS在高频和低频场景下的平均完成率
wo_dgpa_means = [56.5, 90.1]  # w/o DGPA在高频和低频场景下的平均完成率
wo_attn_means = [51.7, 58.7]  # w/o Attn在高频和低频场景下的平均完成率
wo_amn_means = [48.9, 66.9]  # w/o AMN在高频和低频场景下的平均完成率
ppo_means = [44.4, 61.4]  # PPO在高频和低频场景下的平均完成率
sac_means = [39.8, 56.3]  # SAC在高频和低频场景下的平均完成率


x = np.arange(len(categories))  # 横坐标位置
width = 0.15  # 柱状图的宽度

# 设置字体为Times New Roman
font_prop = FontProperties(family='Times New Roman', size=28)
# 设置标题字体为SimHei（黑体）
title_font = FontProperties(family='Microsoft YaHei')


fig, ax = plt.subplots(figsize=(12, 8))  # 设置图表大小
rects1 = ax.bar(x - 3*width, dedrs_means, width, label='RDSE',  capsize=5, color='#1f77b4', alpha=0.7)
rects2 = ax.bar(x - 2*width, wo_dgpa_means, width, label='w/o DGPA',  capsize=5, color='#ff7f0e', alpha=0.5)
rects3 = ax.bar(x - width, wo_attn_means, width, label='w/o Attn',  capsize=5, color='#2ca02c', alpha=0.3)
rects4 = ax.bar(x, wo_amn_means, width, label='w/o AMN',  capsize=5, color='#d62728', alpha=0.3)
rects5 = ax.bar(x + width, ppo_means, width, label='PPO',  capsize=5, color='#9467bd', alpha=0.5)
rects6 = ax.bar(x + 2*width, sac_means, width, label='A2C',  capsize=5, color='#8c564b', alpha=0.7)

# 设置Y轴标签的字体大小
ax.set_ylabel('物资受损率(%)', fontsize=28, fontproperties=title_font)  # 设置y轴标签的字体大小

# # 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=24, fontproperties=font_prop)  # 设置x轴标签的字体大小

# 设置标题的字体大小
# ax.set_title('物资受损率对比', fontsize=26, fontproperties=title_font)  # 设置标题的字体大小

# 设置X轴刻度标签的字体大小
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=28, fontproperties=title_font)  # 设置x轴刻度标签的字体大小

# 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=28)  # 设置y轴刻度的字体大小

# 设置Y轴刻度的字体样式
ax.set_yticklabels(
    ax.get_yticks(),  # 获取当前 Y 轴刻度值
    fontproperties=font_prop,  # 使用之前定义的字体属性
    fontsize=30  # 设置字体大小
)

# 设置图例的字体大小
ax.legend(fontsize=26, prop=font_prop,loc='upper left')  # 设置图例的字体大小

# 保存图片为SVG矢量图格式
plt.savefig('场景一物资受损率对比.svg', format='svg')
plt.tight_layout()  # 自动调整布局
# 显示图表
plt.show()


#场景二大论文物资受损率
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
categories = [ '低频','高频']
dedrs_means = [38.9, 48.9]  # DEDRS在高频和低频场景下的平均完成率
wo_dgpa_means = [63.7, 91.6]  # w/o DGPA在高频和低频场景下的平均完成率
wo_attn_means = [52.5, 59.3]  # w/o Attn在高频和低频场景下的平均完成率
wo_amn_means = [56.7, 69.1]  # w/o AMN在高频和低频场景下的平均完成率
ppo_means = [48.5, 64.6]  # PPO在高频和低频场景下的平均完成率
sac_means = [40.6, 57.3]  # SAC在高频和低频场景下的平均完成率


x = np.arange(len(categories))  # 横坐标位置
width = 0.15  # 柱状图的宽度

# 设置字体为Times New Roman
font_prop = FontProperties(family='Times New Roman', size=28)
# 设置标题字体为SimHei（黑体）
title_font = FontProperties(family='Microsoft YaHei')


fig, ax = plt.subplots(figsize=(12, 8))  # 设置图表大小
rects1 = ax.bar(x - 3*width, dedrs_means, width, label='RDSE',  capsize=5, color='#1f77b4', alpha=0.7)
rects2 = ax.bar(x - 2*width, wo_dgpa_means, width, label='w/o DGPA',  capsize=5, color='#ff7f0e', alpha=0.5)
rects3 = ax.bar(x - width, wo_attn_means, width, label='w/o Attn',  capsize=5, color='#2ca02c', alpha=0.3)
rects4 = ax.bar(x, wo_amn_means, width, label='w/o AMN',  capsize=5, color='#d62728', alpha=0.3)
rects5 = ax.bar(x + width, ppo_means, width, label='PPO',  capsize=5, color='#9467bd', alpha=0.5)
rects6 = ax.bar(x + 2*width, sac_means, width, label='A2C',  capsize=5, color='#8c564b', alpha=0.7)

# 设置Y轴标签的字体大小
ax.set_ylabel('物资受损率(%)', fontsize=28, fontproperties=title_font)  # 设置y轴标签的字体大小

# # 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=24, fontproperties=font_prop)  # 设置x轴标签的字体大小

# 设置标题的字体大小
# ax.set_title('物资受损率对比', fontsize=26, fontproperties=title_font)  # 设置标题的字体大小

# 设置X轴刻度标签的字体大小
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=28, fontproperties=title_font)  # 设置x轴刻度标签的字体大小

# 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=24)  # 设置y轴刻度的字体大小

# 设置Y轴刻度的字体样式
ax.set_yticklabels(
    ax.get_yticks(),  # 获取当前 Y 轴刻度值
    fontproperties=font_prop,  # 使用之前定义的字体属性
    fontsize=30  # 设置字体大小
)

# 设置图例的字体大小
ax.legend(fontsize=26, prop=font_prop,loc='upper left')  # 设置图例的字体大小

# 保存图片为SVG矢量图格式
plt.savefig('场景二物资受损率对比.svg', format='svg')
plt.tight_layout()  # 自动调整布局
# 显示图表
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
categories = ['低频','高频' ]
dedrs_means = [84.1, 68.8]  # DEDRS在高频和低频场景下的平均完成率
wo_dgpa_means = [59.6, 19.8]  # w/o DGPA在高频和低频场景下的平均完成率
wo_attn_means = [69.4, 55.6]  # w/o Attn在高频和低频场景下的平均完成率
wo_amn_means = [72.5, 45.8]  # w/o AMN在高频和低频场景下的平均完成率
ppo_means = [76.1, 54.5]  # PPO在高频和低频场景下的平均完成率
sac_means = [80.3, 57.9]  # SAC在高频和低频场景下的平均完成率

x = np.arange(len(categories))  # 横坐标位置
width = 0.15  # 柱状图的宽度

# 设置字体为Times New Roman
font_prop = FontProperties(family='Times New Roman', size=28)
# 设置标题字体为SimHei（黑体）
title_font = FontProperties(family='Microsoft YaHei')
# 创建柱状图
fig, ax = plt.subplots(figsize=(12, 8))  # 设置图表大小
rects1 = ax.bar(x - 3*width, dedrs_means, width, label='RDSE',  capsize=5, color='#1f77b4', alpha=0.7)
rects2 = ax.bar(x - 2*width, wo_dgpa_means, width, label='w/o DGPA',  capsize=5, color='#ff7f0e', alpha=0.5)
rects3 = ax.bar(x - width, wo_attn_means, width, label='w/o Attn',  capsize=5, color='#2ca02c', alpha=0.3)
rects4 = ax.bar(x, wo_amn_means, width, label='w/o AMN', capsize=5, color='#d62728', alpha=0.3)
rects5 = ax.bar(x + width, ppo_means, width, label='PPO',  capsize=5, color='#9467bd', alpha=0.5)
rects6 = ax.bar(x + 2*width, sac_means, width, label='A2C', capsize=5, color='#8c564b', alpha=0.7)

# 设置Y轴标签的字体大小
ax.set_ylabel('原任务完成率(%)', fontsize=28, fontproperties=title_font)  # 设置y轴标签的字体大小

# 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=24, fontproperties=font_prop)  # 设置x轴标签的字体大小

# 设置标题的字体大小
# ax.set_title('原任务完成率对比', fontsize=26, fontproperties=title_font)  # 设置标题的字体大小

# 设置X轴刻度标签的字体大小
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=28, fontproperties=title_font)  # 设置x轴刻度标签的字体大小

# 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=24)  # 设置y轴刻度的字体大小
# 设置Y轴刻度的字体样式
ax.set_yticklabels(
    ax.get_yticks(),  # 获取当前 Y 轴刻度值
    fontproperties=font_prop,  # 使用之前定义的字体属性
    fontsize=30  # 设置字体大小
)


# 设置图例的字体大小
ax.legend(fontsize=26, prop=font_prop,loc='upper right')  # 设置图例的字体大小

# 保存图片为SVG矢量图格式
plt.savefig('场景一原任务完成率对比.svg', format='svg')
plt.tight_layout()  # 自动调整布局
# 显示图表
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
categories = ['低频','高频' ]
dedrs_means = [82.3, 60.3]  # DEDRS在高频和低频场景下的平均完成率
wo_dgpa_means = [54.3, 24.8]  # w/o DGPA在高频和低频场景下的平均完成率
wo_attn_means = [70.3, 54.1]  # w/o Attn在高频和低频场景下的平均完成率
wo_amn_means = [68.4, 48.7]  # w/o AMN在高频和低频场景下的平均完成率
ppo_means = [70.2, 53.4]  # PPO在高频和低频场景下的平均完成率
sac_means = [77.4, 56.8]  # SAC在高频和低频场景下的平均完成率

x = np.arange(len(categories))  # 横坐标位置
width = 0.15  # 柱状图的宽度

# 设置字体为Times New Roman
font_prop = FontProperties(family='Times New Roman', size=28)
# 设置标题字体为SimHei（黑体）
title_font = FontProperties(family='Microsoft YaHei')
# 创建柱状图
fig, ax = plt.subplots(figsize=(12, 8))  # 设置图表大小
rects1 = ax.bar(x - 3*width, dedrs_means, width, label='RDSE',  capsize=5, color='#1f77b4', alpha=0.7)
rects2 = ax.bar(x - 2*width, wo_dgpa_means, width, label='w/o DGPA',  capsize=5, color='#ff7f0e', alpha=0.5)
rects3 = ax.bar(x - width, wo_attn_means, width, label='w/o Attn',  capsize=5, color='#2ca02c', alpha=0.3)
rects4 = ax.bar(x, wo_amn_means, width, label='w/o AMN', capsize=5, color='#d62728', alpha=0.3)
rects5 = ax.bar(x + width, ppo_means, width, label='PPO',  capsize=5, color='#9467bd', alpha=0.5)
rects6 = ax.bar(x + 2*width, sac_means, width, label='A2C', capsize=5, color='#8c564b', alpha=0.7)

# 设置Y轴标签的字体大小
ax.set_ylabel('原任务完成率(%)', fontsize=28, fontproperties=title_font)  # 设置y轴标签的字体大小

# # 设置X轴标签的字体大小
# ax.set_xlabel('Scenario', fontsize=24, fontproperties=font_prop)  # 设置x轴标签的字体大小

# 设置标题的字体大小
# ax.set_title('原任务完成率对比', fontsize=26, fontproperties=title_font)  # 设置标题的字体大小

# 设置X轴刻度标签的字体大小
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=28, fontproperties=title_font)  # 设置x轴刻度标签的字体大小

# 设置Y轴刻度的字体大小
# ax.tick_params(axis='y', labelsize=24)  # 设置y轴刻度的字体大小
# 设置Y轴刻度的字体样式
ax.set_yticklabels(
    ax.get_yticks(),  # 获取当前 Y 轴刻度值
    fontproperties=font_prop,  # 使用之前定义的字体属性
    fontsize=30  # 设置字体大小
)

# 设置图例的字体大小
ax.legend(fontsize=26, prop=font_prop,loc='upper right')  # 设置图例的字体大小

# 保存图片为SVG矢量图格式
plt.savefig('场景二原任务完成率对比.svg', format='svg')
plt.tight_layout()  # 自动调整布局
# 显示图表
plt.show()