# 车场计费策略，
# 早8点到晚10点：15分钟免费，每小时2元。
# 晚10点到早8点：15分钟免费，每小时2元，夜间封顶5元。
# 根据入场出场时间，输出计费金额

# 导入 datetime 模块
import datetime
# 定义费用和时间
top_cost = 5  # 夜间封顶费用
per_hours_cost = 2  # 每小时停车费
fees = 0  # 定义总停车费
day_hours = 14  # 定义无封顶费用的停车时间，22-8总共14小时

if True:
    # 模拟汽车入场，实际场景是接收从地磁传来的信号？
    admission = bool(input('车辆是否入场（输入任意字符代表入场）：'))
    print('入场成功')

    # 获取车辆入场和出场时间
    in_time = datetime.datetime.now()  # 获取当前时间
    time_str = input('请输入汽车的出场时间（格式：年-月-日 小时:分钟:秒）：')  # 手动输入汽车时间，实际场景应该是汽车出场传回出场时间
    out_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")  # 将输入的字符串解析为日期和时间

    # 定义一个临界时间，该时间为车辆入场当天的早上6点
    # 因为在6点之后停车不可能触发夜间封顶费用
    # 而在当天6点之前停车就有可能触发夜间封顶费用
    critical_time = datetime.datetime.combine(in_time.date(), datetime.time(hour=6, minute=0, second=0))

    # 计算停车时间
    parking_time = out_time - in_time

    # 分别获取停车时间的天数，秒数和微秒数
    days = parking_time.days
    seconds = parking_time.seconds
    microseconds = parking_time.microseconds

    # 将秒和微秒数合并为总秒数
    total_seconds = seconds + microseconds / 1000000

    # 计算小时、分钟和秒数
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # 判断停车时间是否超过15min，不超即免费
    if parking_time < datetime.timedelta(minutes=15):  # 判断停车时间是否超过15min
        fees = 0
        print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')
    else:
        # 判断停车时间是否小于2小时
        if parking_time < datetime.timedelta(hours=2):
            # 不超过2小时就按每小时2元计算，因为向上取整所以hours要+1
            if minutes > 0:
                fees = (hours + 1) * per_hours_cost
                print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')
            # 排除刚好2小时0分的情况，防止多计算一小时费用
            else:
                fees = hours * per_hours_cost
                print(f'您的停车时间为{days}天{hours}时{minutes}分{seconds}秒，停车费为{fees}元')
        else:
            # 超过两小时后就判断停车时间是否在早上6点之后
            if in_time > critical_time:
                # 判断从车辆入场到出场是否跨越了一天
                if


else:
    print('暂无汽车入场')
# car_in = time.localtime()
# car_out = time.localtime() 15min / 10:00 - 20:00  / 20:00 - 9:59 / 1day


print(type(in_time))
print(in_time)
print(type(out_time))
print(out_time)