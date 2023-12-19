# Green Wind

Source:
https://github.com/Duvey314/austin-green-energy-predictor

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── assets             <- Images used in the README.md file
    |
    ├── .devcontainer               <- Folder for the devcontainer configuration files and Dockerfile & Docker Compose files
    │   ├── Dockerfile              <- Dockerfile for the devcontainer
    │   ├── devcontainer.json       <- Devcontainer configuration file
    │   └── docker-compose.yml      <- Docker Compose file for the devcontainer
    │
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in the reports.
    |   └── text           <- The folder for the report text files
    |       ├── paper               <- The folder for the report Latex & Output pdf files
    |       |   ├── paper.pdf       <- The report pdf file
    |       |   └── paper.tex       <- The report LateX file
    |       |
    |       ├── bibliography.bib    <- The bibliography file for the report & presentation
    |       |
    |       └── presenation         <- The folder for the presentation Latex & Output pdf files
    |           ├── slides.pdf      <- The presentation pdf file
    |           └── slides.tex      <- The Beamer presentation LateX file
    │
    ├── app                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes app a Python module
    |   ├── main.py        <- Main application file for FastAPI application
    │   ├── api            <- Configuration file for FastAPI application
    |   |   ├── api_v1
    |   |   |   ├─ deposit_rates.py     <- API endpoints for deposit rates 
    |   |   |   ├─ target_rates.py      <- API endpoints for target rates
    |   |   |   └─ target_ranges.py     <- API endpoints for target ranges
    │   │   └── api.py                  <- API endpoints for the application
    │   │
    │   ├── crud                        <- The CRUD (Create, Read, Update, Delete) operations folder for the application
    │   │   ├── base.py                 <- Base CRUD operations
    |   |   ├── __init__.py             <- Makes crud a Python module
    |   |   ├── crud_deposit_rates.py   <- CRUD operations for deposit rates
    |   |   ├── crud_target_ranges.py   <- CRUD operations for target ranges
    |   |   └── crud_target_rates.py    <- CRUD operations for target rates
    │   │
    │   ├── schema                      <- Folder for the SQLModel models for the application
    │   │   ├── deposit_rate.py         <- SQLModel model for deposit rates
    │   │   ├── target_rate.py          <- SQLModel model for target rates
    |   |   └── target_range.py         <- SQLModel model for target ranges
    │   │
    │   └── utils                                   <- Scripts to import data and create the database
    │       ├── config.py                           <- Configuration file for the application that loads the environment variables
    │       ├─── deps.py                            <- Dependency file for the application that creates the database connection
    │       ├─── import_deposit_rates.py            <- Script to import deposit rates
    │       ├─── import_target_rates.py             <- Script to import target rates
    │       └─── import_target_ranges.py            <- Script to import target ranges
    │   
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    └── env.example        <- Environment variables for the application

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

# Class Materials

<https://github.com/ipozdeev/it-skills-for-research>

# Paper & Presentation Compiling

We used [Latexdevcontainer](https://github.com/qdm12/latexdevcontainer) to compile the paper and presentation.
We simple had to copy accoss the files from the ```reports/``` folder to the [Latexdevcontainer](https://github.com/qdm12/latexdevcontainer) project and it would produce the pdf files on save.


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

![Alt text](assets/dev_containter_popup.png)

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

We can then connect to the Jupyter Notebook: ```notebooks/snb-data-processing.ipynb```  to explore the data with a read only connection to the PostgresDB instance.



