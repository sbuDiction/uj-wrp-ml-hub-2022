# UJ-WRP-Machine-Learning-Hub-2022

### Introduction

UJ WRP Machine Learning Hub 2022 is an open source api that enable students to deploy their machine learning models for thier capstone projects. The perpose of this repository is to allow each team to add their saved **ml** model from eaither **Jupiter Notebook** or **Google Colab**. This api makes it possible for the students to intergrate their **ml** model with their **NodeJs** or **Javascript** web app, they can use **Axios** a Javascript library used to make HTTP requests from node. js or XMLHttpRequests from the browser and it supports the Promise API that is native to JS ES6.

## Reason why this project for this project

> :warning: The prefered operating system to run this project locally is **Linux** and not **Windows**, because **Pickle5** which is used to save and load any **ml** model inside a **Python** invironment does not install on **Windows** 10/11 we were having issues hence we came up with this alternative to help the students deploy their **ml** model.

## Table of contents

- [Installation](#Installation)
- [Usage](#usage)
- [Endpoints](#Endpoints)
- [Authors](#authors)

### System requirements

To run this project on your machine you need a **Linux** operating system.

### Installation

Clone this repository

```bash
  git clone https://github.com/sbuDiction/uj-wrp-ml-hub-2022.git
```

Go to the project directory

```bash
  cd uj-wrp-ml-hub-2022
```

Make the script executable with

```bash
  chmod +x run.sh
```

Start the server

```bash
  ./run.sh
```

### Endpoints

<table>
    <tr>
      <td> HTTP Verbs </td>
      <td> Endpoints </td>
      <td> FormData fields </td>
      <td> Actions </td>
      <td> Groups </td>
    </tr>
  <tr>
      <td> POST </td>
      
  <td>
   
   `/api/model/irrigation`
  </td>

<td>

```json
{
  "soil_moisture": value
}
```

  </td>

  <td>
    Predicts whether to Irrigate or Not irrigate
  </td>
   <td>
  capstone-group-1
  </td>
</tr>

<tr>
      <td> POST </td>
  <td>
   
   `/api/model/radiation`
  </td>

<td>

```json
{
  "first_interval": value,
  "sec_interval": value,
  "third_interval": value
}
```

  </td>
  <td>
  Content to be added...
  </td>
   <td>
  capstone-group-7
  </td>
</tr>
</table>

### Usage

You can post axios data by using `FormData()` like:

```javascript
// This example is using the radiation model demonstration perposes
let bodyFormData = new FormData()
```

And then add the fields to the form you want to send:

```javascript
// This example is using the radiation model demonstration perposes
bodyFormData.append('first_interval', 380)
bodyFormData.append('sec_interval', 378)
bodyFormData.append('third_interval', 379)
```

And then you can use axios `POST` method (You can amend it accordingly)

```javascript
// This example is using the radiation model demonstration perposes
axios({
  method: 'post',
  url: 'uj-wrp-ml-hub-api.herokuapp.com/api/model/radiation',
  data: bodyFormData,
  headers: { 'Content-Type': 'multipart/form-data' }
})
  .then(response => {
    //handle success
    console.log(response.data)
  })
  .catch(response => {
    //handle error
    console.log(response.data)
  })
```

### Technologies Used

- [Flask](https://nodejs.org/) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
- [Gunicorn](https://gunicorn.org/) The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project.
- [scikit-learn](https://scikit-learn.org/stable/) Scikit-learn is a free software machine learning library for the Python programming language.

- [tensorflow-cpu 2.10.0](https://pypi.org/project/tensorflow-cpu/) TensorFlow is an open source software library for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices.

  ### Authors

  - [sbuDiction](https://github.com/sbuDiction)

<div id="header" align="center">
  <img src="https://media.giphy.com/media/WLk8YgE2N4mB2/giphy.gif" width="100%"/>
</div>
