import webbrowser


def generate_html(reviews):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Translated Product Reviews</title>
        <style>
            /* CSS code here */
            {css}
        </style>
    </head>
    <body>
        <h1>Translated Product Reviews</h1>

        <div id="reviews">
            <!-- Product reviews will be displayed here -->
            {reviews}
        </div>

        <script>
            // JavaScript code here
        </script>
    </body>
    </html>
    """
    return html_template.format(css=generate_css(), reviews=generate_review_elements(reviews))


def generate_css():
    css_template = """
    /* Reset default margin and padding */
    body, h1, div {{
        margin: 0;
        padding: 0;
    }}

    /* Center align heading */
    h1 {{
        text-align: center;
        margin-top: 20px;
    }}

    /* Container for reviews */
    #reviews {{
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }}

    /* Individual review styling */
    #reviews div {{
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }}
    """
    return css_template


def generate_review_elements(reviews):
    review_elements = ""
    for review in reviews:
        review_elements += "<div>" + review + "</div>"
    return review_elements


def main():
    # Sample product reviews
    sample_reviews = [
        "Great product! Very satisfied.",
        "Good value for money.",
        "Disappointed with the quality.",
        "Excellent service from the seller.",
        "Highly recommended!",
    ]

    # Generate HTML code with sample data
    html_code = generate_html(sample_reviews)

    # Write HTML code to a file
    with open("index.html", "w") as html_file:
        html_file.write(html_code)

    # Open the generated HTML file in the default web browser
    webbrowser.open("index.html")


if __name__ == "__main__":
    main()
