from flask import Flask

app = Flask(__name__)

# 🟢 STORIES DATABASE (you will add more here later)
stories = {
    "1": {
        "title": "The Lost Boy",
        "content": "Once upon a time, a boy got lost in the city but found help from a stranger..."
    },
    "2": {
        "title": "Joseph in Egypt",
        "content": "Joseph was sold by his brothers but later became a ruler in Egypt..."
    }
}

# 🟢 HOME PAGE
@app.route("/")
def home():
    return """
    <h1>🔥 Dayo Stories</h1>
    <p>Click a story below:</p>
    <a href="/story/1">The Lost Boy</a><br>
    <a href="/story/2">Joseph in Egypt</a>
    """

# 🟢 AUTO STORY PAGES
@app.route("/story/<id>")
def story(id):
    story = stories.get(id)

    if not story:
        return "<h1>Story not found</h1>"

    return f"""
    <h1>{story['title']}</h1>
    <p>{story['content']}</p>
    <br>
    <a href='/'>⬅ Back Home</a>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
