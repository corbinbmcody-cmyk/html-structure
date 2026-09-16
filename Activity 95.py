rom flask import Flask, render_template

app = Flask(__name__)

# Sample wildlife data
WILDLIFE_DATA = [
    {
        "name": "Philippine Eagle",
        "status": "Critically Endangered",
        "habitat": "Tropical forests",
        "description": "One of the world's largest and most powerful eagles, endemic to Philippine forests."
    },
    {
        "name": "Tamaraw",
        "status": "Critically Endangered",
        "habitat": "Grasslands and forests",
        "description": "A small, rare dwarf buffalo native to the island of Mindoro in the Philippines."
    },
    {
        "name": "Palawan Peacock-Pheasant",
        "status": "Vulnerable",
        "habitat": "Forests",
        "description": "A brilliant, iridescent bird found exclusively on the island of Palawan."
    }
]

@app.route('/')
def home():
    return render_template('index.html', animals=WILDLIFE_DATA)

if __name__ == '__main__':
    app.run(debug=True)