from website import create_app

app = create_app()

if __name__ == '__main__':
    #run flask application webserver 
    app.run(debug=True)

