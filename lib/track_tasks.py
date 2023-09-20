def track_tasks(text):
    if text == "":
        raise Exception("There is no any text")
    else:
        return 'TODO' in text 