from app import create_app

# Tworzymy instancję aplikacji Flask
app = create_app()

if __name__ == "__main__":
    # Uruchamiamy serwer developerski Flaska
    app.run()
