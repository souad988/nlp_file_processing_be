<a name="readme-top"></a>

<h3><b>NLP FILE PROCESSING Backend</b></h3>

![Screenshot from 2024-06-02 00-44-25](https://github.com/souad988/nlp_file_processing/assets/59707859/7e9f8940-6e91-4fbe-b4b7-8e7e43b738ff)
![Screenshot from 2024-06-02 00-44-10](https://github.com/souad988/nlp_file_processing/assets/59707859/e3085af2-9ac0-4d76-b517-d0756185073e)


</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [NLP FILE PROCESSING] <a name="about-project"></a>

**[NLP FILE PROCESSING]** is a web application that allows users to perform question answering on their PDF files.

## LIVE DEMO

You can also see a video of mine of a demonstration in this link ([(https://www.loom.com/share/2458d25e3ce345249c590ea44cdca778?sid=a2c6fd89-2d29-4b22-bd21-63f46a8ba969)](https://www.loom.com/share/385230aaa50049f596cb41edb0c8fcbb?sid=1c52c8e6-98e8-43e8-b433-5c36904c666c))

<!-- GETTING STARTED -->

### Frontend Link

https://github.com/souad988/nlp_file_processing


## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Backend</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://langchain.com/">LangChain</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
  </ul>
</details>

<!-- Features -->

### Key Features <a name="key-features"></a>

- **[Upload file]**
- **[Question answer]**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

  - Python
  - pip
  - PostgreSQL

### Setup

Clone this repository to your desired folder:  
  cd my-folder  
  git clone git@github.com:souad988/nlp_file_processing_be.git 

Install  
Install this project with:  
  pip install -r requirements.txt  

Add.env file to the root with these variables:  
  DB_USER=<postgres username>  
  DB_PASSWORD=<postgres password>  
  DB_NAME=<nlp_file_processing>   
  DB_HOST=<localhost>  
  OPENAI_KEY=<openai API key>  


### Usage
To run the project, execute the following command:
  -create database and tables : python3 app/db_migrations.py
  -run server: uvicorn main:app --reload


<!-- AUTHORS -->
👥 Authors <a name="authors"></a>
👤 **Author1**

- GitHub: [@githubhandle](https://github.com/souad988)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/souad-el-mansouri/)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->
🔭 Future Features <a name="future-features"></a>

-[Refactore backend code and separate functionalities]
-[Add user authentication]
-[Add multi tabs for old conversations]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
🤝 Contributing <a name="contributing"></a>
Contributions, issues, and feature requests are welcome!

Feel free to check the issues page.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- SUPPORT -->
⭐️ Show your support <a name="support"></a>
If you like this project please show your support by adding a star

<!-- LICENSE -->
📝 License <a name="license"></a>
This project is MIT licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

