from app import create_app
from app import utils

app = create_app()

if __name__ == "__main__":
    basedata = utils.readJson('./app/config.json')
    app.run(host=basedata["base"]["host"], port=basedata["base"]["port"])
    # manager.run()