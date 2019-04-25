Title: Vimdiff
Date: 2019-04-25 16:30
Authors: sbog
Slug: vimdiff
Tags: til, vim
Lang: en

#### How and why to use vimdiff as git mergetool

For many years I've used standard Git merge tool. Couple times I tried to use
vimdiff as I saw my collegaues using it and were able to fix merge conflicts
faster and easier than I can. But it also looked to much complex and I always
have thrown it halfway. But recently I was involved in a big task which
contained a rebase 10+ downstream commits ahead of upstream which was like 250
commits ahead current downstream master. It looks like nightmare to work on
merge conflicts with standard Git tool for big and old commits, so I decided
to use `vimdiff` for that task. So, here it is in a nutshell:

* first, make sure you have a vimdiff at all. Basically, if you have vim,
  that's it

* next, ensure that you're using vimdiff as a git merge tool:

  ```
  git config merge.tool vimdiff
  git config merge.conflictstyle diff3
  git config mergetool.prompt false
  ```

  first command is about to use vimdiff as a git diff tool, second one enables
  diff3 format, third disables prompt invocation at each run of merge tool

* not required, but nice to have is to add to your `.vimrc` something like

  ```
  if &diff
    colorscheme desert
  endif
  ```

  cause defautl vimdiff colors can be inconvenient for you

Basically that's it. When next time you'll have a merge conflict and run
*git mergetool*, it will show you a screen like this:

![Git vimdiff diff3](https://www.rosipov.com/images/posts/three-way-merge-with-vimdiff.png)

From left to right:

`LOCAL` is a file from your *current* branch
`BASE` is a file from common ancestor between your local branch and remore one
`REMOTE` is a file from *remote* branch

at the bottom you'll see `MERGED` - it is what you'll have in result. Now all
depends on what you wanted to do. To do any of them, first move to the bottom
part of the screen (`MERGED` one), then put your cursor to the merge conflict
ares. There are 4 cases:

1. Save local changes. Run `:diffget LO`
1. Save base changes. Run `:diffget BA`
1. Save remote changes. Run `:diffget RE`
1. Rewrite resulted code manually

After you've done, save file and quit (`:wqa`), commit your changes and you're
done.

Big thanks for all that info for [this manual][1] - I get most of this info
from there.

[1]: https://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/
