# python-fastapi-api

This small piece of API contains all basic features that API's must have. App is created in [FastAPI](https://github.com/tiangolo/fastapi) Python framework. Database (PostgreSQL in our case) connection handled using [SQL Alchemy](https://github.com/sqlalchemy/sqlalchemy). [Pydantic](https://github.com/samuelcolvin/pydantic/) used for data parsing and validation.

## Installation

1) Clone the repository to your development environment:

```bash
git clone https://github.com/perviz3003/python-fastapi-api.git
```

2) `cd` into that folder and create **virtual environment**:

```
cd python-fastapi-api
python3 -m venv venv
```

3) Activate environment and install all required packages from *Requirements.txt* file using the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
source env/bin/activate
pip install -r Requirements.txt
```

## Usage

If you have installed all required packages successfully, you should simply execute below command in terminal:

```bash
uvicorn api.main:app --reload
```

Now you can access your api from web browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

FastAPI provides two beautiful API interface which generate API Docs automatically:

* Swagger UI - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc - [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
