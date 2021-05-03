# Profil3r

For educational purposes only.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<div align="center">
<a href="https://www.buymeacoffee.com/givocefo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

[![Twitter Badge](https://img.shields.io/badge/-@Rog3rSm1th-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/Rog3rSm1th)](https://twitter.com/Rog3rSm1th)

</div>

Profil3r is an [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

![](https://i.imgur.com/hzmfCg0.gif)
## 💡 Prerequisite
[Python 3](https://www.python.org/)

## 🛠️ Installation

Install PyInquirer and jinja2 :

```bash
pip3 install PyInquirer jinja2
``` 

Install Profil3r :

```bash
git clone https://github.com/Rog3rSm1th/Profil3r.git
cd Profil3r/
sudo python3 setup.py install
```
## Features

#### 📙 Domain
- [x] TLD (.com, .org, .net, etc...)

#### ✉️ Emails 
- [x] Data leaks
- [x] Emails

#### 🌐 Social
- [x] Instagram
- [x] Facebook
- [x] Twitter
- [x] Tiktok
- [x] Pinterest
- [x] Linktr.ee
- [x] MySpace

#### 🎵 Music

- [x] Soundcloud
- [x] Spotify

#### ‍💻 Programming

- [x] Github
- [x] Pastebin
- [x] Repl.it
- [x] Cracked.to

#### 💬 Forum

- [x] 0x00sec.org
- [x] Jeuxvideo.com
- [x] Hackernews

#### 🗣️ Tchat

- [x] Skype

#### 📺 Entertainment

- [x] Dailymotion
- [x] Vimeo

#### 🚫 Porn

- [x] PornHub
- [x] RedTube
- [x] XVideos

#### 💸 Money

- [x] BuyMeACoffee
- [x] Patreon

## 📖 Report

#### JSON

A report in JSON format is automatically generated in the `reports/json` folder

#### CSV

A report in CSV format is automatically generated in the `reports/csv` folder

#### HTML

A report in HTML format is automatically generated in the `reports/html` folder, you can access it in your webbrowser

![](https://i.imgur.com/6Ts0eL4.gif)

## ⚙️ The config.json file 

You can modify the paths of the reports, the separators and the services Profil3r will search by default in the `config.json` file

| Field | Type | Default | Description |
|-----------------|--------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| report_elements | Array | `["email", "facebook", "twitter"]` | List of the services for which profil3r will search |
| json_report_path | String | `"./reports/json/{}.json"` | The path of the report's JSON file, this path must include a {} which corresponds to the file name |
| html_report_path | String | `"./reports/html/{}.html"` | The path of the report's HTML file, this path must include a {} which corresponds to the file name |
| csv_report_path | String | `"./reports/csv/{}.csv"` | The path of the report's CSV file, this path must include a {} which corresponds to the file name |
separators |Object|`{"Dot": ".", "Dash": "-", "Underscore": "_"}`| List of separators to separate items, for example: `john.doe`, `john-doe`, `john_doe`|

## 📚 Example

```bash
python3 profil3r.py -p john doe
```

## 📝 License

This project is under the MIT license.

## Contact 

for any remark, suggestion or job offer, you can contact me at r0g3r5@protonmail.com or on twitter [@Rog3rSm1th](https://twitter.com/Rog3rSm1th)