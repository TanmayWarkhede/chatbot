from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the chatbot model (simple Q&A model)
chatbot = pipeline("question-answering")

# Predefined context for the chatbot with more common questions
context = {
    "admissions": "You can apply for admissions from our official website.",
    "courses": "We offer a variety of courses including Computer Science, Engineering, and Arts.",
    "campus": "Our campus has modern facilities including a library, gym, and study areas.",
    "tuition": "Tuition fees vary by program. Please check our website for detailed fee structures.",
    "scholarships": "We offer several scholarships based on merit and need. Visit our financial aid page for more information.",
    "contact": "You can contact the admissions office at admissions@example.com.",
    "events": "Check our events calendar on the website for upcoming events and activities.",
    "library hours": "The library is open from 8 AM to 10 PM on weekdays and 10 AM to 6 PM on weekends.",
    "student life": "Student life includes various clubs, organizations, and activities to enhance your college experience.",
    "internships": "We have partnerships with many companies that offer internships to our students.",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    answer = get_answer(user_input)
    return jsonify({'answer': answer})

def get_answer(user_input):
    # Search for keywords in user input
    for key in context:
        if key in user_input.lower():
            return context[key]
    return "I'm sorry, I don't have an answer for that."

if __name__ == '__main__':
    app.run(debug=True)
