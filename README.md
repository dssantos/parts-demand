
# Parts Demand

## How to run
To run this project you can use one of the following methods:
1. Docker-compose
2. Linux script
3. Windows script

### 1. Docker-compose (copy and paste)
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
docker-compose up --build

```

### 2. Linux script (copy and paste)
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
python -m venv .parts_demand
source .parts_demand/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
cp contrib/.env-sample .env
SECRET_KEY=`python contrib/secret_gen.py`
sed -i "/^SECRET_KEY=/c\SECRET_KEY=$(python contrib/secret_gen.py)" .env
python manage.py migrate
python manage.py runserver

```

### 3. Windows script
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
python -m venv .parts_demand
Set-ExecutionPolicy Unrestricted -Scope Process -force
./.parts_demand/Scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
cp contrib/.env-sample .env
python contrib/secret_gen.py
# Before continue, change SECRET_KEY in .env file
python manage.py migrate
python manage.py test
python manage.py runserver

```
