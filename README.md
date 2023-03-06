# BS4-Deeptranslator-HTML-files

## **Web Scraping and Translation Project** ##

This project involves web scraping and translation of website content. We will use HTTrack to copy pages of the website, and set the desired depth of the copy.

## **Installation** ##

To install the required packages, run the following command:

```
pip install -r requirements.txt
```
## **Usage** ##

1. Copy the pages of the website using HTTrack and save them in a local directory.

2. Open the scraper.py file and modify the file_path variable to point to the local directory where the copied pages are saved.

3. Run the following command to start the translation process:

```
python scraper.py
```

The script will parse the copied HTML files using Beautiful Soup and extract the text from them.

4. The text will then be translated from English to Hindi using the deep_translator API.

5. Finally, the HTML files will be updated with the translated strings.

## **Acknowledgements** ##
* HTTrack
* Beautiful Soup
* deep_translator API


## **P.S** ##
It's not finished


