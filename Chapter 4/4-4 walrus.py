tweet_limit = 280
tweet_string = "Blah" * 150
diff = tweet_limit - len(tweet_string)
if diff >= 0 :
	print("A fitting tweet")
else :
	print("Went over by", abs(diff))

tweet_limit = 280
tweet_string = "Blah" * 250
if diff := tweet_limit - len(tweet_string) >= 0 :
	print("A fitting tweet", diff)
else :
	print("Went over by", abs(diff))


# The book describes these two as the same, however the 
# 2-step assigns an int to diff and the walrus essentially 
# assigns a boolean to diff...