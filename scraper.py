from bs4 import BeautifulSoup
import os
import time
from deep_translator import GoogleTranslator


# import re
# import asyncio
#
# valid_pattern = re.compile(r'[a-z]', re.I)
#
# start_time = time.time()  # start timer
#
# def get_valid_strings():
#     for navigable_string in soup.strings:
#         if valid_pattern.search(navigable_string):
#             yield navigable_string
#
#
# async def translate(navigable_string):
#     print(f'translating {navigable_string} [...]')
#     translated_string = GoogleTranslator(source='auto', target='hi').translate(navigable_string)
#     return navigable_string, translated_string
#
#
# async def translate_strings():
#     for navigable_string, translated_string in await asyncio.gather(*map(translate, get_valid_strings())):
#         print(f'changing {navigable_string} to {translated_string} [...]')
#         navigable_string = translated_string
#
#
# # for root, dirs, files in os.walk("ClassCentral2/www.classcentral.com/"):
# #     for file_name in files:
# #         if file_name.endswith(".html"):
# file_path = 'ClassCentral2/www.classcentral.com/about.html'
#
# with open(file_path, "r+", encoding="utf-8", errors="ignore") as file:
#     soup = BeautifulSoup(file, "html.parser")
#
# asyncio.run(translate_strings())
# end_time = time.time()  # end timer
# print(f"{file_path} translated and saved in {round(end_time - start_time, 2)} seconds.")
# import io

# start_time = time.time()  # start timer
# file_path = 'ClassCentral2/www.classcentral.com/collections.html'
#
# with open(file_path, "r+", encoding="utf-8", errors="ignore") as file:
#     soup = BeautifulSoup(file, "html.parser")
# BUFFER_SIZE = 4_999  # change this to maximum file size limit
#
# navigable_strings = list(soup.strings)
# chunks = []
#
# # translate full text but with null seperation character
# with io.StringIO('\x00'.join(navigable_strings)) as s_raw:
#     chunks.append(GoogleTranslator(source='auto', target='hi').translate(s_raw.read(BUFFER_SIZE)))
#
# tmp = ''.join(chunks).split('\x00')
# print(len(tmp), len(navigable_strings))
#
# # split text into chunks and then modify strings
# for navigable_string, translated_string in zip(navigable_strings, ''.join(chunks).split('\uffff')):
#     print(f'changing {navigable_string} to {translated_string} [...]')
#     navigable_string = translated_string
#
# end_time = time.time()  # end timer
# print(f"{file_path} translated and saved in {round(end_time - start_time, 2)} seconds.")

# for root, dirs, files in os.walk("ClassCentral2/www.classcentral.com/"):
#     for file_name in files:
#         if file_name.endswith(".html"):
#             file_path = os.path.join(root, file_name)
#
#             with open(file_path, "r+", encoding="utf-8", errors="ignore") as file:
#                 soup = BeautifulSoup(file, "html.parser")
#
#             print(f"Translating {file_path}...")
#             start_time = time.time()  # start timer
#
#             original_text = ""
#             for string in soup.stripped_strings:
#                 original_text += str(string) + "\n"
#
#             # Split the original text into chunks of 5000 characters or less
#             chunk_size = 4999
#             chunks = [original_text[i:i+chunk_size] for i in range(0, len(original_text), chunk_size)]
#
#             # Translate each chunk separately and concatenate the results
#             translated_text = ""
#             for chunk in chunks:
#                 translated_chunk = GoogleTranslator(source='auto', target='hi').translate(chunk)
#                 if translated_chunk:
#                     translated_text += translated_chunk + "\n"
#
#             print(f'{translated_text} -> {original_text}')
#
#             # Split the original and translated strings back into individual strings and replace the original strings
#             # with the translated strings
#             for original_string, translated_string in zip(original_text.split("\n"), translated_text.split("\n")):
#                 soup.find(string=original_string).replace_with(translated_string)
#
#             # with open(file_path, "w", encoding="utf-8") as file:
#             #     file.write(str(soup))
#
#             end_time = time.time()  # end timer
#             print(f"{file_path} translated and saved in {round(end_time - start_time, 2)} seconds.")

for root, dirs, files in os.walk("path/path/directory"):
    for file_name in files:
        if file_name.endswith(".html"):
            file_path = os.path.join(root, file_name)
            with open(file_path, "r+", encoding="utf-8", errors="ignore") as file:
                soup = BeautifulSoup(file, "html.parser")

            print(f"Translating {file_path}...")
            start_time = time.time()  # start timer

            for string in soup.stripped_strings:
                original_string = str(string)
                translated_string = GoogleTranslator(source='en', target='hi').translate(original_string)
                if translated_string is not None:
                    soup = BeautifulSoup(str(soup).replace(original_string, translated_string), "html.parser")
                    print(f'{original_string} -> {translated_string}')
                else:
                    print(f'Skipping {original_string} because translation failed.')

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(str(soup))

            end_time = time.time()  # end timer
            print(f"{file_path} translated and saved in {round(end_time - start_time, 2)} seconds.")
