"""
Pillow: redimensionando imagens com Python
Essa biblioteca é como um photoshop do Python
Documentação Pillow: https://pillow.readthedocs.io/en/stable/
"""
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = 'Modulo_4_Modulos_em_Python\\Aula\\AulaExtra_ConsumindoAPI_REST_Com_Python\\Consumir_API\\2015-02-03-21-29-27\
--990592242.jpeg'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

pil_image = Image.open(ORIGINAL)
print(pil_image.size)
width, height = pil_image.size
print(pil_image.info)
exif = pil_image.info['jfif']

new_width = 800
new_height = round(height * new_width / width)

print(width, height)
print(new_width, new_height)

nova_imagem = pil_image.resize(size=(new_width, new_height))
nova_imagem.save(NEW_IMAGE, optimize=True, quality=100)
