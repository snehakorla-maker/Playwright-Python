# Installing Dependencies

This project does not include the virtual environment (`venv`) or installed Python packages because they are ignored by Git.

After cloning the repository to your local system, follow these steps to reinstall all required dependencies.

> **Note:**  
> The example below demonstrates the process for a single sub-folder (`playwright_demo`).  
> If your repository contains multiple Python project sub-folders with their own `requirements.txt` files, these steps must be repeated for each sub-folder.

## 1. Open Terminal

Navigate to the project folder:

```bash
cd playwright_demo
```

## 2. Create a Virtual Environment (Recommended)

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

Run the following command:

```bash
pip install -r requirements.txt
```

## What This Command Does

- Reads all required packages from `requirements.txt`
- Installs the exact dependencies needed for the project
- Recreates the project environment on your local system

## 5. Install Playwright Browsers

After installing dependencies, install Playwright browser binaries:

```bash
playwright install
```

OR:

```bash
python -m playwright install
```

## After Installation

Your Python environment and Playwright dependencies will be ready.

You can then run your tests normally.