from jinja2 import Template

# Define your HTML template
html_template = """
<html>
  <body>
    <h1>Welcome, {{ name }}!</h1>
    <p>This is a test email sent from Python using Jinja2.</p>
    <p>Here is a special offer just for you: <b>{{ offer }}</b></p>
    <p>Visit our website at: <a href="{{ website_url }}">{{ website_name }}</a></p>
  </body>
</html>
"""

# Create a template object
template = Template(html_template)

# Render the HTML with input arguments
html_body = template.render(
    name="John Doe",
    offer="50% off on your next purchase!",
    website_url="https://www.example.com",
    website_name="Our Website"
)
