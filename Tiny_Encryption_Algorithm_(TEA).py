QUALITYOFROUNDS=32
DELTA=0x9E3779B9
SIZEOFCHAR=8
SIZEOFCHAR_KEY=16

def tea_encode(text,keyword):

    text_bit=text.encode('utf-8')
    keyword_bit=keyword.encode('utf-8')
    keyword_bit_16=keyword_bit.ljust(16,b'\x00')
    text_blocks = (len(text_bit) + SIZEOFCHAR - 1) // SIZEOFCHAR
    blocks = text_blocks * SIZEOFCHAR
    text_bit8 = text_bit.ljust(blocks, b'\x00')
    blocks_text = [text_bit8[i:i + SIZEOFCHAR] for i in range(0, len(text_bit8), SIZEOFCHAR)]
    k0 = ((keyword_bit_16[0] << 24) | (keyword_bit_16[1] << 16) | (keyword_bit_16[2] << 8) | keyword_bit_16[3])
    k1 = ((keyword_bit_16[4] << 24) | (keyword_bit_16[5] << 16) | (keyword_bit_16[6] << 8) | keyword_bit_16[7])
    k2 = ((keyword_bit_16[8] << 24) | (keyword_bit_16[9] << 16) | (keyword_bit_16[10] << 8) | keyword_bit_16[11])
    k3 = ((keyword_bit_16[12] << 24) | (keyword_bit_16[13] << 16) | (keyword_bit_16[14] << 8) | keyword_bit_16[15])
    encrypted_data = b''
    for index, j in enumerate(blocks_text):
        current_block=j
        left = ((current_block[0]<<24)| (current_block[1]<<16)| (current_block[2]<<8) | current_block[3])
        right =((current_block[4]<<24)| (current_block[5]<<16)| (current_block[6]<<8) | current_block[7])

        summator = 0
        for i in range(QUALITYOFROUNDS):
            summator = (summator + DELTA) & 0xFFFFFFFF
            left=(left+(((right<<4)+k0)^ (right+summator)  ^((right>>5)+k1)))& 0xFFFFFFFF
            right=(right+(((left<<4)+k2)^ (left+summator)  ^((left>>5)+k3)))& 0xFFFFFFFF
        l1=(left >> 24) & 0xFF
        l2 = (left >> 16) & 0xFF
        l3 = (left >> 8) & 0xFF
        l4 = left  & 0xFF
        r1 = (right >> 24) & 0xFF
        r2 = (right >> 16) & 0xFF
        r3 = (right >> 8) & 0xFF
        r4 = right & 0xFF
        text_ready=bytes([l1,l2,l3,l4,r1,r2,r3,r4])
        encrypted_data+=text_ready
    return encrypted_data
def tea_decode(encode,keyword):
    keyword_bit = keyword.encode('utf-8')
    keyword_bit_16 = keyword_bit.ljust(16, b'\x00')
    k0 = ((keyword_bit_16[0] << 24) | (keyword_bit_16[1] << 16) | (keyword_bit_16[2] << 8) | keyword_bit_16[3])
    k1 = ((keyword_bit_16[4] << 24) | (keyword_bit_16[5] << 16) | (keyword_bit_16[6] << 8) | keyword_bit_16[7])
    k2 = ((keyword_bit_16[8] << 24) | (keyword_bit_16[9] << 16) | (keyword_bit_16[10] << 8) | keyword_bit_16[11])
    k3 = ((keyword_bit_16[12] << 24) | (keyword_bit_16[13] << 16) | (keyword_bit_16[14] << 8) | keyword_bit_16[15])
    blocks_text = [encode[i:i + SIZEOFCHAR] for i in range(0, len(encode), SIZEOFCHAR)]
    decrypted_data=b''
    for index, j in enumerate(blocks_text):
        current_block = j
        left = ((current_block[0] << 24) | (current_block[1] << 16) | (current_block[2] << 8) | current_block[3])
        right = ((current_block[4] << 24) | (current_block[5] << 16) | (current_block[6] << 8) | current_block[7])

        summator = (DELTA * QUALITYOFROUNDS) & 0xFFFFFFFF
        for i in range(QUALITYOFROUNDS):

            right = (right - (((left << 4) + k2) ^ (left + summator) ^ ((left >> 5) + k3))) & 0xFFFFFFFF
            left = (left - (((right << 4) + k0) ^ (right + summator) ^ ((right >> 5) + k1))) & 0xFFFFFFFF

            summator=(summator-DELTA) & 0xFFFFFFFF
        l1 = (left >> 24) & 0xFF
        l2 = (left >> 16) & 0xFF
        l3 = (left >> 8) & 0xFF
        l4 = left & 0xFF
        r1 = (right >> 24) & 0xFF
        r2 = (right >> 16) & 0xFF
        r3 = (right >> 8) & 0xFF
        r4 = right & 0xFF
        text_ready = bytes([l1, l2, l3, l4, r1, r2, r3, r4])
        decrypted_data += text_ready
    return decrypted_data.decode('utf-8',errors='ignore').rstrip('\x00')
text=input("Введите текст для шифрованием TEA: ")
keyword=input("Введите ключ шифрования TEA: ")
encode=tea_encode(text,keyword)
decode=tea_decode(encode,keyword)
print(encode)
print(decode)
