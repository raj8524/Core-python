#source control is surveillence system of the source code. GIT is distributed VCS.Git stores the snapshot not the difference.

"""
GIT States:
Modified-files r modified .GIT knows it but GIT cant do anthting about it.
STAGED: git has marked this for next snapshot.
commited: snapshot taken.

steps:
1.git clone https://github.com/raj8524/flask_blog.git           from github repo
2.ls -la
3.git status     # to see the staus of ur repo,in which state is it and how it looks as compare to origin/master
4.git log        # all commits done on this repo
5.git log --patch -1     #to see detail of log
add somthing in file .
6.git status   # after making changes in repo , can see in modified state   ..will be in red color

7.git add test.txt     # file cloned and changes done it. this is to change from modified to stagged state
8.git status          # can see that changes to be committed     will be in green color

#when u want to move file from staged to modified,unstagged state
9.git restore --staged Test.txt
10.git status       # can see the modified state file

#  will restore as clone file as it was when clonned.
11.git restore Test.txt
12.git status


13.git commit -m "my first commit"   # this will be committed in local
14.git status
15.git remote -v       #to check origin of the file.

16.git push origin master  #to push to master

#when new file is there in ur local,changes r done.
17.git status    will show the new file there in modified state
18.git add .   will move all file in dirctory local/folder to stagged state

##--------branching.......Learngit is the master.to Learngit now,will create branch
19.git log --oneline --decorate     #will show head is pointing to master
20.git branch develop       #develop branch is created to Learngit master  in local
21.git status
22.git log --oneline --decorate    #can see that head is pointing to head as well as develop
23.git checkout develop    # to move to develop branch
24.git status         #can see on branch develop ,nothing to commit

#new file is there develop_test.txt under develop branch.
25.git status   #can see the develop_test.txt in modified state
26.git add develop_test.txt    # will change develop_test.txt from modified to staged state
27.git commit -m "first commit file under branch"
28.git status
29.git log --oneline --decorate    #can see first commit in branch head pointing to develop
30.git remote -v
31.git push origin develop        #because we r in develop branch rit now
32.git log --oneline --decorate
33.git checkout master       #switched from branch to master  because we want develop to merge to master
34.git merge develop       #develop is merged to master locally
35.git status
36.git log --oneline --decorate    #can see head to master,develop
37.git push origin master  #it is now pushed to github


   git config --global user.name "raj8524"
   git init      It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.
   git add .     The git add command adds a change in the working directory to the staging area.
   git commit -m "my_first_testing"
   git remote add origin https://github.com/raj8524/flask_blog.git
   git status
   git push -u origin master


































"""