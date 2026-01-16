from flask import Flask, render_template, request
import re
import html

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    regex = ""
    text = ""
    highlighted_text = ""
    error = None

    if request.method == "POST":
        regex = request.form.get("regex")
        text = request.form.get("text")

        try:
            pattern = re.compile(regex)
            result = ""
            last_end = 0

            for match in pattern.finditer(text):
                start, end = match.span()
                if start == end:
                    continue

                result += html.escape(text[last_end:start])
                result += f'<span class="highlight">{html.escape(text[start:end])}</span>'
                last_end = end

            result += html.escape(text[last_end:])
            highlighted_text = result

        except re.error as e:
            error = f"Invalid Regex: {e}"
            highlighted_text = html.escape(text)

    return render_template(
        "index.html",
        regex=regex,
        text=text,
        highlighted_text=highlighted_text,
        error=error
    )

if __name__ == "__main__":
    app.run()
