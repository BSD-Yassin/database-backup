## Database Archive Scheduled Task

This will move any data from n table to archive table

## Installation on bare

```bash
git clone git-repo
cd git-repo
pip install -r requirements.txt
```

## Installation on virtual

```bash
git clone git-repo
cd git-repo
## optional
## you can use a virtualenv if you want to avoid messing with your pip modules
pip install virtualenv
python -m virtualenv db-save

# on Windows
Scripts/activate.ps1 

# on Linux
Scripts/activate
pip install -r requirements.txt
```

## Run manually

To simply run manually, use the main.py 

## Folder structure 

```bash
├── README.md
├── config # Config values for auth and other settings
│   ├── logs.ini
│   └── secrets.ini
├── database-saver ## Virtualenv Used for the project 
├── docker_db ## Small Docker Project for testing purpose
│   ├── docker-compose.yml
│   └── requirements.txt
├── main.py # Actual python script
└── requirements.txt # Pip requirements to install for modules to run
```
