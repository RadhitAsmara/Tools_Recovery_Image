def repair_jpg(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    header = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF'
    if data[:21] != header:
        data = header + data[21:]

    footer = b'\xFF\xD9'
    if data[-2:] != footer:
        data = data[:-2] + footer

    with open(filename, 'wb') as f:
        f.write(data)
    print("JPG repaired successfully!")


repair_jpg("corrupted.jpg")
