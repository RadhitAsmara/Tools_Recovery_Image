def repair_png(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    header = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00'
    if data[:18] != header:
        data = header + data[18:]

    footer = b'\x00\x00\x00\x00IEND\xaeB`\x82'
    if data[-12:] != footer:
        data = data[:-12] + footer

    with open(filename, 'wb') as f:
        f.write(data)
    print("PNG repaired successfully!")


repair_png("corrupted.png")
