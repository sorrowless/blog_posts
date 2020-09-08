Title: How to find role id in Ansible galaxy
Date: 2020-09-08 23:51
Authors: sbog
Slug: ansible-galaxy-role-id
Tags: til, ansible
Lang: en

In case you need to find Ansible galaxy role id (e.g. for badge in your Github
repo), you can just run

    ansible-galaxy info YourUser.RoleName | grep -E 'id: [0-9]' | awk {'print $2'}

which will return you a bunch of info with role id in it.

