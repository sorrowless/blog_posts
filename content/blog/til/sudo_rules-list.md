Title: How to understand which sudo rules will be applied
Date: 2020-10-2 21:50
Authors: sbog
Slug: sudo-roles-list
Tags: til, sudo, linux
Lang: en

There are cases when you need to understand how your custom sudo rules will be
applied. To understand this, sudo tool provides useful flag

    sbog@personal:~$ sudo -l
    [sudo] password for sbog:
    Matching Defaults entries for sbog on personal:
        !visiblepw, always_set_home, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE INPUTRC", env_keep+="KDEDIR LS_COLORS MAIL PS1 PS2", env_keep+="QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE
        LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES LC_MONETARY", env_keep+="LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE LC_TIME", env_keep+="LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
        secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

    User sbog may run the following commands on personal:
        (ALL) PASSWD: ALL
    sbog@personal:~$

which will return you a list with rules and how they will be processed

