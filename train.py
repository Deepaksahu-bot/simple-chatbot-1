from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def train(serra):
	path = 'data\\english\\'
	for file in os.listdir(path):               #changing the name of bot to serra and also changed my_bot to my_serra
		data = open(path + file, 'r').readlines()
		serra.train(data)

def main():
	serra = ChatBot('My_serra')
	serra.set_trainer(ListTrainer)
	train(serra)


if __name__ == '__main__':
	main()

