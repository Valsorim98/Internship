import json
import os

class Tokens():

    def get_database(self):

        dir_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(dir_path, "database.json")
        
        json_content = None
        with open(file_path, 'r') as f:
            content = f.read()
            json_content = json.loads(content)
        
        return json_content
