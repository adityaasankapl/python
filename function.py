feedback = input("enter your feedback")

print("--------------------------------------".center(100))
print("Feedback Formated Report".center(100).upper())
print("--------------------------------------".center(100))
print
print("original feedback".title())
print(feedback)
print("---------------------------------------")

print("feeback summary".title())
print("totoal count of characters : ".title(),len(feedback))
print("total count of word : ".title(),len(feedback.split()))

space = feedback.count(" ")
print("total count of space : ".title(),space)
print("total count exclamation marks :".title(),(feedback.count("!")))

print("---------------------------------------")
print("uppercase feedback :".title(),feedback.upper())
print("lowercase feedback :".title(),feedback.lower())
print("capitalize feedback :".title(),feedback.capitalize())
print("swapecase feeback :".title(),feedback.swapcase())
print("---------------------------------------")

print("---------------------------------------")
print("profissional feedback :".title(),feedback.capitalize())
print("word list".title(),feedback.split())
print("---------------------------------------")

print("-----------------------------------------".center(100))
print("thank your for your feedback".title().center(100))
print("-----------------------------------------".center(100))