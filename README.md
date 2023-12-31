# Microgrid simulation with ScadaBR and Modbus TCP

This project aims to provide the necessary files for simulating a complete microgrid industrial environment, including a SCADA server (SCADABR), a microgrid simulation with Simulink, and a Modbus server. This project was carried out as part of the INF6103 "Cybersecurity of critical infrastructure" course given at Polytechnique Montréal.

## Project Contents

The project is organized as follows:

- **/scadabr**: Contains the files necessary to configure and run the SCADA server (SCADABR). Refer to the README inside this directory for detailed instructions on configuration.

- **/simulink**: Includes Simulink files needed to simulate a microgrid. Explore the directory to find examples of configurations and usage. You have to open this repository inside your matlab. Execute the simulation directly with the tcp_client.m script.

- **/modbus-server**: Contains files to set up a Modbus server. The README in this directory will guide you through the configuration and execution.

### Virtual Machines Setup

For a complete simulation environment, you will need three different virtual machines:

1. **SCADABR Server VM:** Set up a virtual machine to host the SCADABR server. Follow the instructions in `/scadabr` for configuration details.

2. **Modbus Server VM:** Create another virtual machine dedicated to the Modbus server. Refer to the documentation in `/modbus-server` for setup instructions.

3. **Host Machine for Simulink:** Simulink, used for microgrid simulation, will be executed directly on your host machine. Ensure Matlab/Simulink is installed on your host machine.

## Usage Instructions

1. Clone this repository to your local machine.

```bash
git clone https://github.com/abonnivard/Microgrid-simulation-for-security-test.git
cd Microgrid-simulation-for-security-test
