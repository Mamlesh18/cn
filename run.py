from chatapp import create_app, socketio

app = create_app()

if __name__ == "__main__":
    socketio.run(app, host="54.254.162.138")
