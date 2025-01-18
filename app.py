from task_lister import app 
import os

if __name__ == "__main__":
    app.run(debug=os.environ.get('TASK_LISTER_DEBUG'))