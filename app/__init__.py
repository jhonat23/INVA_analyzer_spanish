from flask import Flask
from flask_bootstrap import Bootstrap
from typing import Dict

def start_app() -> Flask:
    
    app = Flask(__name__)
    
    app_enviroment: Dict[str: str] = {
        'dev': 'config.dev_config',
        'prod': 'config.prod_config'
    }
    
    app.config.from_object(app_enviroment[app.env])
    
    return app

if __name__ == '__main__':
    
    start_app()