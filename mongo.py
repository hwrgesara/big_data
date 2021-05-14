from pymongo import MongoClient
from pprint import pprint
import requests
import json

# Client connects to "localhost" by default 
client = MongoClient()


# Create local "bipm" database on the fly 
db = client['bipm']

# When we rerun the whole notebook, we start from scratch 
# by dropping the colection "courses"
db.courses.drop()

# Create a Python Dictonary
courses = [
    {'title': 'Data Science',
     'lecturer': {
         'name': 'Markus Locher',
         'department': 'Math',
         'status': 'Professor'
     },
     'semester': 1},
    {'title': 'Data Warehousing',
     'lecturer': {
         'name': 'Roland M. Mueller',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 1},
    {'title': 'Business Process Management',
     'lecturer': {
         'name': 'Frank Habermann',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 1},
    {'title': 'Stratigic Issues of IT',
     'lecturer': {
         'name': 'Sven Pohland',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 1},
    {'title': 'Text, Web and Social Media Analytics Lab',
     'lecturer': {
         'name': 'Markus Locher',
         'department': 'Math',
         'status': 'Professor'
     },
     'semester': 2},
    {'title': 'Enterprise Architectures for Big Data',
     'lecturer': {
         'name': 'Roland M. Mueller',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 2},
    {'title': 'Business Process Integration Lab',
     'lecturer': {
         'name': 'Frank Habermann',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 2},
    {'title': 'IT-Security and Privacy',
     'lecturer': {
         'name': 'Dennis Uckel',
         'department': 'Information Systems',
         'status': 'External'
     },
     'semester': 2},
    {'title': 'Research Methods',
     'lecturer': {
         'name': 'Marcus Birkenkrahe',
         'department': 'Information Systems',
         'status': 'Professor'
     },
     'semester': 2},
]

#pprint(courses)

db.courses.insert_many(courses)

# TODO: Print all courses
cursor = db.courses.find()
for document in cursor:
    pprint(document)

my_json = '{"title": "Master Thesis", "semester": 3}'
another_course = json.loads(my_json)
another_course

# TODO: Store `another_course` as another course:
db.courses.insert_one(another_course)

# TODO: Print all courses
cursor = db.courses.find()
for course in cursor:
    pprint(course)

# TODO: Find the course with the title "Data Science" 
# save the result in a varibale result
# and pprint the result.
result = db.courses.find_one({"title": "Data Science"})
pprint(result)

print(result["_id"])
print(result["lecturer"]["name"])

# TODO: Find the first course (one course) in the second semester
# and print it
result = db.courses.find_one({"semester": 2})
pprint(result)

# TODO: Find all courses in the second semester
# and print the course titles
result = db.courses.find({"semester": 2})
for course in result:
    pprint(course["title"])

# TODO: Find all courses in the second semester
# and print the lecturers names
result = db.courses.find({"semester": 2})
for course in result:
    pprint(course["lecturer"]["name"])

# TODO: Find all courses of Frank Habermann
# and print the title and the semester
result = db.courses.find({"lecturer.name": 'Frank Habermann'})
for course in result:
    pprint(course["title"] + " " + str(course["semester"]))

# TODO: Find all courses from Frank Habermann in the second semester
# and print the title and the semester
result = db.courses.find({"lecturer.name": 'Frank Habermann', "semester": 2})
for course in result:
    pprint(course["title"] + " " + str(course["semester"]))

# TODO: Find all courses from Frank Habermann or Markus Locher
# and print the title and the semester
result = db.courses.find({"$or": [{"lecturer.name": "Frank Habermann"}, {"lecturer.name": "Markus Locher"}]})
for course in result:
    pprint(course["title"] + " " + str(course["semester"]))

# TODO: Find all courses in semester greater than 1
# and print the title and the semester
result = db.courses.find({"semester": {"$gt": 1}})
for course in result:
    pprint(course["title"] + " " + str(course["semester"]))

# TODO: How many courses are in the second semester?
result = db.courses.count_documents({"semester": 2})
print(result)

# Create local "nobel" database on the fly 
db = client["nobel"]
db.prizes.drop()
db.laureates.drop()
# API documented at https://nobelprize.readme.io/docs/prize 
for collection_name in ["prizes", "laureates"]:
    singular = collection_name[:-1] # the API uses singular
    response = requests.get( "http://api.nobelprize.org/v1/{}.json".format(singular)) 
    documents = response.json()[collection_name] 
    # Create collections on the fly 
    db[collection_name].insert_many(documents)

pprint(db.laureates.find_one())

# TODO: Print the first name of the first document
pprint(db.laureates.find_one()['firstname'])

# How many female laureates exists?
result = db.laureates.count_documents({"gender": 'female'})
print(result)

db.laureates.distinct("bornCountry", {"bornCountry": {"$regex": "Germany"}})

# TODO: How many laureates are from Germany?
result = db.laureates.count_documents({"bornCountry": {"$regex": "Germany"}})
print(result)

# TODO: Find all physics nobel laureates that are from Germany
# print the year of the first prize, the first name, and surename
results_nobel = db.laureates.find({"bornCountry": {"$regex": "Germany"}, "prizes.category": "physics"})
for laureate in results_nobel:
    pprint(str(dict(laureate["prizes"][0])["year"]) + " " + laureate["firstname"] + " " + laureate["surname"])

# TODO: find and print the document for "Malala" (firstname)
db.laureates.find_one({"firstname": "Malala"})

# TODO: Find only female nobel laureates 
# and sort them according the the prize year in ascending order
# print year of the first prize, firstname, and surename
result = db.laureates.find({"gender": 'female'}).sort([("prizes.year", 1)])
for laureate in result:
    pprint(str(dict(laureate["prizes"][0])["year"]) + " " + laureate["firstname"] + " " + laureate.get("surname", ""))