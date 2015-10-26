def Budget(body)
	WeeklyBudget = 15
	DailyBudget = 10
	currency = "$"

	splittest = Budget.split()

	for InputWords in splittest:
	        word = InputWords.lower()
			if word == "weekly":
				word = "We found the word weekly"
				keyword = "weekly"
				break
	        if word == "daily":
	            print ("we found the word daily")
	            keyword = "daily"
	            break
	        if word == "spent" or word == "used" or word == "paid":
	            keyword = "paid"
	            break


	for words in splittest:
			if keyword == "weekly":
				try:
					floatwords = float(words)
					WeeklyBudget = WeeklyBudget + floatwords
					WeeklyBudget = str(WeeklyBudget)
					print ("We have added", currency + WeeklyBudget, "to your Weekly Budget")
				except:
					continue
			if keyword == "daily":
	                        try:
	                                floatwords = float(words)
	                                DailyBudget = DailyBudget + floatwords
	                                DailyBudget = str(DailyBudget)
	                                print ("We have added", currency + DailyBudget, "to your Weekly Budget")
	                        except:
	                                continue
	        if keyword == "paid":
	                        try:
	                                floatwords = float(words)
	                                WeeklyBudget = WeeklyBudget - floatwords
	                                WeeklyBudget = str(WeeklyBudget)
	                                DailyBudget = DailyBudget - floatwords
	                                DailyBudget = str(DailyBudget)
	                                print ("Your Budget for today is now", currency + DailyBudget)
	                                print ("Your Budget for this week is now", currency + WeeklyBudget)
	                        except:
	                                continue
            