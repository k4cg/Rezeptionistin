import time
from plugin import Plugin

class Authentication(Plugin):
  auth_jobs = []

  def check_user_authentication(self, bot, user_nick, success_callback, failure_callback=None):
    auth_job = {
      "nick": user_nick,
      "success": success_callback,
      "failure": failure_callback,
      "created_at": time.time()
    }
    self.auth_jobs.append(auth_job)
    bot.send_command("nickserv", "ACC " + user_nick)

  def on_notice(self, bot, user_nick, host, channel, message):
    if user_nick.lower() == "nickserv" and ("ACC" in message):
      nick = message.split()[0]
      status = message[-1:]

      for job in self.auth_jobs:
        if job["nick"] == nick:
          if status == '3':
            job["success"]()
          elif job["failure"]:
            job["failure"]()
          self.auth_jobs.remove(job)
          break

    # throw out all jobs older than 20 sec
    self.auth_jobs = [job for job in self.auth_jobs if (time.time() - job["created_at"] < 20.0)]
