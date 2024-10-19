
import pyscreenshot as ImageGrab


def screen_capture():
    imagem = ImageGrab.grab()
    imagem.save('./app/img.png', 'png')

    