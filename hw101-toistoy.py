import urllib
import re
import numpy as np
url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
text = urllib.request.urlopen(url)

words =[]
for i in text:
    line=i.decode("utf-8")
    for word in line.lower().split():
        if re.findall('\w+', word) and word not in words:
            word = re.sub(r"[^a-zA-Z]", "", word)
            word = re.sub(r"[ixv]", "", word)
            word =  word.strip()
            words.append(word)
unique_words = np.array(words)
unique_words_list = np.unique(unique_words)
print(len(unique_words_list))

