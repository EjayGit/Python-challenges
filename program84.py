# Write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib

sentence = "hello world!hello world!hello world!hello world!"

compressedSentence = zlib.compress(sentence.encode())
decompressedSentence = zlib.decompress(compressedSentence).decode()

print(f'Original Sentence: {sentence}')
print(f'Compressed Sentence: {compressedSentence}')
print(f'Decompressed Sentence: {decompressedSentence}')