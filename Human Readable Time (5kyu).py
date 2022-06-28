def make_readable(seconds):
    hours = 00
    minutes = 00
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds - (minutes * 60)
        if minutes >= 60:
            hours = minutes//60
            minutes = minutes - (hours * 60)
    if hours < 10:
        hours = f'0{hours}'
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'

    return f'{hours}:{minutes}:{seconds}'