
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length=0
    ans=0
    for i in range(len(s)):
        if s[i::-1]==s[0:i+1]:
            j=0
            if i-j+1>length:
                length=i-j+1
                ans=s[j:i+1]
        for j in range(1, i+1):
            if s[i:j-1:-1]==s[j:i+1]:
                if i-j+1>length:
                    length=i-j+1
                    ans=s[j:i+1]
    return ans

s=input()
print(longestPalindrome(s))
