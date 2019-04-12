import goslate

text = "ciao a tutti\nmi chiamo andrea\ne sono bello\ne mi piace giocare con le bambole"

gs = goslate.Goslate()
translatedText = gs.translate(text,'en')

print(translatedText)