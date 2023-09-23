#!/usr/bin/env python
# coding: utf-8

# Ans 1 : Flask is a micro web framework written in Python³. It is classified as a microframework because it does not require particular tools or libraries³. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions³. It's a Python module that lets you develop web applications easily¹. It has a small and easy-to-extend core¹.
# 
# The advantages of using the Flask framework are⁶⁷²⁸:
# 
# 1. **Lightweight**: Flask is considered the best framework for light web application serving. It's a lightweight framework and can also be useful to the developer if he or she chooses a web interface to the default system based UI.
# 2. **Easy to Understand**: The Flask framework is easy to understand, which is why it's best for beginners. Its simplicity gives you the opportunity to understand it better and learn from it⁶.
# 3. **Flexibility**: Flask lets you be in total control in web development, taking full creative control of the application and web development.
# 4. **Template Engine**: Flask comes with a template engine that lets you use the same user interface for multiple pages.
# 5. **Testing**: Using Flask for web development allows for unit testing through its integrated support, built-in development server, fast debugger, and restful request dispatching.
# 6. **Scalable**: Due to its status as a microframework, Flask can be used to quickly grow technological projects like web apps.
# 7. **Negotiation is Simple**: To paraphrase one of the Zen of Python lines, "Simple is better than complex" - this applies perfectly to Flask.
# 8. **Support for Unit Testing**: Flask has built-in support for unit testing.
# 9. **Secure Cookies Support**: Flask supports secure cookies (client-side sessions).
# 10. **Templating using Jinja2**: Flask uses Jinja2 for templating.
# 11. **Request Dispatching using REST**: Flask supports RESTful request dispatching.
# 
# These advantages make Flask an excellent choice for developing web applications.

# In[1]:


#Ans 2 : 
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"



# In[ ]:





# ![image.png](attachment:image.png)

# Ans 3 : App routing in Flask is a technique used to map specific URLs to associated functions that handle the logic for those URLs. For example, in a Flask application, the URL ("/") is associated with the root URL¹. If you want to add routing to "www.example.org/hello", you would use "/hello" in your Flask application¹. To bind a function to a URL path, you use the `app.route` decorator. 
# 
# We use app routes for several reasons:
# - **Meaningful URLs**: Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler.
# - **Direct Access**: It allows users to access the desired page directly without having to navigate from the home page.
# - **Function Mapping**: It maps specific URLs with associated functions that are intended to perform some task.
# - **Avoiding Duplicate Route Names**: Using app routes can help avoid duplicate route names and thus prevent typo errors.
# 
# In essence, app routing plays a crucial role in providing a structured and efficient way of defining the paths and responses within your web application.
# 
# 

# Ans 4: 

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Company Details</h1>
    <p>Company Name: ABC Corporation</p>
    <p>Location: India</p>
    <p>Contact Detail: 999-999-9999</p>
    """

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to ABC Corporation</h1>"

if __name__ == '__main__':
    app.run()


# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)
# 

# Ans 5 : In Flask, the url_for() function is used for URL building. It accepts the name of the function as the first argument, and one or more keyword arguments, each corresponding to the variable part of the URL rule. The function returns a URL that can be used to invoke the function.

# In[ ]:


from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the home page."

@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation!"

@app.route('/user/<username>')
def profile(username):
    return f"Welcome {username}!"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('welcome'))
    print(url_for('profile', username='John'))

if __name__ == '__main__':
    app.run()


# In[ ]:




