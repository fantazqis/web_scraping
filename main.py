import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions": [],
    "vote": []
}

# for que in questions:
#   q = que.select_one(."s-link").getText()
#   vote_count =

questions = soup.select(".s-post-summary")

for question in questions:
  que = question.select_one(".s-link").getText()
  vote_count = question.select_one(".s-post-summary--stats-item-number").getText()
  print(f"""pertanyaan : {que}
        vote: {vote_count}""")
  questions_data['questions'].append({
         "question": que,
         "vote_count": vote_count
     })

json_data = json.dumps(questions_data)

with open("sample.json", "w") as outfile:
    outfile.write(json_data)