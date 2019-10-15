
text = "The patient ingested calcium 15mg and had serious side effects. \
	Another patient who took calcium tablets also had similar reactions kidney stone."
dic = ["Tylenol", "calcium","sodium acetate", "kiddney stone"]


def simple_match(dic, text):
	"""This is simple string match method which simply search for matching words in given string"""
	for d in dic:
		if d.upper() in text:
			text = text.replace(d.upper(), "<"+d.upper()+">")
		elif d.lower() in text:
			text = text.replace(d.lower(), "<"+d.lower()+">")
		elif d.title() in text:
			text = text.replace(d.title(), "<"+d.title()+">")
	return text
print "Simple Match :\n"
print simple_match(dic, text), "\n\n"




def difflib_longest_match(needle, haystack):
	"""Here difflib in python used to find longest match"""
	import difflib
	for word in needle:
		 s = difflib.SequenceMatcher(None, haystack, word)
		 a,b,size = s.find_longest_match(0,len(haystack),0,len(word))
		 if a != 0:
		 	ratio = float(size)/len(word)*100
		 	if ratio > 75:
		 		match = haystack[a: a + size]
		 		print "match", match, haystack.find(match)
		 		haystack = 	haystack.replace(match, "<"+match+">")
	return haystack

print "Match using difflib in Python :\n"
print difflib_longest_match(dic, text)