# Green Wind

Green Wind is an example of a ETL tool that is able to take in unstructed Battery Data and store it in a Postgres Database! 

Here is an example of some unstructered data that we will be working with:


```json
{
  "battery_id": "B123456789",
  "manufacturer": "GreenPowerTech",
  "model": "GPT-5000",
  "capacity": {
    "current_capacity": "4000 kWh",
    "design_capacity": "5000 kWh",
    "remaining_capacity": "3500 kWh"
  },
  "voltage": {
    "terminal_voltage": "480 V",
    "operating_voltage": "450-500 V",
    "charging_voltage": "460 V"
  },
  "temperature": {
    "internal_temperature": "35°C",
    "external_temperature": "30°C",
    "operating_temperature_range": "20-40°C"
  },
  "current": {
    "charging_current": "100 A",
    "discharging_current": "95 A",
    "operating_current_range": "80-110 A"
  },
  "status": {
    "state_of_charge": "70%",
    "health_status": "Good",
    "operational_status": "Active",
    "faults": [
      {
        "fault_id": "F123",
        "fault_description": "Overtemperature warning",
        "fault_timestamp": "2023-12-21T09:00:00Z"
      },
      {
        "fault_id": "F124",
        "fault_description": "Low voltage alert",
        "fault_timestamp": "2023-12-21T09:00:00Z"
      }
    ]
  },
  "energy_throughput": {
    "total_energy_delivered": "2000 kWh",
    "total_energy_charged": "1800 kWh"
  },
  "maintenance": {
    "last_maintenance_date": "2023-12-20",
    "next_maintenance_due": "2024-06-20",
    "maintenance_actions": [
      {
        "action_id": "M123",
        "action_description": "Replace cooling fan",
        "action_status": "Completed"
      },
      {
        "action_id": "M124",
        "action_description": "Inspect insulation",
        "action_status": "Pending"
      }
    ]
  },
  "environmental_conditions": {
    "ambient_temperature": "28°C",
    "humidity": "60%",
    "altitude": "500 meters",
    "pressure": "1 atm"
  },
  "operational_parameters": {
    "charge_cycles": "150",
    "discharge_cycles": "140",
    "max_continuous_discharge_rate": "120 A",
    "max_continuous_charge_rate": "110 A"
  },
  "timestamp": "2023-12-21T10:00:00Z"
}
```

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



