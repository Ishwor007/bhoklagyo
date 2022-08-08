# Project Bhoklagyo

## Setup
Install postgresql from <a href="https://www.postgresql.org/">Postgresql website</a>

### For windows
Search `psql` in start menu and open shell

### For Mac/Linux
Start postgresql shell
> sudo -u postgresql psql

### Setup database
Create user
   >CREATE USER 'seetal' WITH PASSWORD 'postgres';

Create database
   >CREATE DATABASE 'bhoklagyo' SET PASSWORD 'postgres' OWNER seetal;


## Activate virtual environment
Windows

> source bhenv/Scripts/activate

Mac/Linux
>bhenv\Scripts\activate


## Install requirements (python>=3.8)
Use `python3` for linux/mac and `python` for Windows
> python -m pip install -r requirement.txt

Since `psycopg2` is not supported in linux install binary
> python3 -m pip install psycopg2-binary

## Run project
> python manage.py runserver `port`(optional)

 