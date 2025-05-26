from PIL import Image
import sys

def encode(file_path, message):
    def set_lsb(byte, bit):
        return byte | 1 if bit == 1 else byte & ~1

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += format(0, '08b') # Terminating character
    
    with Image.open(file_path) as img:
        img = img.convert("RGB")
        pixels = list(img.getdata())

        if len(pixels)*3 < len(binary_message):
            print("Message too large for image")
            sys.exit(1)

        message_bit_index = 0
        modified_pixels = []
        for pixel in pixels:
            modified_pixel = list(pixel)
            for i in range(3):
                if message_bit_index < len(binary_message):
                    modified_pixel[i] = set_lsb(pixel[i], int(binary_message[message_bit_index]))
                    message_bit_index += 1

            modified_pixels.append(tuple(modified_pixel))

        new_img = Image.new(img.mode, img.size)
        new_img.putdata(modified_pixels)
        new_img.save(f'out_{file_path}')
        
def decode(file_path):
    def get_lsb(byte):
        return 1 if byte & 1 == 1 else 0
    
    binary_message = ''

    with Image.open(file_path) as img:
        img = img.convert("RGB")
        pixels = list(img.getdata())

        for pixel in pixels:
            for channel in pixel:
                binary_message += str(get_lsb(channel))
                if len(binary_message) % 8 == 0 and binary_message[-8:] == '00000000':
                    return binary_message[:-8]
    return None
                
def binary_to_ascii(binary_string):
    ascii_message = ""

    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        ascii_char = chr(int(byte, 2))
        ascii_message += ascii_char
        
    return ascii_message

def main(argv):
    if len(argv) != 2:
        print("Usage: python3 steno.py <filename>")
        sys.exit(1)

    file_path = argv[1]
    
    mode = None
    while mode != 1 and mode != 2:
        mode = int(input("1) Encode\n2) Decode\nChose mode: "))
    
    if mode == 1:
        message = input("Enter message: ")
        encode(file_path, message)
    elif mode == 2:
        binary_string = decode(file_path)
        if binary_string:
            print(binary_to_ascii(binary_string))
        else:
            print("The image does not contain a LSB stenography string")

if __name__ == "__main__":
    main(sys.argv)
