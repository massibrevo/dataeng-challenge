<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<h3 align="center">Data Operations Engineer Challenge</h3>

  <p align="center">
    Welcome to the Data Operations Engineer Challenge repository.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#project-structure">Project Structure</a>
    </li>
    <li>
      <a href="#how-to-run">How to Run</a>
    </li>
    <li>
      <a href="#running-the-application">Running the Application</a>
      <ul>
        <li><a href="#first-challenge">First Challenge</a></li>
        <li><a href="#second-challenge">Second Challenge</a></li>
      </ul>
    </li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#running-with-docker">Running with Docker (Optional)</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#additional-information">Additional Information</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project includes a Python tool that parses log files to analyze network connections. It can handle both static log files and streaming log data, providing insights into host connectivity over time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROJECT STRUCTURE -->
## Project Structure

Here's a brief overview of the directory structure and key files included in this project:

- `/app`: The main application directory.
  - `/config`: Configuration files, such as `logging.conf` for logging setup.
  - `/log_parser`: Contains the parsing scripts `parse_data.py` and `unlimited_parse.py`.
  - `main.py`: The entry point script to run the challenges.
- `/data`: Directory containing sample log files.
- `/logs`: Directory where application logs are stored.
- `/tests`: Contains unit tests for the application.
- `Makefile`: Defines a set of tasks to be executed.
- `Dockerfile`: Used to build a Docker container for the application.
- `requirements.txt`: Lists the Python dependencies required for the application.
- `.dockerignore`: Specifies patterns to exclude from Docker builds.
- `.gitignore`: Specifies patterns to exclude from git version control.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW TO RUN -->
## How to Run

To run this tool, follow these steps:

1. Ensure you are in the root directory of this project.
2. Install the necessary Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. To execute the first challenge, run:

    ```sh
    python app/main.py --challenge 1
    ```

   Follow the prompts to input the required parameters.

4. To execute the second challenge (Unlimited Input Parser), run:

    ```sh
    python app/main.py --challenge 2
    ```

   This will start the parser that runs indefinitely and outputs the results once every hour.

## Goals to Achieve

### 1. First Challenge — Parse the Data with a Time Range

The goal is to build a tool that, given a log file and a specified time range, returns a list of hostnames connected to a given host during that period.

### 2. Second Challenge — Unlimited Input Parser (Optional)

This optional challenge extends the first by continuously parsing the log file, even as new data is written, and outputs results every hour, including:

- A list of hostnames connected to a specified host.
- A list of hostnames that received connections from a specified host.
- The hostname that generated the most connections.

### Run Tests 

   ```sh
   python -m unittest tests.test_parse_data
   python -m unittest tests.test_parse_unlimited
   ```

## Extra

This project also includes optional Docker support for containerization, which hasn't been fully tested. To use Docker to build and run the application in a container, follow these additional steps:

1. Ensure Docker is installed on your system.
2. Build the Docker image:

    ```sh
    docker build -t clarity-challenge .
    ```
   
3. Run the application in a Docker container:

    ```sh
    docker run -it clarity-challenge
    ```

Note: The Docker functionality is provided as an extra feature and may require additional configuration and testing to fully integrate with the challenges.
