import os
# short script to load book names from Tanach.txt download
def get_book_names ():
	curDir = os.path.dirname(os.path.abspath(__file__)) + "/Tanach.txt"
	books = os.listdir(curDir)
	for i in range(len(books)):
		books[i] = books[i].split(".")[0]
	return(books)
