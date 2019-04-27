Title: Ansible hostvars
Date: 2019-04-25 16:30
Authors: sbog
Slug: ansible-hostvars
Tags: til, ansible
Lang: en

#### Neat trick of usage ansible hostvars

When one is using ansible host vars, usually there are couple ways to do so:

* Use plaintext yaml files. This way will work if you do not have sensitive
  information in them

* Use fully vault-encrypted yaml files. This way is pretty okay, but you will
  have to decrypt them before get any useful info from them (even
  non-sensitive). First of all, it takes some time. Second, you have to write
  some tools if you want to get such info (like ip addresses of hosts) from
  several files at once.

* Use partially encrypted yaml files. Sensitive info can be encrypted as
  strings. This way have couple problems too. First, you do not have convenient
  way to encrypt/decrypt them (actually, you *can* achieve that by 3rd party
  tools but it's still inconvenient). Second, there is **no** way to rekey
  these strings even in one file by one command - you have to do that manually.

But there is one way to achieve needed level of security - and even more,
actually. Documentation to Ansible says that you can create *directories*
named after host names and store yaml files in these directories - all these
files will be appreciated at runtime, merged with each other, unencrypted and
so on. So, main idea is to place all sensitive vars to one file and all
non-sensitive to another. In non-sensitive file you should define your
sensitive keys and point them to values in file with sensitive data. It allows
to encrypt file with sensitive data completely but still know most of info by
reading file which is non-encrypted. Here it is by example.

Let's say you have host named *babylon*. Here is how host vars for it will look
like:

        > tree host_vars/babylon
        host_vars/babylon
        ├── babylon_vault.yml
        └── babylon.yml

Let's take a quick look at vars in `babylon.yml`:

        > head host_vars/babylon/babylon.yml
        ---
        ansible_host: "{{ vault_ansible_host }}"
        ansible_port: "{{ sshd_port }}"
        ansible_user: "{{ ansible_common_user }}"
        ansible_become: true

Look at `ansible_host` var. It has a value named `vault_ansible_host`. Now
look at `babylon_vault.yml`:

        > ansible-vault view host_vars/babylon/babylon_vault.yml | head
        ---
        vault_ansible_host: <redacted - it is still sensitive info, man>

So, when we run `ansible-playbook` for host `babylon`, it will take both files,
and substitute sensitive info from `babylon_vault.yml` to `babylon.yml`,
that's it. You can have your `babylon_vault.yml` file fully encrypted.

The same trick you can use for cases your yaml vars files grows too big and you
want to split them. Let's look at the example:

        > tree host_vars/personal_vps
        host_vars/personal_vps
        ├── backup_vault.yml
        ├── backup.yml
        ├── common.yml
        ├── mail_vault.yml
        ├── mail.yml
        ├── website_vault.yml
        └── website.yml

Pretty useful, huh? That's all for today. Hope it was helpful info.
