git add filename 
git commit -a -m
git diff readme.txt 查看改动
git log --pretty=online  查看提交日志

git reset --hard HEAD^ 版本回退到上一个版本
HEAD is now at 2205b26 wrote a readme file

git reset --hard [版本号] 回退到指定版本

git reflog[查看git使用命令历史]
b920846 HEAD@{0}: reset: moving to b920
2205b26 HEAD@{1}: reset: moving to HEAD^
b920846 HEAD@{2}: commit: add GPL
2205b26 HEAD@{3}: commit (initial): wrote a readme file

1:git add  [将修改过的文件放到stage暂存区，以待提交]
2:git commit [只提交stage里的文件]
每次修改，如果不add到暂存区，那就不会加入到commit中

＃撤销修改
1:如果没有git add readme.txt放到暂存区，用git checkout -- readme.txt 撤销修改
2:如果git add readme.txt放到了暂存区，git reset HEAD readme.txt 把暂存区的修改撤销掉,再git checkout -- readme.txt撤销

[没有git add ,git checkout -- <file>]git checkout HEAD -- readme.txt
[如果已经git add放到暂存区，git reset HEAD <file>将修改从暂存区丢弃,再git checkout -- <file>撤销修改]

git checkout HEAD -- readme.txt
git reset HEAD <file> 只会撤销暂存区的本次修改，不会覆盖工作区的修改

#git rm 删除文件
git rm test.txt
git checkout -- test.txt 撤销删除

#远程仓库
git remote add origin git@github.com:NextZeus/learngit.git
git push -u origin master
由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。


#branch
Git鼓励大量使用分支：

查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>


用带参数的git log也可以看到分支的合并情况：
git log --graph --pretty=oneline --abbrev-commit 

#--no-off
git merge --no-ff -m "merge with no-ff" dev
合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并

#git stash
git stash apply 应用缓存区的修改
git stash drop 删除缓存区
git stash pop [上面两个的总命令]
git stash list
=======
#删除分支
git branch -d 分支名
git branch -D 分支名 [强制删除]

#git remote
git remote 查看远程库的信息
git remote -v 显示更详细信息

git push origin master
git push origin dev
git pull <remote> <branch>
git fetch

git pull如果失败了，原因是没有指定本地dev分支与远程origin/dev分支的链接，根据提示，设置dev和origin/dev的链接
$ git branch --set-upstream dev origin/dev
Branch dev set up to track remote branch dev from origin.

因此，多人协作的工作模式通常是这样：

首先，可以试图用git push origin branch-name推送自己的修改；

如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

如果合并有冲突，则解决冲突，并在本地提交；

没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！

如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream branch-name origin/branch-name。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。


#tag 标签
git tag <name>
git tag v1.0
命令git tag <name>用于新建一个标签，默认为HEAD，也可以指定一个commit id；

git tag -a <tagname> -m "blablabla..."可以指定标签信息；

git tag -s <tagname> -m "blablabla..."可以用PGP签名标签；

命令git tag可以查看所有标签。

git tag -d v1.0 删除标签

git push origin v1.0 推送标签到远程
git push origin --tags 推送所以标签到远程
git push origin :refs/tags/v0.9

#实验
bogon:learngit $ git push origin --tags
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/NextZeus/learngit.git
 * [new tag]         v0.9 -> v0.9
 * [new tag]         v1.0 -> v1.0
bogon:learngit $ git push origin :refs/tags/v0.9
To https://github.com/NextZeus/learngit.git
 - [deleted]         v0.9


#配置命令别名
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD'
git config --global alias.prettylog 'log --pretty=oneline'

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"


