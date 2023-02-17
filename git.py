# git脚本工具
import os
import sys 
import subprocess
# file_name = sys.argv[1]
pwd = os.getcwd()
class Git:
    def git_init(self):
        status = subprocess.Popen('git init',shell=True,cwd=pwd)
    def git_set(self):
        num = input("请输入user:")
        num2 = input("请输入email:")
        status = subprocess.Popen(f'git config --global user.name "{num}"',shell=True,cwd=pwd)
        status2 = subprocess.Popen(f'git config --global user.name "{num2}"',shell=True,cwd=pwd)
    def git_all(self):
        status = subprocess.Popen('git add .',shell=True,cwd=pwd)
    def git_commit(self):
        status = subprocess.Popen(f'git commit -m {input("请输入版本号：")}',shell=True,cwd=pwd)
    def git_push(self):
        status = subprocess.Popen('git push -u origin master',shell=True,cwd=pwd)
    def get_status(self):
        status = subprocess.Popen(f'git status',shell=True,cwd=pwd)
    def get_log(self):
        status = subprocess.Popen(f'git log --oneline',shell=True,cwd=pwd)
    def reset_o(self):
        num = input("请输入id:")
        status = subprocess.Popen(f'git reset --hard {num}',shell=True,cwd=pwd)
    def reset_s(self):
        num = input("请输入id:")
        status = subprocess.Popen(f'git reset --hard {num}',shell=True,cwd=pwd)
    def reset_u(self):
        status = subprocess.Popen(f'git reset --hard HEAD^',shell=True,cwd=pwd)
    def reset_l(self):
        num = input("请输入id:")
        status = subprocess.Popen(f'git checkout {num}',shell=True,cwd=pwd)
    def menu(self):
        print('-'*30)
        print('1.上传仓库')
        print('2.回到上一个版本')
        print('3.查看日志')
        print('4.初始化仓库')
        print('5.返回指定版本')
        print('0.退   出')
        print('-'*30)
if __name__ == "__main__":
    git = Git()
    while True:
        git.menu()
        num = input("请输入选项:")
        if num == "1":
            git.git_all()
            git.git_commit()
            git.git_push()
        elif num == "2":
            git.reset_u()
        elif num == "3":
            git.get_log()
        elif num == "4":
            git.git_init()
        elif num == "5":
            git.get_log()
            git.reset_s()
        elif num == 0:
            break
        else:
            pass
