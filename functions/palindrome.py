def check_palindrome(text):
    text = text.lower()
    text=text.replace(" ","")
    if text==text[::-1]:
        return("text is palindrome")
    else:
        return("text is not palindrome")
print(check_palindrome("Кит на море не романтик"))
print(check_palindrome("test"))