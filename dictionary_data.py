# turn your lyrics text into a string
lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"

# create an array
list_of_lyrics = lyrics.split(" ")

# create a list of unique lyrics
unique_words = set(list_of_lyrics)

print "lyrics:", lyrics

print "list of lyrics:", list_of_lyrics

# length of list of lyrics and length of unique lyrics
print "length of list_of_lyrics:", len(list_of_lyrics)
print "list of unique words:", unique_words
print "length of unique words:", len(unique_words)

# a dictionary with initial values (prior to any iteration)
word_histogram = dict.fromkeys(unique_words, 0)

# initial histogram values
print "word histogram:", word_histogram

# PYTHON FOR LOOP SYNTAX BTW....
for number_derp in [1,2,3,4]:
    print(number_derp +10)

# come back to try to break this down line by line but:
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word] + 1

# looped histogram values
print "word histogram:", word_histogram
