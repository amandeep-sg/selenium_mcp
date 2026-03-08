# rfpn_jobserver

# base framework setup

1. git setuo
  - `git init`
  - `git remote add origin {url}`

2. requirements.txt
  - `pip freeze > requirements.txt`

3. docker
  - create dockerfile
  - create dockerignore
  - create compose.yml
  - `docker build -t rfpn_jobserver .`
  - `docker run -d -p 8000:8000 rfpn_jobserver`
  - `docker-compose up -d`

4. Create virtual environment
  - `python3 -m venv scraper_jobserver`
  - `source scraper_jobserver/bin/activate`