#!/usr/bin/env python3
'''
This script translates timezones and prints the result to and the 
translation table along with a column that lets you know if it's a 
good time to call.
'''

def good_time(a, b):
	if a > 6 and b > 6:
		return "YES"
	return " "

pst_ephem = [(x, "AM" if x < 12 else "PM") for x in range(0, 25)]
cet_ephem = [((x+9)%24, "AM" if (x+9) < 12 else "PM") for x in range(0, 25)]
print("PST",  "\t= ", "CET", "\t\tGood time to call?")
for pst, cet in zip(pst_ephem, cet_ephem):
	pst, pst_ampm = pst
	cet, cet_ampm = cet
	print(pst%12, pst_ampm, "\t= ", cet%12, cet_ampm, "\t", good_time(cet, pst))