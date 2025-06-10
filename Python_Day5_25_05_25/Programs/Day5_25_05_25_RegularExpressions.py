# import re
# def is_valid_phone_number(number):
#   pattern = r'^\d{10}$'
#   return re.match(pattern, number)
# mobile_number = input("Enter your Mobile Number: ")
# print(bool(is_valid_phone_number(mobile_number)))

# text = input('Enter a String with your valid e-mail Id: ')
# print('\n'.join(re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)))

# date = input('Enter a String with a date: ')
# match = re.search(r'(\d{2})-(\d{2})-(\d{4})', date) or re.search(r'(\d{2})/(\d{2})/(\d{4})', date)
# if match:
#   day, month, year = match.groups()
#   print(f'Day: {day}, Month: {month}, Year: {year}')

# def detect_choice(response):
#   match = re.search('yes|no', response.lower())
#   return match.group() if match else "No Match"
# choice = input("Enter a String with your choice(Yes or No): ")
# print(detect_choice(choice))

# # text=input('Enter a Text: ')
# # string=input('Enter a String to find: ')
# # pattern=f'({re.escape(string)})*'
# # match_string=re.search(pattern,text)
# # print(match_string.group() if match_string else "No match found")
# # Thats soooo funnyyy, Hahahahaha AND haha

# text=input('Enter a Text: ')
# string=input('Enter a String to find: ')
# pattern=f'({re.escape(string)})+'
# match_string=re.search(pattern,text)
# print(match_string.group() if match_string else "No match found")