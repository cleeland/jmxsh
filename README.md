# jmxsh

Automatically exported from code.google.com/p/jmxsh by Chris Cleeland
on or around 7 June 2015, yet another person to export this project
from googlecode.  I guess it either needs a shepherd or to die.

The remainder of this document is reproduced verbatim from that page
with minor formatting changes to leverage markdown.

## What is it?

An easy-to-use, scriptable, command-line interface to JMX servers
based on Java/Tcl.  Released under the Apache License 2.0

## Features

* Scriptable Tcl interpreter, based on the Java/Tcl project.
* Use interactively, or run scripts from teh command line.
* Easy-to-use "Browse" mode to explore JMX namespace interactively.
* Connect to multiple servers simultaneously.
* Command-line editing and persistent history using jline.
* User/password authentication, SSL, and jmxmp in addition to rmi.
* Source in mulitple Tcl files from the command line--build a library
  of useful functions.

## Future

* Improve the handling of non-primitive Java objects to be more
  transparent (e.g., auto-convert Java lists to tcl; provide an easier
  way to invoke object methods than Java/Tcl provides)
* Upgrade to the next jline version (0.9.94)
* Automatically source in jmxsh files in top level directory of
  jarfile (So user can add startup files)

## Release History (prior to export)

03-12-2010 - jmxsh-R5.jar

* I never checked jmx_list into subversion, so I'm not sure if I
  actually added it in R4 or not... Ooops.  It's there now and checked
  in.  And I fixed Issue #2

03-03-2009 - jmxsh-R4.jar

* Added jmx_list command to list MBeans.  Takes a regex for domains
  and one for mbeans, and returns a Tcl list.

02-09-2009 - jmxsh-R3.jar

* Fixed jmx_set bug which was the same as the jmx_get bug.  Also fixed
  a bug where error messages of jmx_set weren't being reported.

02-06-2009 - jmxsh-R2.jar

* Fixed jmx_get bug where it was erroring if the ATTROP variable was
  not set, even if you passed an attribute in its command line.
  Thank, Bruce, for the bug report!

02-06-2009 - jmxsh-

* This is a shell script wrapper to the jar file.  It doesn't allow
  you to write standalone scripts, but does allow you to say things
  like `% jmxsh myscript.jmxsh`, etc.  You still need to download the
  jmxsh.jar separately.  Of course, this is a Unix-only thing.
  
Original Release -

* Fully functional as described in the Summary (I think).
