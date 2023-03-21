import webbrowser

from app import app


if __name__ == "__main__":
    port = 5000
    webbrowser.open(f"http://localhost:{port}")
    app.run("0.0.0.0", port, debug=True)
