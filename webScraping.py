from bs4 import BeautifulSoup 
import requests
import random


#Obtaining url
url = "https://www.enchantedlearning.com/wordlist/"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")

#Creating variable that will be used later
startingThemes = ['Adjectives', 'Country Names', "Landforms", 'School']
themes = []
words = []

letterWordsChecker = False
index = 0

#Finding all the themes
while index < 4:
    startingWord = soup.find_all(text=startingThemes[index])
    startingWordParent = startingWord[0].parent
    themesParent = startingWordParent.parent

    for tag in themesParent:
        themes.append(str(tag.text.strip()))

    while '' in themes:
        for topics in themes:
            if topics == '':
                themes.remove(topics)

    index += 1

#CHoosing theme
while letterWordsChecker == False:
    chosenTheme = random.choice(themes)
    finalChosenTheme = ''.join(chosenTheme.split()).lower()

    #Obtaining words from new url
    linkRequest = "https://www.enchantedlearning.com/wordlist/" + finalChosenTheme + ".shtml"
    themeRequest = requests.get(linkRequest)
    themeSoup = BeautifulSoup(themeRequest.content, "html.parser")

    #Finding all words in the chosen theme
    letterWords = themeSoup.find_all('div', class_ = 'wordlist-item')

    if len(letterWords) > 1:
        letterWordsChecker == True

#Making sure words are listed neatly, without spaces
for tags in letterWords:
    words.append(str(tags.text.strip()))

#Choosing a word from the chosen theme
chosenWord = random.choice(words)

#Making sure characters aren't in the word
while " " in chosenWord or "." in chosenWord or "'" in chosenWord or '-' in chosenWord:
    chosenWord = random.choice(words)