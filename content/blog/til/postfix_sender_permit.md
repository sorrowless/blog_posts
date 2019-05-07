Title: Postfix explicit permits for sender domain
Date: 2019-05-07 14:34
Authors: sbog
Slug: postfix-permits
Tags: til, postfix
Lang: en

#### How to explicitly trust some sender domains in postfix

Today I stuck with situation when my personal Postfix mail server discarded
emails from the domain which I had to trust. Message from logs:


        May  7 16:56:11 personal-vps postfix/smtpd[30414]: NOQUEUE: reject: RCPT from
        mail-182-75.mailgun.info[23.253.182.75]: 450 4.1.7
        <bounce+cc8a03.552af-<redacted>@<redacted>>: Sender address rejected:
        unverified address: host aspmx.l.google.com[173.194.222.27] said: 550-5.1.1 The
        email account that you tried to reach does not exist. Please try 550-5.1.1
        double-checking the recipient's email address for typos or 550-5.1.1
        unnecessary spaces. Learn more at 550 5.1.1  h;
        from=<bounce+cc8a03.552af-<redacted>@<redacted>>
        to=<redacted@sbog.ru> proto=ESMTP helo=<mail-182-75.mailgun.info>

It happens due to wrong configuration of sender mail server - sender is trying
to send emails from bounce address which does not exists, but RFC does not
recommend that, cause that address is not verifiable and, as a result, looks
like a spam for mail servers. But I had needed an email from this domain, so
temporarily added to my Postfix next configuration:

        root@personal-vps:/etc/postfix# cat sender_permits
        <sender domain placed here>      permit

        root@personal-vps:/etc/postfix# grep -A1 smtpd_sender_restrictions main.cf
        smtpd_sender_restrictions =
            hash:/etc/postfix/sender_permits,

        root@personal-vps:/etc/postfix# postmap sender_permits
        root@personal-vps:/etc/postfix# postfix reload
        root@personal-vps:/etc/postfix#

After this I was able to get needed emails from wrong configured sender domain.
