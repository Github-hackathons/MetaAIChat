from flask import Flask, render_template, request, jsonify 
import openai
from ai import ask_openai
from blob_search import ask_openai_blob


app = Flask(__name__) 
messages = []
@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
	if request.method == 'POST': 
		prompt = request.form['prompt'] 
		response = ask_openai(prompt) 

		return jsonify({'response': response}) 

	return render_template('chat.html') 


if __name__ == "__main__": 
	app.run(debug=True) 
