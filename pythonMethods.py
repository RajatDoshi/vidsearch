from nltk.corpus import wordnet
import string 

#Input will be two sentences (tokenized in function)
#Output is the number of matching words in the two sentence 
def num_words_matching(first_List,second_List):
	table = str.maketrans({key: None for key in string.punctuation})
	first_List = first_List.translate(table)
	first_List = first_List = first_List.strip().split(' ')
	print(first_List)
	second_List = second_List.translate(table)
	second_List = second_List.strip().split(' ')
	print(second_List)
	count = 0
	indexCount = 0
	for i in first_List:
		i = i.lower()
		first_List[indexCount] = i
		indexCount+=1
	indexCount = 0
	for j in second_List:
		j = j.lower()
		second_List[indexCount] = j
		indexCount+=1
	for i in first_List:
		for j in second_List:
			if(i == j):
				count = count + 1
	print(count)
	return count 

#Input is two common names for a word
#Output is the similarity score
def similarityScore(wordOne, wordTwo):
	synOne = wordnet.synsets(wordOne)
	synTwo = wordnet.synsets(wordTwo)
	score = 0
	scoreList = []
	for indexOne in range (0, len(synOne)):
		for indexTwo in range (0, len(synTwo)):
			score = synOne[indexOne].wup_similarity(synTwo[indexTwo])
			if score is not None:
				scoreList.append(score)
	sum = 0
	for num in scoreList:
		sum = sum + num
	average = sum / (len(scoreList))
	print(average)
	return average

#Example Calls
similarityScore("chair", "man")
num_words_matching("This is a - wait for it - example sentence!", "Example Sentence")