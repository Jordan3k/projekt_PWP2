The application is prepared in two versions.
The first version of the application is run locally
Download the file named PythonProject_local. The application uses the PostgreSQL database, so the application needs a PostgreSQL database to function properly.
The second version of the application is prepared to create a docker image
Download the file named PythonProject_docker.

A web application built with **Flask** and **PostgreSQL**.  
The project can be launched in two ways:
- **PythonProject_Local** (Python + PostgreSQL installed on your machine)
- **UPythonProject_docker** (Docker + Docker Compose)


## Prerequisites

### Local version
- Python **3.10+**
- PostgreSQL **14+**
- `pip` and `venv`

### Docker version
- Docker **24+**
- Docker Compose


Repository structure
projekt_PWP2/
│
├── PythonProject_local/      # local run
│   ├── app/                  # Flask application code
│   ├── requirements.txt      # Python dependencies
│   └── run.py                # main entry point
│
├── PythonProject_docker/     # Docker run
│   ├── Dockerfile            # app image
│   ├── docker-compose.yml    # Compose configuration
│   └── ...
│
└── README.md                 # project instructions












