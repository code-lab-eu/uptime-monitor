Uptime monitor
==============

This is a simple Python script that will check a list of sites and send a
notification on a Telegram channel when the site is down.

Usage
-----

* Create a [Telegram bot](https://core.telegram.org/bots/features#botfather).
  You will receive an API token.
* Create a Telegram channel and retrieve its ID.
* Copy the `.env.dist` file to `.env`. Fill in your API token, chat ID and the
  list of URLs you want to monitor.
* Run the script periodically using `cron` or a systemd timer.

