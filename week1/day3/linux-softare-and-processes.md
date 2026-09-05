       APT commands - 
update - look for latest catalog of software
upgrade - read the updated catalog and install the latest version
how apt (advanced package tools) installs a software - catalog lookup(apt check the cached packages and find the location and version of the software)
- dependency resolution(check if the software need s any supporting software to run the software)
- download(connects to remote ubuntu repositories to dowload required .deb package files)
- install and setup - unpack the files , place them in to system directories , setup with systemd so that software is ready to run
       systemd and service management
systemctl status - checks the status of a specific service
systemctl start -  start the service
systemctl stop - stop the service
restart - restart the seervice
is-active - active or inactive the service is
is-enabled - prints if its enabled
         what is a process?
its a active instance of active programs loaded in to ram executed by cpu.every process has a unique PID to linux to track it 
what is nginx - its a web server host and reverse proxy, it is a multiprocess service , master and worker process. so that it uses less cpu usage , worker process run 1 process per cpu core. high performace.zero downtime reload(update website's config ar ssl certificate without breaking user connection or stopping server)
      process monitoring commands
ps,top,htop,pgrep,kill
