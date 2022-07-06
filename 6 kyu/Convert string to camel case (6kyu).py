def to_camel_case(text):
    text = text.replace('_','-').split('-')
    camel = ''
    for i in text:
        if i.lower() == 'the' or i.lower() == 'a':
            camel += i
        else:
            camel += i.capitalize()
    return camel