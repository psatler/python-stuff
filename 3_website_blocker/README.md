# Website blocker

The script checks if the current time is a working hour. If so, it then opens the [_hosts file_](https://www.wikiwand.com/en/Hosts_(file)) and check if the website you want to block is there already. If it's not, then you add it to the file. When it's not working hours, the _hosts_ file is read line by line and the websites are removed from it.

On Windows the hosts file is generally located at _C:\Windows\System32\drivers\etc_ path. Though, the original file was copied to the working directory.

## Cron Job Scheduler
On Unix-like operating systems, you can easily schedule a job using the [Cron Job Scheduler](https://www.wikiwand.com/en/Cron). On Linux, it comes already installed. 

Just open Cron Table with `sudo crontab -e` in the terminal. Then, add the path to the main script file (.py) followed by the command _@reboot_. For example, `@reboot python3 path/to/directory/3_website_blocker/web_block.py`. By doing this, when rebooting your computer, it will take effect.


