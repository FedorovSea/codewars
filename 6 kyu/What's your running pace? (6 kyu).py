def running_pace(distance, time):
    minutes, second = time.split(":")
    second_per_minutes = int(minutes)*60 + int(second)
    distance = second_per_minutes / distance
    return f'{int(distance//60)}:{int(distance%60)}'