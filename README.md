
# Parts Demand

## 1. Run the project
To run this project you can use one of the following methods:

    * Docker-compose
    * Linux script
    * Windows script

### Docker-compose (copy and paste)
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
docker-compose up --build

```

### Linux script (copy and paste)
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
python -m venv .parts_demand
source .parts_demand/bin/activate
python -m pip install -U pip
pip install -r requirements-dev.txt
cp contrib/.env-sample .env
SECRET_KEY=`python contrib/secret_gen.py`
sed -i "/^SECRET_KEY=/c\SECRET_KEY=$(python contrib/secret_gen.py)" .env
python manage.py migrate
python manage.py runserver

```

### Windows script
```bash
git clone https://github.com/dssantos/parts-demand.git parts_demand
cd parts_demand
python -m venv .parts_demand
Set-ExecutionPolicy Unrestricted -Scope Process -force
./.parts_demand/Scripts/activate
python -m pip install -U pip
pip install -r requirements-dev.txt
cp contrib/.env-sample .env
python contrib/secret_gen.py
# Before continue, change SECRET_KEY in .env file
python manage.py migrate
python manage.py test
python manage.py runserver

```

## 2. Populate database
Run this script to populate with user. address and demands sample data

```bash
cat contrib/sample_data.py | python manage.py shell

```

## 3. Have fun!!
Have fun with the API. Now use the postman collection attached to this repository to test the endponis of this API.
Remember, some operations need authentication, so generate a new token in /api/login/ and update the request header.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/4817709/UVJhCaAr)
