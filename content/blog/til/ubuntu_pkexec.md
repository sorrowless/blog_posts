Title: Ubuntu root access to sudo when sudoers is broken
Date: 2020-08-04 19:52
Authors: sbog
Slug: root-pkexec
Tags: til, pkexec, ubuntu, root, sudo, sudoers
Lang: en

#### How to run visudo in case your sudoers is broken

All of us make mistakes from time to time. Some of them are okay. Some are
not. For a long time I thought that broken sudoers file related to the second
ones. Fortunately, that's not true. Today I learn how to fix broken sudoers
in case you just had to have a sudo but not apply it as long as sudoers does
not work anymore. That solution is right for Ubuntu (tested on Xenial, Bionic,
Focal releases) and may (or may not) work on other distros. All you need to
have is a `pkexec` tool. It is preinstalled by default and is a part of
PolKit framework. So there is what you need to do to edit broken sudo:

* Open two shells under your user which had to have root access
* On the first one run `echo $$` to get current console PID
* On the second one run `pkttyagent --process PID_FROM_STEP_1` where
  PID_FROM_STEP_1 is a number from `echo $$` of previous step
* On the first console run `pkexec bash`. You will be asked for your
  administrative password on second console. Enter it.
* That's it. You're now running `bash` shell as root on the first console. Go
  and fix your sudoers

That trick works due to the fact that PolKit is enabled by default in Ubuntu
and it does not use sudoers directly. By default it configured the way which
allows to become root even in case sudoers file is broken as a result.
