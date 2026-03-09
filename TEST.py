import qrcode 
text = input("Ingresa Texto: ")
nombre_img = input("Ingresa el nombre de la imagen:   ")

img = qrcode.make(text)
img.save(nombre_img + ".png")