
para =    '''
    On May 30, a seventh-grader from Tampa, Florida, became the 2024 Scripps National Spelling Bee champ. 
    Bruhat Soma, 12, crushed a lightning tiebreaker round by spelling 29 words correctly in 90 seconds. 
    The winning word was abseil. It’s a word used in the sport of mountaineering.
    This was Bruhat’s third appearance in the bee. In 2022, he tied for 163rd place. Last year, he came 74th.
    Bruhat told NPR that he felt “excited” about winning. “I’ve been working really hard, so I just put a lot of time into spelling,” he said. 
    “I’m really happy that I won. Like, I really can’t describe it. I’m still shaking.”
    Bruhat’s spelling coach was 16-year-old speller Sam Evans. Sam coached three of the top four finishers. 
    He told the Associated Press that Bruhat had indeed put in a lot of hard work. 
    “I’m very happy that I could use my experience to help him, but at the end of the day, it’s all about his hard work and his dedication,” Evans said. 
    “I’m so happy for him.”
    Bruhat’s prize includes more than $50,000, reference materials, and a trophy. 
    The trophy was presented to him by Adam Symson, president and CEO of The E.W. Scripps Company. 
    In a press release, Symson said that “Bruhat impressed with his display of knowledge and composure."
    '''

#count letters
letter_count = 0
for letter in para.lower():
    if letter in list("abcdefghijklmnopqrstuvwxyz"):
        letter_count += 1

print(f"There are {letter_count} letters in this text.")


#count numbers
number_count = 0
for number in para.lower():
    if number in list("0123456789"):
        number_count += 1

print(f"There are {number_count} numbers in this text.")


#count words (including characters)
word_count = 0
list_para = para.split()
for word in list_para:
    word_count += 1

print(f"There are {word_count} words in this text.")


