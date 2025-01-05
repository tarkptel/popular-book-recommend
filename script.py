from wsgiref.util import request_uri

from flask import  Flask,  render_template, request
import pickle
import numpy as np


popular_books = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_s = pickle.load(open('similarity_s.pkl','rb'))
book = pickle.load(open('book.pkl','rb'))



app = Flask(__name__, template_folder="Tamplates")

@app.route('/')
def index():
    return render_template("ts.html",
                           book_name = list(popular_books['Book-Title'].values),
                           author = list(popular_books['Book-Author'].values),
                           image = list(popular_books['Image-URL-M'].values),
                           rating_count = list(popular_books['rating_counts'].values),
                           rating = list(popular_books['rating_counts_mean'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    return render_template("recommend.html")

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    index = np.where(pt.index == user_input)[0][0]
    sim_b = sorted(list(enumerate(similarity_s[index])), key=lambda x: x[1], reverse=True)[1:7]

    data = []
    for i in sim_b:
        item = []
        temp = book[book['Book-Title'] == pt.index[i[0]]]

        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    print(data)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)