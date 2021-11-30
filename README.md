
# parts_demand

## How to dev

### Linux
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
python manage.py test
```

### Windows
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
```

