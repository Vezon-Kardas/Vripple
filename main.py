import WorkWithImage

start = WorkWithImage.WorkWithImage("piu@yandex.ru/piu@yandex.ru.db",
                                    "      Every action has its consequences. So was it and so will.",#_________________
                                    "Example",
                                    "Личное")
add = start.addDataRetrieval()
print(add)
start.template(add)
start.pasteImageInTemplate()

