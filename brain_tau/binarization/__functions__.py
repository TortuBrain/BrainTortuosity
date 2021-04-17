from PIL import Image

image_bin=Image.open('path')


if image_bin.mode != 'L':
    image_bin=image_bin.convert('L')


umbral=65

datos=image_bin.getdata()
datos_binarios=[]

for x in datos:
    if x<umbral:
        datos_binarios.append(0)
        continue
 
    datos_binarios.append(1)

nueva_imagen=Image.new('1', image_bin.size)
nueva_imagen.putdata(datos_binarios)
nueva_imagen.save('path')

nueva_imagen.close()
image_bin.close()