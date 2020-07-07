# Flask Blog Completed

## Set Up

To set up this app you will need to create a virtual environment with Python. Which requires some installs.

```bash
sudo apt install python3 python3-venv python3-pip
```

Then to create the venv and activate it.

```bash
python3 -m venv venv
./venv/bin/activate
```

Then you can install everything the app needs.

```bash
pip3 install -r requirements.txt
```

You will need a Database for this app to work and a connection string to that database e.g.

`mysql+pymysql://username:password@host/database-name`

This will need to be exported as an environment variables.

```bash
export MYSQL_USER=your-username
export MYSQL_PASS=your-password
export MYSQL_URL=your-host
export MYSQL_DB=your-database-name
```

You will also need a secret key to allow the user to post information to the application.

```bash
export SECRET_KEY=your-secret-key
```

Then finally run this to start the app.

```bash
python3 app.py
```

