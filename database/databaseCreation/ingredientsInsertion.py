from database.manager import Manager
from database import settings
import time


def insert_ingredient_to_database():
	"""
  insert ingredient data to database
  """
	# get data from txt file to save receipes data
	with open("../IngEnGoogle.txt", "r") as file:
		# create a new instance of db manager
		manager = Manager(settings.host,
											settings.username,
											settings.passwd,
											settings.database,
											settings.charset,
											settings.auth_plugin)

		manager.connect()
		i = 0
		# searching for the ingredient names and amount in the text file
		for line in file:
			i += 1
			ingredient = line.replace("\n", "")
			if not manager.contain_ingredient(ingredient):
				manager.insert_ingredient("", ingredient, 0)
				time.sleep(0.05)

		print(f"{i} ingredients inserted into database Complete")
		manager.close()


if __name__ == '__main__':
	insert_ingredient_to_database()
