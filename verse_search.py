import os
SOFIT = {"ם":"מ","ך":"כ","ן":"נ","ף":"פ","ץ":"צ"}
HEBREW = set("אבגדהוזחטיכךלמםנןסעפףצץקרשת")

def normalize_text(text):
	return "".join(SOFIT.get(ch, ch) for ch in text if ch in HEBREW)

def is_subsequence(text, pattern):
    j = 0
    for ch in text:
        if ch != pattern[j]: continue
        j += 1
        if j == len(pattern):
            return True
    return False

# ----- search conditions

books = ['Jeremiah', 'Amos', 'Joshua', 'Nahum', 'Zephaniah', 'Obadiah', 'Exodus', 'Numbers', 'Judges', 'Ezra', 'Isaiah', 'Chronicles_1', 'Joel', 'Proverbs', 'Zechariah', 'Chronicles_2', 'Malachi', 'Samuel_1', 'Haggai', 'Nehemiah', 'Samuel_2', 'Song_of_Songs', 'Kings_2', 'Genesis', 'Kings_1', 'Esther', 'Psalms', 'Job', 'Daniel', 'Ruth', 'Micah', 'Habakkuk', 'Jonah', 'Hosea', 'Deuteronomy', 'Ecclesiastes', 'Lamentations', 'Leviticus', 'Ezekiel']
name = "אבשלום"
search_type = "let"
max_len = 1000

norm_name = normalize_text(name)

# ----- search methods 

# Search books and find each matching pasuk
instances = []
for book in books : 
	# print(book)
	# load the book file 
	with open(f"{os.path.dirname(os.path.abspath(__file__))}/Tanach.txt/{book}.txt",'r') as file:
		# loop over each line
		for line in file.readlines():			
			# skips the line if it is not a pasuk line ie 
			if "\u202a" in line : continue 
			# slice the line string to get the pasuk and take from it the first and last letters 
			pasuk = line[10:line.index("\u202c")-2]
			letters = normalize_text(pasuk)
			if len(pasuk) > max_len : continue
			ok = False
			if search_type=="reg" : 
				ok = letters[0] == norm_name[0] and letters[-1] == norm_name[-1]
			elif search_type=="let" : 
				ok = is_subsequence(letters, norm_name)
			elif search_type=="bot" : 
				ok = (
                    letters[0] == norm_name[0] and letters[-1] == norm_name[-1]
                    and is_subsequence(letters, norm_name)
                )
			if ok:
				pasuk_num = line[2:5]
				perek_num =  line[6:9]
				instances.append(f"{book} :{perek_num}:{pasuk_num}: \u202b {pasuk} \u202c \n")

# ----- output

# write out pesukim with their location to a text file with the name containing the name searched for 
with open(f"{os.path.dirname(os.path.abspath(__file__))}/pesukim_for_{name}_using_{search_type}.txt","w") as file:
	for instance in instances:
		file.write(instance)	 

		