# processing-1-billion-rows

## Usage

1. Create a virtual environment and activate it
```
python -m venv .env
source .env/bin/activate
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run script to create 1 billion rows file. It takes ~= 10 min.
```
python create_measurements.py
```

4. Run etl
```
python etl.py
```
