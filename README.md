
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kyleliang919/The-Everything-App">
    <img src="logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">The Everything App</h3>

  <p align="center">
    One App to rule them All!
    <br />
    <a href=""><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/kyleliang919/The-Everything-App/issues">Report Bug</a>
    ·
    <a href="https://github.com/kyleliang919/The-Everything-App/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
  <img src="example.png">
</p>


OpenAI just released chatGPT. It can do many amazing things. But it comes with some limitation: it doesn't have access to open internet, hence it only knows what it knows; It knows how to do things but it can't actually do it for you; This explorative project aims to:
* provide an interface to interact with chatGPT programatically
* give chatgpt the ability to interact with the real world (through exisiting or imaginary App APIs, which we will build)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* ChatGPT

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Things you need to use the software and how to install them.
* Python3.7 or above
* Chrome (preferably latest version)

### Installation

Installing and setting up your app.

1. Clone the repo
   ```sh
   git clone https://github.com/kyleliang919/The-Everything-App.git
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Setting up your app credientials in a yaml file, for example
  ```yaml
    openai:
      email: YOUR_EMAIL
      password: YOUR_PASSWORD
    twitter:
      consumer_key: YOUR_CONSUMER_KEY
      consumer_secret: YOUR_CONSUMER_SECRET
      access_token: YOUR_ACCESS_TOKEN
      access_token_secret: YOUR_ACESS_TOKEN_SECRET
      client_id: YOUR_CLIENT_ID
      client_secret: YOUR_CLIENT-SECRET
    gmail:
      sender_email : YOUR_EMAIL
      sender_password : YOUR_PASSWORD
      receiver_email : RECEIVER_EMAIL
      subject : YOUR_SUBJECT
      body : YOUR_EMAIL_BODY
    youtube:
      api_key : YOUR_API_KEY
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Useful examples of how a project can be used. Link to more resources, Additional screenshots, code examples and demos.
```python
  python src/main.py --yaml <path_to_yaml>
```

App-specific usage:
- OpenAI: Sign up an OpenAI account, and fill in your password in the yaml.
- Twitter: Register a client and fill in required items in the yaml.
- Gmail:
  You will need to generate Google App passward for gmail, and fill it in `sender_password` in the yaml. 
  
  Please refer to `Create & use App Passwords` section on  `https://support.google.com/accounts/answer/185833?hl=en`.

  When sending emails using ChatGPT, please use this prompt: "Write an email from xx to xx using stmi gmail package."
- 
  Youtube: uses Youtube Data API V3 package. You need to install `pip install google-api-python-client`
  and login to your google cloud console `https://console.cloud.google.com/projectselector2/apis/credentials?supportedpurview=project`. Press `Create Project` then `create credential` and add a new `Api_key`. Copy the generated `api_key` to the Yaml.

  Then if you saw 400 error while running the code, go back to your gogole cloud console and click `Eable API Services` and look for `YouTube Data API v3` in the filter, and click enable app. 

  reference: `https://developers.google.com/youtube/registering_an_application`

  - useful commands :
    write python code to show me the most popular 10 videos on YouTube (using google app api).

## Useful Commands and Prompt Templates:
<details>
<summary>Answer in python code only: with API, things you want to do</summary>
This will prompt chatgpt to generate API python calls 
</details>
<details>
<summary>run it</summary> 
run the code generated, it only works only if the last command generated python code
</details>
<details>
<summary>
exit
</summary>
quiting the chatbot
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Basic functionality of chatgpt
- [x] First App integrated with limited functionalities
- [x] Basic documentations
- [ ] Supporting more apps
- [ ] Multi-language Support
    - [ ] English
    - [ ] Chinese
- [ ] Replace with Official API once released

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kaizhao Liang - [@KyleLiang5](https://twitter.com/KyleLiang5) - kyleliang919@gmail.com

Project Link: [https://github.com/kyleliang919/The-Everything-App](https://github.com/kyleliang919/The-Everything-App)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

TBD

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kaizhao-liang-427a42132/
[product-screenshot]: images/screenshot.png