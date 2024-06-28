from flask import Flask , render_template
from utils import *


app = Flask(__name__)

@app.route("/")
@app.route("/<page>")
def Wiki_Index(page=None):
    if page:
        page_data = get_page(page)
        if not page_data:
            return "<H1>ERROR NO FILE FOUND</H1>"

        return render_template('page.html', page=page, data= page_data)
    
    pages = list_pages()
    return render_template('index.html', pages= pages)




if __name__ == "__main__":
    app.run(debug=True)
