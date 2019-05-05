Title: Ansible remote recursive copy
Date: 2019-05-05 14:34
Authors: sbog
Slug: ansible-synchronize
Tags: til, ansible, copy, sync
Lang: en

#### How to recursively copy directories on remote host with Ansible

Ansible `copy` module cannot recursively copy directories on remote machine.
Of course you can co that by `shell` or `command` modules with `cp -r` in them,
but that's ugly and not recommended by Ansible itself. Additionally you'll get
linter warnings each time you trying to do so. But another method exists - use
trick with `synchronize` method. As usual, example is better that a thousand
words:

        ---
        - name: Sync remote dirs
          hosts: remote.host
          tasks:
            - name: Sync dirs
              synchronize:
                src: /tmp/test/
                dest: /tmp/test2
              delegate_to: "{{ inventory_hostname }}"

Trick is to use `delegate_to` here. How it works - when you're using delegation
to remote hostname, that hostname becomes base host which is initiates command.
As synchronize module by default tries to get the data from base (master) host
and rsync them to target host (which in our case is the same host) - it just
copy all of that locally. Pretty neat.
