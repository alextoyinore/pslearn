from cProfile import run
from distutils.log import debug
from web import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
