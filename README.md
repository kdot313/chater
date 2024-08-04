# E-commerce Chatbot

Welcome to the E-commerce Chatbot project! This chatbot is designed to assist users with their online shopping experience by providing product recommendations, answering questions, and assisting with various inquiries related to the ecommerce store.

## Overview

The Ecommerce Chatbot is built using Python and Flask framework. It leverages natural language processing (NLP) techniques to understand user queries and generate appropriate responses. The chatbot integrates with the ecommerce store's product database to provide personalized recommendations and information about available products.

## Features

- Interactive chat interface for users to interact with the chatbot.
- Natural language processing for understanding user queries.
- Product recommendation engine based on user preferences and browsing history.
- Integration with the ecommerce store's product database.
- Ability to handle various user inquiries such as product availability, pricing, shipping information, etc.

## Installation

To set up the Ecommerce Chatbot locally, follow these steps:

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/E-Commerce_ChatBot_Project
```

### Step-2: Navigate to the project directory:
```bash
    cd ecommerce-chatbot
```

### Step 3: Create a conda environment after opening the repository

```bash
    conda create -p env python=3.10 -y
```

```bash
    conda activate env567/
```

### Step 4: Install the requirements
```bash
    pip install -r requirements.txt
```

### Step-5: Set up environment variables:
- Create a .env file in the project directory.
- Define the necessary environment variables such as database connection strings, API keys, etc.
- My .env file is [here](https://drive.google.com/file/d/1HadmVnwU_LLi_XvA9ci9MHFLsq_p3Y3o/view?usp=sharing)
  
### Step-6: Run the Flask application:
```bash
    python app.py
```

## AWS DEPLOYMENT
### Step-1: Push your entire code to github
### Step-2: Login to your AWS account Link
### Step-3: Launch your EC2 Instance
### Step-4: Configure your EC2 Instance
### Step-5: Command for configuring EC2 Instance.
### INFORMATION: sudo apt-get update and sudo apt update are used to update the package index on a Debian-based system like Ubuntu, but they are slightly different in terms of the tools they use and their functionality:
### Step-6: Connect your EC2 Instance and start typing the following commands

### Step-7: This command uses apt-get, the traditional package management tool.
```bash
    sudo apt-get update
```

### Step-8: This command uses apt-get, the traditional package management tool.
```bash
    sudo apt update -y
```

### Step-9: Install required tools.
```bash
    sudo apt install git curl unzip tar make sudo vim wget -y
```

### Step-10: Clone git repository.
```bash
    git clone https://github.com/jatin-12-2002/E-Commerce_ChatBot_Project
```

### Step-11: Create a .env file there.
```bash
    touch .env
```

### Step-12: Open file in VI editor.
```bash
    vi .env
```
### Press insert and Mention env variable then press esc for saving and write :wq for exit.
### cat .env #for checking the value

### Step-13: For installing python and pip here is a command
```bash
    sudo apt install python3-pip
```

### Step-14: install the requirements.txt. The --break-system-packages flag in pip allows to override the externally-managed-environment error and install Python packages system-wide.
```bash
    pip3 install -r requirements.txt

    pip3 install -r  requirements.txt --break-system-packages
```

### The --break-system-packages flag in pip allows to override the externally-managed-environment error and install Python packages system-wide. pip install package_name --break-system-packages


### Step-15: Configure your inbound rule:
1. Go inside the security
2. Click on security group
3. Configure your inbound rule with certain values
4. Port 5000 0.0.0.0/0 for anywhere traffic TCP/IP protocol

### Step-16: Save it and now run your application.
```bash
    python3 app.py
```

### If you encounter any error like code:400 while running "https:{Public_address}:5000" then just run it with 'http' instead of 'https'.


## For more Information you can follow this [document](https://docs.google.com/document/d/1bUonQSpW_T6BZmij80Sa-FbWQszojC6l/edit?usp=sharing&ouid=108540473432270728768&rtpof=true&sd=true) and [video](https://youtu.be/VfG2YV1pCO0?feature=shared).