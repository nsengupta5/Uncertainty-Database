import json

# Sample file
amazon_data = "./raw-public/amazon-com.txt"

# Result dictionary
result = {}

fields = ['date', 'title', 'links', 'duration', 'planned', 'causes', 'implications', 'fixes']

with open(amazon_data) as ad:

    for line in ad:

