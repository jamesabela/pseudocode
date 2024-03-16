"""
LENGTH(<identifier>)
Returns the integer value representing the length of string. The identifier should be of data type string.
LCASE(<identifier>)
Returns the string/character with all characters in lower case. The identifier should be of data type string or char.
UCASE(<identifier>)
Returns the string/character with all characters in upper case. The identifier should be of data type string or char.
SUBSTRING(<identifier>, <start>, <length>)
Returns a string of length length starting at position start. The identifier should be of data type string, length and start should be positive and data type integer.
Generally, a start position of 1 is the first character in the string.

Example – string operations
LENGTH("Happy Days") will return 10
LCASE(ꞌWꞌ) will return ꞌwꞌ
UCASE("Happy") will return "HAPPY"
SUBSTRING("Happy Days", 1, 5) will return "Happy"



"""

#OUTPUT LENGTH("Happy Days")
print(len("Happy Days"))

# OUTPUT LCASE(ꞌWꞌ)
print('W'.lower())

# UCASE("Happy")
print("Happy".upper())

# SUBSTRING("Happy Days", 1, 5)
print("Happy Days"[0:5])
