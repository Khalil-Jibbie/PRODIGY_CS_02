from PIL import Image # type: ignore

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    img_encrypted = Image.new(img.mode, img.size)
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
          
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            img_encrypted.putpixel((x, y), encrypted_pixel)
    
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    img_encrypted.save(encrypted_image_path)
    print(f"Image encrypted successfully with adjustment of {key}. Encrypted image saved as {encrypted_image_path}.")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    img_encrypted = Image.open(encrypted_image_path)
    width, height = img_encrypted.size
    img_decrypted = Image.new(img_encrypted.mode, img_encrypted.size)
    
    for y in range(height):
        for x in range(width):
            pixel = img_encrypted.getpixel((x, y))
          
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            img_decrypted.putpixel((x, y), decrypted_pixel)
    
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img_decrypted.save(decrypted_image_path)
    print(f"Image decrypted successfully with adjustment of {key}. Decrypted image saved as {decrypted_image_path}.")
    return decrypted_image_path

image_path = 'jcole.png'
key = 40  
encrypted_image_path = encrypt_image(image_path, key)

decrypted_image_path = decrypt_image(encrypted_image_path, key)
