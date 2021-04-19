# Profil3r

<a href="https://www.buymeacoffee.com/givocefo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Profil3r is an [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

![](https://i.imgur.com/xK1aDR0.gif)
## 💡 Prerequisite
[Python 3](https://www.python.org/)

## 🛠️ Installation
```bash
git clone https://github.com/Rog3rSm1th/Profil3r.git
cd Profil3r/
python3 setup.py install
```
## Features

#### Emails 
- [x] Data leaks
- [x] Emails

#### Social
- [x] Instagram
- [x] Facebook
- [x] Twitter
- [x] Tiktok
- [x] Pinterest

#### Music

- [x] Soundcloud
- [x] Spotify

#### Programming

- [x] Github
- [x] Pastebin

#### Forum

- [x] 0x00sec.org
- [x] Jeuxvideo.com

#### Tchat

- [x] Skype

#### Entertainment

- [x] Dailymotion

## 📖 Report

A report in JSON format is automatically generated in the `reports` folder

## ⚙️ The config.json file 

You can modify the report path and the services Profil3r will search in the `config.json` file

| Field            | Type   | Default                            | Description                                                                                         |
|-----------------|--------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| report_elements | Array  | `["email", "facebook", "twitter"]` | List of the services for which profil3r will search                                                 |
| report_path     | String | `"./reports/{}.json"`              | The path of the report's JSON file, this path must include a {} which corresponds to the file name |

## 📚 Example

```bash
python3 profil3r.py john doe
```

## 📝 License

This project is under the MIT license.

## Contact 

for any remark, suggestion or job offer, you can contact me at r0g3r5@protonmail.com or on twitter [@Rog3rSm1th](https://twitter.com/Rog3rSm1th)