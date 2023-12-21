# Green Wind

Green Wind is an example of a ETL tool that is able to take in data and store it in a Postgres Database! 

The source of the Data and Data Science code is from here:
https://github.com/Duvey314/austin-green-energy-predictor



# Set Up Instructions

### Option 1: Github Codespaces (devcontainer) - Automatic Dev Environment

To get started, create a codespace for this repository by clicking this 👇

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=708763302)

A selection menu will open allowing you to create a Codespace. After create a Codespace it  will open in a web-based version of Visual Studio Code. The [dev container](.devcontainer/devcontainer.json) is fully configured with software needed for this project along with added development vscode extensions such as [Jupyter Notebook](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), Python, and Docker.

It should Automatically build the application and install the ```requirements.txt``` file. if not run the following command in the terminal:

```bash
pip install -r requirements.txt
```

### Option 2: Local Machine

This repository can be [used locally](https://code.visualstudio.com/docs/devcontainers/tutorial) on a system running Visual Studio Code and Docker, or in a remote cloud based [Codespaces](https://github.com/features/codespaces) environment as shown in Option 1.

1. Ensure you have Docker installed on your local machine, if not follow the instructions here: <https://docs.docker.com/get-docker/>

2. Clone the repository to your local machine
   ```git clone https://github.com/Butch78/Bank-Size-Central-Bank-Sensitivity.git```

3. After you open the root project in Vscode, the following pop-up should appear. Click "Reopen in Container"

If not click the button in the bottom left corner and then select "Reopen in Container" or type into the command prompt at the top an enter the following command ```>Reopen in container```

This will build the Docker container and should install the requirements.txt file 
Automatically build the application and install the ```requirements.txt``` file along with creating a PostgresDB instance. if not run the following command in the terminal:

```bash
pip install -r requirements.txt
```

# Start Application Command

rename the ```.env.example``` in the root directory to ```.env```

Then the following command will load the Data into the PostgresDB and start a FastAPI application on port 8000, You can view the API documentation at <http://localhost:8000/docs>

```bash
uvicorn app.main:app --reload
```

Once the application has started The csv files from ```/data/raw```  will automatically be loaded into the PostgresDB instance. 

We can then connect to the Jupyter Notebook: ```notebooks/cell_processing.ipynb.ipynb```  to explore the data with a read only connection to the PostgresDB instance.



