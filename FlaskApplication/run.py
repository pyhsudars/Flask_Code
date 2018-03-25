from .factory import createApp

if __name__ == "__main__":
    app=createApp()
    print(app)
    app.run(port=9000, debug=True)
