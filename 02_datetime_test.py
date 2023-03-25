# 导入 datetime和math模块
import datetime
import math
# 定义费用和时间
fees = 0  # 定义总停车费
top_cost = 5  # 夜间封顶费用
per_hours_cost = 2  # 每小时停车费
day_hours = 14  # 定义无封顶费用的停车时间，22-8总共14小时

# 模拟汽车入场，实际场景是接收从地磁传来的信号？
admission = bool(input('车辆是否入场（输入任意字符代表入场）：'))
if admission:
    print('入场成功')
    # 获取车辆入场和出场时间
    time_str1 = input('请输入车辆入场时间（格式：年-月-日 小时:分钟:秒）：')   # 手动输入车辆入场时间
    entry_time = datetime.datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")  # 将输入的字符串解析为日期和时间
    time_str2 = input('请输入出场时间（格式：年-月-日 小时:分钟:秒）：')  # 手动输入车辆出场时间
    exit_time = datetime.datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")
    print(f'入场时间：{entry_time}')
    print(f'出场时间：{exit_time}')

    # 获取车辆的入场日期和出场日期之差
    entry_date = entry_time.date()  # 入场日期
    exit_date = exit_time.date()  # 出场日期
    date_diff = max((exit_date - entry_date).days, 0)

    # 定义一个入场临界时间，该时间为车辆入场当天的早上6点
    # 因为在6点之后停车不可能触发夜间封顶费用
    # 而在当天6点之前停车就有可能触发夜间封顶费用
    critical_time = datetime.datetime.combine(entry_time.date(), datetime.time(hour=6, minute=0, second=0))

    # 定义一个入场时间差，用于计算车辆在22:00之前入场时，而产生的停车时间
    # 定义晚上10点，用于计算差值
    night_time = datetime.datetime.combine(entry_time.date(), datetime.time(hour=22, minute=0, second=0))
    # 计算时间差
    entry_diff = (night_time - entry_time).total_seconds() // 3600
    entry_diff = max(0, entry_diff)  # 如果时间差为负数则视为0
    entry_diff = math.ceil(entry_diff)  # 向上取整

    # 同上，定义一个出场时间差，用于计算车辆出场当天，晚于8点出场而产生的停车时间
    morning_time = datetime.datetime.combine(exit_time.date(), datetime.time(hour=8, minute=0, second=0))
    # 计算时间差，步骤合并
    exit_diff = (exit_time - morning_time).total_seconds() // 3600
    exit_diff = max(0, exit_diff)
    exit_diff = math.ceil(exit_diff)
    print(f'exit_diff={exit_diff}')
    print(f'entry_diff={entry_diff}')