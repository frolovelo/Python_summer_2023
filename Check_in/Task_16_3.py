def title_text(func):
    def wrapper(text):  # если функция что-то меняет, то надо бы и передавать ей что-то на вход!
        return func(text).title()
    return wrapper

@title_text
def change_text(text):
    return text

print(change_text('hhheLLLLLLLooooOOOOoooo'))