# stenography-tool

Basic python implementation of LSB (Least Significant Bit) stenography to **encode** and **decode** hidden messages in images.

## Dependencies
- Pillow

```bash
pip install Pillow
```

## Usage
You can encode or decode hidden messages in an image by passing your image file as an argument.
```bash
python3 steno.py my_img.png
```

You will then be prompted to encode a new message or attempt to decode a message.
```txt
1) Encode
2) Decode
Chose Mode: 1
Enter Message: Hello, World!
```

# Contributing

Feel free to contribute, all PRs welcome.
