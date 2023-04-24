from main import create_app
from famapi.settings.extensions import mail
from famapi.settings.database import Base, engine
import os
from flask import redirect
import os


app = create_app()
mail.init_app(app)


@app.route('/')
def home():
    return redirect('/ui')


# app.add_url_rule('/', 'home', home)

Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT", default=8000), debug=True)
