name: Python Package

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    # 1. Checkout the repository content
    - name: Checkout repository
      uses: actions/checkout@v4

    # 2. Set up a specific Python version
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    # 3. Install dependencies from requirements.txt
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    # 4. Run the test suite (using pytest)
    - name: Run tests
      run: |
        pytest
