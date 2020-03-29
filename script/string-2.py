# CodingBat Practice - String-2

"""
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""

# Solution
def double_char(str):
    return "".join([x * 2 for x in str])


"""
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

# Solution
def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        count += str[i:i+2] == "hi"
    return count

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

# Solution
def cat_dog(str):
    return str.count("cat") == str.count("dog")

"""
Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

# Solution
def count_code(str):
    x = ["co" + i + "e" for i in str.lower()]
    count = 0
    index = 0
    for i in x:
        if i in str[index:]:
            index = str.find(i)+1
        count += 1
    return count

"""
Given two strings, return True if either of the strings appears at the very end of the
other string, ignoring upper/lower case differences (in other words, the computation
should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

# Solution
def end_other(a, b):
    a1 = a.lower()
    b1 = b.lower()
    if a1.endswith(b1) or b1.endswith(a1):
        return True
    else:
        return False

"""
Return True if the given string contains an appearance of "xyz" where the xyz is not
directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""

# Solution
def xyz_there(str):
    for i in range(len(str)):
        if str[i] != "." and str[i+1:i+4] == "xyz":
            return True
    if str[0:3] == "xyz":
        return True
    else:
        return False