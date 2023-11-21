from datetime import timedelta,datetime, time as dt_time
end_time = datetime.combine(datetime.now().date(), dt_time(16, 0))
print(end_time,datetime.now())
    