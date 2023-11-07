import re
import os
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

problems_data = dict()
unknown_problems = set()

file_path = os.path.join(os.path.dirname(__file__), 'problems.json')

with open(file_path, "r") as json_file:
    problems_data = json.load(json_file)



@app.route('/', methods=['GET'])
def hello():
    return "Welcome to codechef-stats-api, For documentation visit:https://www.github.com/iamhariharanvj/geeksforgeeks-api"
@app.route('/get/<username>', methods=['GET'])
def get_geeksforgeeks_data(username):

    url = f"https://www.codechef.com/users/{username}"

    page = requests.get(url)

    if page.status_code != 200:
        return jsonify({"error": "User doesn't exist"})

    soup = BeautifulSoup(page.text, 'html.parser')


    data = dict()
    data["username"] = username

    problem_solved_section = soup.find('section', class_="rating-data-section problems-solved")

    if(problem_solved_section is None):
        return jsonify({"error": "User doesn't exist"})
        

    no_solved = problem_solved_section.find_all('h3')


    data["total_problems_solved"] = int(re.findall(r'\d+', no_solved[0].text)[0])
    data["problems"] = {}
    for tag in ["school", "easy", "medium", "hard"]:
        data["problems"][tag] = {"count": 0, "problems": []}

    problem_links = problem_solved_section.find('p').find_all('a')


    for link in problem_links:
        problem_code = link["href"].split("/")[-1]

        if problem_code in problems_data.keys():            

            problem = problems_data[problem_code]

            data["problems"][problem["level"]]["count"] += 1
            data["problems"][problem["level"]]["problems"].append({
                "question": problem["name"],
                "link": "https://www.codechef.com/problems/" + problem_code,
                "submissions": problem["submissions"],
                "difficulty_rating": problem["difficulty"],
                "contest_code": problem["contestcode"],
            })

        else:
            unknown_problems.add(problem_code)

    return jsonify(data)


@app.route('/problems/unknown')
def unknown():
    return jsonify(list(unknown_problems))

if __name__ == '__main__':

    app.run(debug=True)
