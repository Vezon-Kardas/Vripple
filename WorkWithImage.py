from PIL import Image, ImageDraw, ImageFont
import Database
#Упорядочить текcт
#Уникальное имя в оответтвии  индеком

class WorkWithImage(Database.Database):

    """
    Класс для подготовки шаблона и вставки и сохранения карточки-изображения.
    """

    __SIZE = (1380, 1380)
    __PLACE = (60, 60)
    __color = (255, 255, 255)
    __FONTSIZE_ONE = 42
    __FONTSIZE_TWO = 45
    __RECTANGLE = (60, 60, 1440, 1440)
    __ELLIPSE = (60, 1950, 160, 2050)
    __ONE_MULTILINE_TEXT = (625, 1975)
    __TWO_MULTILINE_TEXT = (90, 1700)
    __THREE_MULTILINE_TEXT = (1380, 1975)
    __font = ImageFont.truetype("arial.ttf", size=__FONTSIZE_ONE)
    __ID = ""
    def __init__(self, text, path, original_img_path, path_table):
        super().__init__(text, path, original_img_path, path_table)

    def template(self, add):
        """Функция для создания шаблона для последующей вставки изображения.
        Принимает аргумент кортеж(дату и текст-опиание), сохраненный в базу данных"""
        self.__ID = str(add[1])
        fontOneText = ImageFont.truetype("arial.ttf", size=self.__FONTSIZE_ONE)
        fontTwoText = ImageFont.truetype("arial.ttf", size=self.__FONTSIZE_TWO)

        img = Image.new('RGB', (1500, 2102), self.__color)
        imgDrawer = ImageDraw.Draw(img)

        imgDrawer.rectangle(self.__RECTANGLE, fill=None, outline=(0, 0, 0), width=5)
        imgDrawer.ellipse(self.__ELLIPSE, outline=(128, 128, 128), width=5)

        imgDrawer.multiline_text(self.__ONE_MULTILINE_TEXT, str(add[0]), font=fontOneText, fill=(0, 0, 0), align="center")
        imgDrawer.multiline_text(self.__TWO_MULTILINE_TEXT, self.text, font=fontTwoText, fill=(0,0,0), align="center")
        imgDrawer.multiline_text(self.__THREE_MULTILINE_TEXT, str(add[1]), font=fontOneText, fill=(0,0,0))

        img.save('piu@yandex.ru/InWork/pil-basic-example.png')

    def pasteImageInTemplate(self):

        one_image = Image.open("piu@yandex.ru/InWork/pil-basic-example.png")
        two_image = Image.open("piu@yandex.ru/Photo/{0}.jpg".format(self.original_img_path))

        two_image.resize(self.__SIZE).save("piu@yandex.ru/InWork/Save.jpg")
        two_image = Image.open("piu@yandex.ru/InWork/Save.jpg")
        one_image.paste(two_image, self.__PLACE)
        one_image.save("piu@yandex.ru/ReadyCard/{0}/{1}.jpg".format(self.path_table, self.__ID))


