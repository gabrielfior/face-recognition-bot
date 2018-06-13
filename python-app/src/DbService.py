from typing import List

from tinydb import TinyDB, where


class DbService:
    """
    Class for communication with database.
    """

    def __init__(self, datafile = "data.json"):
        """
        Instantiates DB
        """
        self.db = TinyDB(datafile)
        self.add_recipes()

    def add_recipes(self) -> None:
        """
        Adds recipes to database (for testing purposes)
        :return:
        """
        recipes = [
            {"name": "Fried Rice", "ingredients": ["rice", "onion", "garlic", "carrot", "egg", "peas", "soy sauce"]},
            {"name": "Thai Street Pancakes",
             "ingredients": ["wheat", "green onion", "garlic", "shrimp", "onion", "mushroom", "crab", "soy sauce",
                             "sesame oil", "lemon juice"]}]

        self.db.table('recipes').insert_multiple(recipes)

    def add_documents_to_table(self, tablename : str, documents : List) -> None:

        print("%d documents to be inserted" %(len(documents)))
        self.db.table(tablename).insert_multiple(documents)

    def purge_table(self, tablename):
        self.db.purge_table(tablename)


if __name__ == "__main__":
    a = DbService()