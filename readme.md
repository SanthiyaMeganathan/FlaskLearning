
# Flask Learning Notes

This repository contains notes and examples for learning **Flask** and **Jinja2 templates**.

It covers important Flask concepts such as:

* Flask Routing
* URL Variables
* Query Parameters
* Passing Data from Backend to HTML
* Loops in Templates
* Conditional Statements
* Template Inheritance
* Include Templates
* Template Filters
* Custom Filters
* Macros (Reusable Template Functions)

These concepts help build **dynamic and reusable web applications using Flask**.

---

# 1. Flask Routes

In Flask, a **route** connects a URL with a Python function.

Example:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')
```

⚠️ Important:

If multiple functions use the **same route**, Flask will use **only the first function defined** for that route.

---

# 2. URL Variables

Flask allows us to pass variables directly through the URL.

Example:

```python
@app.route('/contact/<int:age>/<string:name>')
def contact(age, name):
    return f"Name: {name}, Age: {age}"
```

Explanation:

* `int` → Data type
* `age` → Variable name
* `string` → Data type
* `name` → Variable name

Example URL:

```
/contact/25/kishore
```

---

# 3. Query Parameters

Query parameters are values passed through the URL using **key-value pairs**.

Example URL:

```
?name=kishore&age=25
```

To access query parameters in Flask we use `request.args`.

Example:

```python
from flask import request

@app.route('/user')
def user():
    name = request.args.get('name')
    age = request.args.get('age')

    return f"Name: {name}, Age: {age}"
```

Explanation:

* `request` is imported from Flask
* `request.args` stores query parameters
* `.get()` retrieves the value

Anything sent from the frontend (forms, URL, API requests) is called a **request**.

---

# 4. Passing Data from Backend to HTML

We can send data from Flask to HTML templates using `render_template()`.

Example:

```python
@app.route('/')
def home_page():
    return render_template('home.html', language="Python")
```

Access it in HTML using **double curly braces**:

```html
<h2>{{ language }}</h2>
```

Flask can send many data types to templates:

* Strings
* Numbers
* Lists
* Dictionaries

Example:

```python
@app.route('/')
def home_page():
    return render_template(
        'home.html',
        language="Python",
        projectname="ecommerce",
        numbers=[1,2,3,4,5]
    )
```

---

# 5. Using Loops in Flask Templates

Plain HTML does not support loops.

Flask uses **Jinja2 templating**, which allows loops and conditions.

Example image reference:

```
imsage.png
```

Example loop:

```html
<ul>
{% for num in numbers %}
    <li>{{ num }}</li>
{% endfor %}
</ul>
```

Example backend code:

```python
@app.route('/')
def home_page():
    return render_template(
        'home.html',
        language="python",
        projectname="ecommerce",
        numbers=[1,2,3,4,5]
    )
```

Example screenshot:

```
image-2.png
```

---

# 6. Conditional Statements in Templates

Jinja templates support conditions like `if`, `elif`, and `else`.

Example screenshot:

```
image-3.png
```

Example code:

```html
{% if language == "Python" %}
    <h2>Python Selected</h2>

{% elif language == "Java" %}
    <h2>Java Selected</h2>

{% else %}
    <h2>Other Language</h2>
{% endif %}
```

Example screenshot:

```
image-4.png
```

Example output:

```
image-5.png
```

These conditions help display **different UI elements based on logic**.

---

# 7. Template Inheritance

Template inheritance helps avoid repeating common HTML code such as:

* Navbar
* Header
* Footer

Example: Websites like Amazon use the **same navbar on every page**.

Instead of writing it repeatedly, we create a **base template**.

Example base template screenshot:

```
image-6.png
```

Example base template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>

<nav>
    <h2>My Navbar</h2>
</nav>

{% block content %}
{% endblock %}

</body>
</html>
```

Block example screenshot:

```
image-7.png
```

Another page extending the base template:

```html
{% extends "base.html" %}

{% block content %}

<h1>Welcome to Home Page</h1>

{% endblock %}
```

This makes code:

* Cleaner
* Reusable
* Easier to maintain

---

# 8. Include Templates

Sometimes we want a component to appear **only in some pages**, not every page.

In that case we use **include**.

Example:

```html
{% include "filename.html" %}
```

Example screenshot:

```
image-8.png
```

This helps reuse small HTML components.

---

# 9. Template Filters

Filters modify how data is displayed in templates.

Example screenshot:

```
image-9.png
```

Example usage:

```html
{{ name | upper }}
```

General syntax:

```html
{{ variable | filtername }}
```

Important:

Filters **do not change the original data**, they only change how it is displayed.

---

# 10. Custom Filters

If the required filter is not available, we can create our own filter in `app.py`.

Example custom filter:

```
image-10.png
```

Example code:

```python
@app.template_filter('reverse')
def reverse_string(s):
    return s[::-1]
```

Using the custom filter in HTML:

```html
{{ name | reverse }}
```

Another example screenshot:

```
image-11.png
```

---

# 11. Macros (Reusable HTML Components)

Macros are similar to **functions**, but used inside templates.

They allow us to create **reusable HTML components**.

Example screenshot:

```
image-12.png
```

Example macro:

```html
{% macro display_user(name) %}
    <h3>User: {{ name }}</h3>
{% endmacro %}
```

Using the macro:

```html
{{ display_user("Santhiya") }}
{{ display_user("Kishore") }}
```

Macros help us:

* Avoid repeating HTML
* Write cleaner templates
* Reuse UI components

Macros can also accept parameters and work dynamically.

They can also use **caller blocks** to change content dynamically.

Example idea:

```
macro(name)
```

---

# Summary

This guide demonstrates the following Flask concepts:

* Flask Routing
* URL Variables
* Query Parameters
* Passing Data to Templates
* Jinja2 Loops
* Conditional Rendering
* Template Inheritance
* Include Templates
* Template Filters
* Custom Filters
* Macros

These features help developers build **dynamic and reusable Flask web applications**.


