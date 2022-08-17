def amount_of_pages(summary):
    count = ''
    if summary < 10:
        return summary
    for i in range(1,summary**2):
        count += str(i)
        if len(count) == summary:
            return (i)