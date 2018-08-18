# no-ip-updater
Update your IP to no-ip.info service from your own Raspberry every 15 minutes.

How to run the script:
- Create a folder in **/no-ip-updater** to save the file **no-ip-updater.py**
- Create a file named **ips.txt** in the folder
- Change the permision to these files to run the script and to append text
- Add the following line to your cron service: 
```
*/15 * * * * /usr/bin/python /no-ip-updater/actualizar_ip.py 2>&1
```
- Restart the cron service.
