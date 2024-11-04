import os
import django
from pymongo.collection import ObjectId

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors.settings")
django.setup()

from authorsapp.models import Author, Quote
from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://krutsvitya:vitya091003@krutsvitya.plhxk.mongodb.net/?retryWrites=true&w"
                           "=majority&appName=krutsvitya")
mongo_db = mongo_client["test"]
mongo_collection_authors = mongo_db["author"]
mongo_collection_quotes = mongo_db["quote"]

author_mapping = {}

for mongo_author in mongo_collection_authors.find():
    author = Author(
        fullname=mongo_author.get("fullname"),
        born_date=mongo_author.get("born_date"),
        born_location=mongo_author.get("born_location"),
        description=mongo_author.get("description")
    )
    author.save()
    author_mapping[mongo_author.get("fullname")] = author
    print(f"Author {author.fullname} migrated to PostgreSQL.")

for mongo_quote in mongo_collection_quotes.find():
    author_id = mongo_quote.get('author')

    author_data = mongo_collection_authors.find_one({"_id": ObjectId(author_id)})

    if author_data:
        author_fullname = author_data.get('fullname')
        author = author_mapping.get(author_fullname)

        if author:
            quote_text = mongo_quote.get('quote', '')[:255]
            quote = Quote(
                tags=mongo_quote.get('tags'),
                author=author,
                quote=quote_text
            )
            quote.save()
            print(f"Author {quote.quote} migrated to PostgreSQL.")

mongo_client.close()
