from googletrans import Translator

translator = Translator()


def translate(chinese_word):
    return translator.translate(chinese_word).text


if __name__ == '__main__':
    a = translator.translate("杭州")
