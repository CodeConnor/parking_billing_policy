# import datetime
#
# 获取当前时间
import datetime

in_time = datetime.datetime.now()

time_str = input('请输入汽车的出场时间（格式：年-月-日 小时:分钟:秒）：')  #
out_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

#
# 计算out_time - in_time
result_time = datetime.date(out_time) - datetime.date(in_time)

# 输出结果
print("输入的时间为：", out_time)
print("当前时间为：", in_time)
print("结果为：", result_time)


