# UJ-WRP-Machine-Learning-Hub-2022

### Introduction

UJ WRP Machine Learning Hub 2022 is an open source api that enable students to deploy their machine learning models for thier capstone projects. The perpose of this repository is to allow each team to add their saved **ml** model from eaither **Jupiter Notebook** or **Google Colab**.

## Table of contents

- [Installation](#Installation)
- [Usage](#usage)
- [Endpoints](#Endpoints)
- [Authors](#authors)

<!-- ### Project Support Features
* Users can signup and login to their accounts
* Public (non-authenticated) users can access all causes on the platform
* Authenticated users can access all causes as well as create a new cause, edit their created cause and also delete what they've created. -->

### System requirements

To run this project on your machine you need a linux operating system.

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

<!--
| HTTP Verbs | Endpoints               | FormData fields | Action                              |
| ---------- | ----------------------- | --------------- | ----------------------------------- |
| `POST`     | `/api/model/irrigation` |                 | content to be added by team members |
| `POST`     | `/api/model/radiation`  |                 | content to be added by team members | -->

<table>
    <tr>
      <td> HTTP Verbs </td>
      <td> Endpoints </td>
      <td> FormData fields </td>
      <td> Action </td>
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
  Content to be adde...
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
  Content to be adde...
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

  - [Black Developa](https://github.com/blackdevelopa)

<div id="header" align="center">
  <img src="https://media.giphy.com/media/WLk8YgE2N4mB2/giphy.gif" width="100%"/>
</div>
