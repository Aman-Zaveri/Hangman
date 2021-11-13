from bs4 import BeautifulSoup 
import requests
import random

url = "https://www.enchantedlearning.com/wordlist/"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")

startingThemes = ['Adjectives', 'Country Names', 'Landforms', 'School']
themes = []
words = []

for items in startingThemes:
    startingWord = soup.find_all(text=items)
    startingWordParent = startingWord[0].parent
    themesParent = startingWordParent.parent

    for tag in themesParent:
        themes.append(str(tag.text.strip()))

    while '' in themes:
        for topics in themes:
            if topics == '':
                themes.remove(topics)


letterWords = ''

while len(letterWords) < 1:
    chosenTheme = random.choice(themes)
    finalChosenTheme = ''.join(chosenTheme.split()).lower()

    linkRequest = "https://www.enchantedlearning.com/wordlist/" + finalChosenTheme + ".shtml"
    themeRequest = requests.get(linkRequest)
    themeSoup = BeautifulSoup(themeRequest.content, "html.parser")

    letterWords = themeSoup.find_all('div', class_ = 'wordlist-item')

for tags in letterWords:
    words.append(str(tags.text.strip()))

chosenWord = random.choice(words)

while " " in chosenWord or "." in chosenWord or "'" in chosenWord or '-' in chosenWord:
    chosenWord = random.choice(words)