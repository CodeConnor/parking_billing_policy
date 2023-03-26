# 车场计费策略，
# 早8点到晚10点：15分钟免费，每小时2元。
# 晚10点到早8点：15分钟免费，每小时2元，夜间封顶5元。
# 根据入场出场时间，输出计费金额

# 导入 datetime和math模块
import datetime
# 定义费用和时间
fees = 0  # 定义总停车费
top_cost = 5  # 夜间封顶费用
per_hours_cost = 2  # 每小时停车费
day_hours = 14  # 定义白天时间，22-8总共14小时

# 模拟汽车入场，实际场景是接收从地磁传来的信号？
admission = bool(input('车辆是否入场（输入任意字符代表入场）：'))
if admission:
    print('入场成功')
    # 获取车辆入场和出场时间
    time_str1 = input('请输入车辆入场时间（格式：年-月-日 小时:分钟:秒）：')   # 手动输入车辆入场时间
    entry_time = datetime.datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")  # 将输入的字符串解析为日期和时间
    time_str2 = input('请输入出场时间（格式：年-月-日 小时:分钟:秒）：')  # 手动输入车辆出场时间
    exit_time = datetime.datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")

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
    night_time = datetime.datetime.combine(entry_time.date(), datetime.time(hour=22, minute=00, second=00))
    # 排除22:00之后入场的情况
    if entry_time >= night_time:
        entry_diff = 0
    else:
        entry_diff = (night_time - entry_time).total_seconds() // 3600
        entry_diff += 1  # 向上取整

    # 同上，定义一个出场时间差，用于计算车辆出场当天，晚于8点出场而产生的停车时间
    morning_time = datetime.datetime.combine(exit_time.date(), datetime.time(hour=8, minute=00, second=00))
    # 排除8:00之前出场的情况
    if exit_time <= morning_time:
        exit_diff = 0
    else:
        exit_diff = (exit_time - morning_time).total_seconds() // 3600
        exit_diff += 1

    # 计算停车时间
    parking_time = exit_time - entry_time
    # 分别获取停车时间的天数，秒数和微秒数
    days = parking_time.days
    seconds = parking_time.seconds
    microseconds = parking_time.microseconds
    # 将秒和微秒数合并为总秒数
    total_seconds = seconds + microseconds / 1000000
    # 计算小时、分钟和秒数
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # 判断停车时间是否超过15min，不超过即免费
    if parking_time < datetime.timedelta(minutes=15):  # 判断停车时间是否超过15min
        fees = 0
        print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')

    # 判断停车时间是否超过2小时
    elif parking_time < datetime.timedelta(hours=2):
        # 判断是否为整小时，例如1小时0分0秒
        if seconds > 0:
            # 非整小时：费用中的小时数向上取整
            fees = (hours + 1) * per_hours_cost
            print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')
        else:
            # 整小时：小时数不用向上取整
            fees = hours * per_hours_cost
            print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')

    # 判断入场时间是否在早上6点之前
    elif entry_time < critical_time:
        # 计算夜间封顶费用
        fees += top_cost * (date_diff + 1)
        # 停车费公式
        fees += ((day_hours * date_diff) + exit_diff) * per_hours_cost
        print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')

    else:
        # 计算夜间封顶费用
        fees += top_cost * date_diff
        # 停车费公式
        fees += (entry_diff + exit_diff + day_hours * (date_diff - 1)) * per_hours_cost
        print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')

else:
    print('入场失败或者暂无汽车入场')
