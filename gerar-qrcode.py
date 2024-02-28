import segno


def gerar_qrcode(numero, imagem, nome):
    url = f'https://api.whatsapp.com/send?phone=5598{numero}'
    qrcode = segno.make(url)
    qrcode.to_artistic(background=imagem, target=f'{nome}.jpeg', scale=10)
    return qrcode


if __name__ == '__main__':
    numero = input('Digite o numero: ')
    imagem = 'src/mateus.jpeg' # Alterar pela imagem que colocar na pasta SRC
    nome = input('Digite o nome: ')
    gerar_qrcode(numero, imagem, nome).save(f'{nome}.png', scale=10)
