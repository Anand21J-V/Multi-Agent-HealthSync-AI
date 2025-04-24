from flask import Flask, request, jsonify, render_template_string
from crew import run_crew

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>HealthSync AI</title></head>
<body style="font-family: sans-serif;">
  <h2>Healthcare AI Chatbot</h2>
  <form method="POST">
    <label>Enter your symptoms:</label><br>
    <textarea name="symptoms" rows="4" cols="50" required></textarea><br><br>
    <input type="submit" value="Diagnose">
  </form>
  {% if result %}
  <h3>AI Recommendations:</h3>
  <pre>{{ result }}</pre>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        result = run_crew(symptoms)
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
