
def get_matching_string(dic, text):
	try:
		import time
		start_time = time.time()
		text_lst = text.split(" ")
		if len(dic) and len(text):
			for word in dic:
				wlen = len(word.split(" "))
				start_idx = 0
				end_idx = 0 + wlen
				while not end_idx > len(text_lst):
					# if string is multi worded. make string of that much length of words and find matching string
					search_in = " ".join(text_lst[start_idx: end_idx])
					# matching ratio is set to 0.75
					if get_ratio(word, search_in) > 0.75 and not ("<" in search_in or ">" in search_in):
						if text_lst[start_idx] == text_lst[end_idx-1]:
							text_lst[start_idx] = "<"+str(text_lst[start_idx])+">"
						else:
							text_lst[start_idx] = "<" + str(text_lst[start_idx])
							text_lst[end_idx-1] = str(text_lst[end_idx-1]) + ">"
					end_idx += 1
					start_idx += 1
	except Exception as e:
		print "Something went wrong, while matching the string", e
	finally:
		print "Execution time: ", time.time() - start_time
		print "Matching strings are shown in < > : \n"
		return " ".join(text_lst)

def get_ratio(str1, str2):
	"""return matching ration of given strings"""
	from difflib import SequenceMatcher
	s = SequenceMatcher(None, str1, str2)
	return s.ratio()

text = """The patient ingested calcium 15mg and had serious side effects.
	Another patient who took calcium tablets also had similar reactions kidney stone."""
dic = ["Tylenol", "calcium","sodium acetate", "Calcium",  "kiney ston"]

print get_matching_string(dic, text)