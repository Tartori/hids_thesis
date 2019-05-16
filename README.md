# hids_thesis

## Todos

* Finish Setting up Latex
* Decide on a Programming Language
* Add the ability to scann the whole system with Sleuthkit
* Add a Database connector to one type of database
* Add a recording function that records the scan.
* Implement functionality to create rules
* Implement the functionality to run the scan according to some rules
* Implement some sort of alerting function
* Add the functionality to scale it to a big file system
* Add functionality of repeated scans
* Add multiple connections to different database systems
* Add multiple different versions of alerting
* Add software hardening --> detection of modification of software or config

### new todos

* adding table wiht errors
* storing everything on every run
* extending fids file table to contain all the information of TSK for file and directory
* the alerting stuff

``` bash
file.info.meta.attr is sadly not acessible... 

>>> file.info.meta.
file.info.meta.addr         file.info.meta.content_len  file.info.meta.ctime        file.info.meta.link         file.info.meta.nlink        file.info.meta.type
file.info.meta.atime        file.info.meta.content_ptr  file.info.meta.ctime_nano   file.info.meta.mode         file.info.meta.seq          file.info.meta.uid
file.info.meta.atime_nano   file.info.meta.crtime       file.info.meta.flags        file.info.meta.mtime        file.info.meta.size         
file.info.meta.attr_state   file.info.meta.crtime_nano  file.info.meta.gid          file.info.meta.mtime_nano   file.info.meta.tag   
```

#### mile stones

* finished coding with prototype
* update documentation

## programming language decisions

### java

pros:

* already very good knowledge
* some community resources

cons:

* low motivation
* low learning potential
* big overhead

### python

pros:

* already some basic foundation
* a lot of community resources
* active library to directly call sleuthkit tool
* lot of activity in community
* small overhead
* easy to prototype

cons:

* dynamically typed

### go

pros:

* interesting new language
* made for (low level) server side applications

cons:

* no prior knowledge
* no prior community support

## meeting notes

* I will contact expert and setup a meeting with him
* Main points of that meeting is describing what I want to do / project
* and Showing that I already put in some work.
* ils command
* fls -v output

### schedule

* daemon vs scheduled task
* what timestamp to put
* how to add it to db, once per file, batched
* adding a tag for each run
* different objects for different file systems
* timezones (later)
* cool name
* Journal!

### next meeting

* 11.4.19 11:00 Cafeteria Biel

KMail on phone for pgp mails

## expert meeting notes 28.03

Discussion Points:

* what do I do

## links

<http://www.sleuthkit.org/sleuthkit/docs/api-docs/4.2/structTSK__FS__FILE.html#a74c7fc77db20b5c4efc617806fd49e2e>
<https://github.com/py4n6/pytsk/wiki/Development>