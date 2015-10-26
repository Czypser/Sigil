def Keyword(Body)
	SplitMessage = Keyword.split()
	for Word in SplitMessage:
		Word = Word.lower()
		if word == "weekly":
			Weekly(Keyword)
			break
		if word == "daily":
			Daily(Keyword)
			break
		if word == "weekly":
			Weekly(Keyword)
			break

