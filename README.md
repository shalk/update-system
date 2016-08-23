# update-system


# SYNOPSIS

	usage: update.py [-h] [-V] {install,status,check} ...
	
	this is update system command line
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -V, --version         show program's version number and exit
	
	commands:
	  {install,status,check}
	    install             install some patch
	    status              get the system status
	    check               check the environment


#app.py
check.py     environment check
cli.py       command line
config.ini   config for program
config.py    config parser and default value
log.py       log config for stream and file handler
orchestra.py orachestra for task (read topo file and generate task info with order )
task.py      task object for bugfix

__init__.py  Update System Class  like a app ; 



#user 
1. install us and prepare bugfix(with topo file)
2. modify config.ini(optional)
3. execute  python update.py [args] (maybe wrapper it ) 

#program

1. in update.py   new a UpdateSystem Object
2. UpdateSystem Object.run()
-------------------------------------
in UpdateSystem 
1. handle config
2. read default(/etc/us/config.ini ,read config, read commandline 
3. judge what to do 
4. if do task,first read orchestra ;generate info then do each task in order
5. if do check,do check
6. if do status, do status
7. if do other ,do other 


 

