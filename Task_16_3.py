def title_text(func):
    def wrapper():
        return func().title()
    return wrapper

@title_text
def change_text():
    return input()

print(change_text())