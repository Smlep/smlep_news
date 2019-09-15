[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Essential
=========

This project is a simple gatherer of different news I found interesting.

Currently, it sends all news gathered through e-mails to all the mail addresses from a database.

To simply send a mail to a target without using any database, use the function `prepare_mail` from `mail`.

Currently the gathered News are the following:

- Weather from [Open Weather Map](https://openweathermap.org)
- Top products from [Product Hunt](https://www.producthunt.com)
- Trending repos from [GitHub](https://github.com)
- News from [Guardian](https://www.theguardian.com) or [Le Figaro](http://www.lefigaro.fr) depending on the language you decide to use (`en` or `fr`)

Architecture
============

This project is divided in different packages:

- `figaro`: fetches french news from [Le Figaro](http://www.lefigaro.fr).
- `github`: fetches trending repos from [GitHub](https://github.com).
- `guardian`: fetches us news from [Guardian](https://www.theguardian.com).
- `mail`: calls gatherer from the other packages, format their content and send mail.
- `product_hunt`: fetches top products from [Product Hunt](https://www.producthunt.com).
- `runner`: gathers e-mail addresses from a database and send the gathered news through e-mails. This package configuration is relative to my own setup, if you want to use this program, you should bring changes to this package (or not use it).
- `weather`: fetches weather from [Open Weather Map](https://openweathermap.org). To choose the city you have to provide an ID, a list of city IDs can be downloaded [here](http://bulk.openweathermap.org/sample/).

API KEYS
========

This program uses APIs from different sources, and some of them require authentication.
You'll have to provided API Keys in `config.json`:

- `DEFAULT.PH_KEY`: Product Hunt Api Key.
- `DEFAULT.WEATHER_KEY`: Open Weather Map Api Key.
- `DEFAULT.GUARDIAN_KEY`: Guardian Api Key.

All these keys can be obtained freely.

To send mails, you need an email account, it is already configured for `gmail` so all which is needed is to provide credentials in `config.json`.

- `MAIL.NAME`
- `MAIL.USERNAME`
- `MAIL.PASSWORD`


