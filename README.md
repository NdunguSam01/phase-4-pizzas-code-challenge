# Flask Code Challenge - Pizza Restaurants
## Project Description

This project is a Flask and React based application that creates  an interactive web page to display information about pizza restaurants. 

## Project Pre-requisites

To successully run this project, the following software(s) need to be installed in your machine:

1. **Python** - You can download it from their [official site](https://www.python.org/downloads/).
2. **Pipenv** - This is a Python virtual environment management tool that automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile. You can download it from their [official site](https://pypi.org/project/pipenv/).
3. **Node** - This is an open-source, cross-platform JavaScript library and runtime environment. You can download it from [https://nodejs.org/en](https://nodejs.org/en)

## Project Setup Instructions

### Starting the server

In order to start the of this project, create a new directory where you want to store the project files, navigate into it and follow the instructions below:

1. **Cloning**- clone the repository by typing the following command into your terminal:

    ```
    git clone https://github.com/NdunguSam01/phase-4-pizzas-code-challenge
    ```

    Optionally, you can download the zipped file by clicking the green Code button then selecting the "Download ZIP" option.

2. **Installing dependencies** - since this project needs various dependencies to run,  type the following command in your terminal:

    ```
    pipenv install
    ```

    After this operation is completed, run the following command to enter into the virtual environment:

    ```
    pipenv shell
    ```

3. **Create the database** - once you have successfully cloned the project and entered the virtual environment, run the following commands to navigate into the app folder and create an instance of the database since the project's database migrations have already been done

    ```
    cd app
    ```

    ```
    flask db upgrade 
    ```

4. **Seed the database** - to successfully view the results, run the seed file  which will populate the database with data

    ```
    python3 seed.py
    ```

5. **Start the Flask API** - to start the Flask API, run the app.py file

    ```
    python3 app.py
    ```

Once the server runs, it can be accessed via [http://127.0.0.1:5555/](http://127.0.0.1:5555/)

### Starting the front end application

In order to view the results on the front end, follow the instructions below:

1. **Install dependencies** - to install the dependencies needed to run the React application, open a new terminal and enter the following command

    ```
    npm install --prefix client
    ```

2. **Starting the React application** - run the follwoing command to start the application

    ```
    npm start --prefix client
    ```

Once the React application loads, you should be able to see the data loaded from the database via [http://localhost:4000/](http://localhost:4000/).

Follow the links displayed on the page to view the data and perform various actions on the application.

## Author

[Samuel Muigai](https://github.com/NdunguSam01)

## License

MIT License

Copyright &copy; 2024 Samuel Muigai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
