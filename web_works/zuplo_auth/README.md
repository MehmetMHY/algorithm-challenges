# Implmentation Of API Key Auth (Similar To OpenAI's Solution)

## About

This is a simple implmentation of API key auth based on of [Zuplo's Video](https://www.youtube.com/watch?v=ooyOmiczY1g). It was originally written in TypeScript back in Fall 2023 but as of March 2024 has been converted to Python.

## How To Run

1. Setup python3 environment and activate it

   ```
   python3 -m venv env

   source env/bin/activate
   ```

2. Run Postgres database, using Docker

   ```
   docker run --name "pgDB-$(date +%s)" -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
   ```

3. Install python deps:

   ```
   pip3 install -r requirements.txt
   ```

4. Run the API

   ```
   python3 main.py
   ```

5. Make requests by reviewing the code and usinga tool like [Postman](https://www.postman.com/)
