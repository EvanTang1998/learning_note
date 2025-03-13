
git 显示当前路径下的git仓库
find ./  -name ".git" -type d -prune | sed 's/\/\.git//'

pycharm 自动风格化：菜单栏—Code—Reformat File

查看git config
git config —list
设置用户名
git config --global user.name "Your Name"
git config --local user.name "Your Name"
git config --global user. email "you@example.com"
查看用户名
git config user.name

git remote -v 查看远程仓库配置
撤销一次add 操作 git reset
撤销最近一次commit ：git reset --soft HEAD^


提交流程
建一个卡片
git add .
复制卡片上的 commit
git commit -m "复制的内容"
git push origin HEAD:refs/for/master   #origin是远程地址的名称  提交到origin的master分支 注意refs似乎不能写成refers
如果有问题 可以直接本地修复后:  
git add .
git commit —amend --no-edit可以直接修改commit信息
git push origin HEAD:refs/for/master   
也就是第二步改成追加，然后重新push同样的就可以了

最后git pull --rebase 是本地跟远程保持一致
git pull origin master
git pull <remote> <branch>

当git与本地不一致时 可以 git fetch 然后 git merge 

git reset —hard 将本地代码重置为最近一次提交 并丢弃当前未保存的修改

######
将本地分支调整为跟远程一致：
git fetch origin
git reset --hard origin/master
#####

git log  origin/master 查看远程分支的内容
显示git仓库的根目录
git rev-parse --show-toplevel
查看所有远程分支
git branch -r
git diff branch_a branch_b 对比两个分支 —stat 可以简化输出
切换分支
git checkout [option] <branch>      -b可以创建
