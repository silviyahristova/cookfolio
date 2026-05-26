from app import create_app

app = create_app()

# Run the Flask application for production use,
# with debug mode disabled
if __name__ == '__main__':
    app.run()
