import os
# useful functions
# returns true if a letter is within the unicode space of regular hebrew letters
def is_hebrew(char):
	return char <= "ת" and char >="א"

# dictionary for sofit letters to their normal forms
convert_sofit = {"ם":"מ","ך":"כ","ן":"נ","ף":"פ","ץ":"צ"}
sofit = {"ם","ך","ן","ף","ץ"}

# finds the last hebrew letter of a string and converts it to regular form if need be  
def get_last_letter(pasuk):
	letter = ""
	for i in range (len(pasuk)-1,0,-1):
		if is_hebrew(pasuk[i]):
			letter = pasuk[i]
			break
		
	if (letter in sofit):
		letter = convert_sofit[letter]

	return letter

# finds the first hebrew letter of a string 
def get_first_letter(pasuk):
	for i in range (0,len(pasuk)-1,1):
		if is_hebrew(pasuk[i]):
			return pasuk[i]

books = ['Jeremiah', 'Amos', 'Joshua', 'Nahum', 'Zephaniah', 'Obadiah', 'Exodus', 'Numbers', 'Judges', 'Ezra', 'Isaiah', 'Chronicles_1', 'Joel', 'Proverbs', 'TanachHeader', 'Zechariah', 'Chronicles_2', 'Malachi', 'Samuel_1', 'Haggai', 'Nehemiah', 'Samuel_2', 'Song_of_Songs', 'Kings_2', 'Genesis', 'Kings_1', 'Esther', 'Psalms', 'Job', 'Daniel', 'Ruth', 'Micah', 'Habakkuk', 'Jonah', 'TanachIndex', 'Hosea', 'Deuteronomy', 'Ecclesiastes', 'Lamentations', 'Leviticus', 'Ezekiel']

# name input
name = "אבשלום"

first_letter = get_first_letter(name)
last_letter = get_last_letter(name)

# type of search 
search_type = "reg"

# regular match
def regular_match(pasuk):
	first = get_first_letter(pasuk)
	last = get_last_letter(pasuk)
	# check the first and last letters 
	if first == first_letter and last == last_letter:
		pasuk_num = line[2:5]
		perek_num =  line[6:9]
		#print(last)
		#print(f"found match in book {book} perek {perek_num} pasuk {pasuk_num}")
		#print(f"pasuk : \u202b {pasuk} \u202c")
		return f"{book} :{perek_num}:{pasuk_num}: \u202b {pasuk} \u202c \n"
	return None

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
			if search_type=="reg" and regular_match(pasuk) != None:
				instances.append(regular_match(pasuk))

# write out pesukim with their location to a text file with the name containing the name searched for 
with open(f"{os.path.dirname(os.path.abspath(__file__))}/pesukim_for_{name}.txt","w") as file:
	for instance in instances:
		file.write(instance)	 

		