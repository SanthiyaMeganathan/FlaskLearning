Here is a **clean, well-structured README version** of your notes. I corrected grammar, organized sections, and wrote it in **simple, easy-to-understand language**, which is suitable for a GitHub README.

---

# Flask Basics Guide

This document explains some important Flask concepts such as routing, URL variables, query parameters, template rendering, loops, conditions, template inheritance, filters, and macros.

---

# 1. Flask Routes

In Flask, routes are used to map a URL to a Python function.

```python
@app.route('/')
def home_page():
    return render_template('home.html')
```

⚠️ If multiple functions use the **same route**, Flask will use the **first one defined**, and the others will be ignored.

---

# 2. URL Variables

Flask allows us to pass variables directly through the URL.

Example:

```python
@app.route('/contact/<int:age>/<string:name>')
def contact(age, name):
    return f"Name: {name}, Age: {age}"
```

Here:

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

Query parameters are values sent in the URL using **key-value pairs**.

Example URL:

```
?name=kishore&age=25
```

To access query parameters in Flask:

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
* `.get()` retrieves the value of a key

---

# 4. Passing Data from Backend to HTML

We can send data from Flask (backend) to HTML templates using `render_template()`.

Example:

```python
@app.route('/')
def home_page():
    return render_template('home.html', language="Python")
```

In HTML, we access the variable using **double curly braces**:

```html
<h2>{{ language }}</h2>
```

Flask can pass many data types:

* String
* Number
* List
* Dictionary

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
However, Flask uses **Jinja2 templating**, which allows loops and conditions.

Example:

```html
<ul>
{% for num in numbers %}
    <li>{{ num }}</li>
{% endfor %}
</ul>
```

This will display all numbers in the list.

---

# 6. Conditional Statements in Templates

Jinja2 also supports conditions like `if`, `elif`, and `else`.

Example:

```html
{% if language == "Python" %}
    <h2>Python Selected</h2>

{% elif language == "Java" %}
    <h2>Java Selected</h2>

{% else %}
    <h2>Other Language</h2>
{% endif %}
```

This allows us to display different content based on conditions.

---

# 7. Template Inheritance

Template inheritance helps avoid repeating common code such as:

* Navbar
* Footer
* Header

Example: Amazon has the same navbar on every page.

### Base Template

Create a **base file** called `base.html`.

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

---

### Extending the Base Template

In other pages:

```html
{% extends "base.html" %}

{% block content %}

<h1>Welcome to Home Page</h1>

{% endblock %}
```

Now all pages automatically include the **navbar and base layout**.

---

# 8. Include Templates

Sometimes we want to reuse a small section (like a component).

Instead of putting it in the base template, we can use **include**.

Example:

```html
{% include "header.html" %}
```

This will insert the contents of `header.html`.

---

# 9. Template Filters

Filters modify how data is displayed in HTML.

Important:
Filters **do not change the original data**, they only change the display.

Example:

```html
{{ name | upper }}
```

This converts the text to uppercase.

General syntax:

```html
{{ variable | filtername }}
```

---

# 10. Custom Filters

We can also create our own filters in `app.py`.

Example:

```python
@app.template_filter('reverse')
def reverse_string(s):
    return s[::-1]
```

Using the filter in HTML:

```html
{{ name | reverse }}
```

---

# 11. Macros (Reusable HTML Functions)

Macros allow us to create **reusable HTML components**, similar to functions in programming.

Example Macro:

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

This helps avoid repeating the same HTML code.

Macros can also accept parameters, making them **dynamic and reusable**.

---

# Summary

This guide covered the following Flask concepts:

* Flask Routes
* URL Variables
* Query Parameters
* Passing Data to Templates
* Jinja2 Loops
* Conditional Statements
* Template Inheritance
* Include Templates
* Template Filters
* Custom Filters
* Macros

These features help build **dynamic and reusable web applications using Flask**.

