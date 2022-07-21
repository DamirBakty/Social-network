# Social-network
Backend of Social-network,Analogue of VK.

# Main tools
DRF, Sqlite, Redis, React for front

# Installation of libraries
pip install -r requirements.txt
# Migration to database
python3 manage.py migrate
# Running Redis server
sudo docker run -p 6379:6379 -d redis:6.0
# Running server
python3 manage.py runserver
