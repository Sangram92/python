def all_matches(needle, haystack):
	result = []
	for i in xrange(len(haystack) - len(needle) + 1):
		if is_match(needle, haystack, i):
			result.append(i)
	return result

def is_match(needle, haystack, i):
	for j in xrange(len(needle)):
		if needle[j] != haystack[i+j]:
			return False
	return True

print all_matches("calcium", "The patient ingested calcium 15mg and had severe side effects.")