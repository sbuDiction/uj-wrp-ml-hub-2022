# UJ-WRP-Machine-Learning-Hub-2022

### Introduction

UJ WRP Machine Learning Hub 2022 is an open source api that enable students to..

<!-- ### Project Support Features
* Users can signup and login to their accounts
* Public (non-authenticated) users can access all causes on the platform
* Authenticated users can access all causes as well as create a new cause, edit their created cause and also delete what they've created. -->

### Installation Guide

Clone this repository

```bash
  git clone https://github.com/sbuDiction/uj-wrp-ml-hub-2022.git
```

<!-- * Clone this repository [here](https://github.com/blackdevelopa/ProjectSupport.git).
* The develop branch is the most stable branch at any given time, ensure you're working from it.
* Run npm install to install all dependencies
* You can either work with the default mLab database or use your locally installed MongoDB. Do configure to your choice in the application entry file.
* Create an .env file in your project root folder and add your variables. See .env.sample for assistance. -->

### Usage

Make the script executable with

```bash
  chmod +x run.sh
```

Start the server

```bash
  ./run.sh
```

<!-- * Run npm start:dev to start the application.
* Connect to the API using Postman on port 7066. -->

### API Endpoints

| HTTP Verbs | Endpoints             | Action                |
| ---------- | --------------------- | --------------------- |
| POST       | /api/model/irrigation | To predict irrigation |
| POST       | /api/model/radiation  | To predict radiaion   |

### Technologies Used

- [Flask](https://nodejs.org/) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
- [Gunicorn](https://gunicorn.org/) The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project.
- [scikit-learn](https://scikit-learn.org/stable/) Scikit-learn is a free software machine learning library for the Python programming language.

  <!-- ### Authors
  - [Black Developa](https://github.com/blackdevelopa)

<!-- - ![alt text](https://avatars0.githubusercontent.com/u/29962968?s=400&u=7753a408ed02e51f88a13a5d11014484bc4d80ee&v=4)
  -->
