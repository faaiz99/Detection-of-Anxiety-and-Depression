# Mind Care

Your mental health is our priority

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Prerequisites

- **Python Version 3.10**: Make sure you have Python 3.10 installed on your system.

To get started, ensure you have the necessary prerequisites:

- Upgrade your `pip` to the latest version:
  ```bash
  python -m pip install --upgrade pip
  ```

- Generate a `requirements.txt` file: [NOT REQUIRED IF CLONING]
  ```bash
  pip freeze > requirements.txt
  ```

## Installation

Follow these steps to install the project on your local machine:

1. Create a Python virtual environment:
   ```bash
   py -3 -m venv .venv
   ```

2. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

3. Install project dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project, use the following command:
```bash
uvicorn API:app --reload 
```

## License

This project is licensed under the COMSATS Islamabad Islamabad. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out to faaizaslam75@live.com.

docker build -t test-image.
sudo docker run -p 8000:8000 test-image