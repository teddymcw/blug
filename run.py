import os

from flask_blog_root.blog import app

port = int(os.environ.get('POST', 5000))
app.run(host='0.0.0.0', port=port, debug=False)