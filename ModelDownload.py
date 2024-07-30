import os
import psutil
import subprocess
import time

def sd_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20 -d /home/xlab-app-center/models/stable_diffusion -o realisticasianthaila_v20.ckpt")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//DreamShaper_8_pruned.safetensors -d /home/xlab-app-center/models/stable_diffusion -o DreamShaper_8_pruned.safetensors")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//rev-animated-v1-2-2.safetensors -d /home/xlab-app-center/models/stable_diffusion -o rev-animated-v1-2-2.safetensors")

def sdXL_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realistic_bailingXL_v2.safetensors -d /home/xlab-app-center/models/stable_diffusion_xl -o realistic_bailingXL_v2.safetensors")

def AnimateDiff_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/houshaowei/AnimateDiff/weight//mm_sd_v15.ckpt -d /home/xlab-app-center/models/AnimateDiff -o mm_sd_v15.ckpt")

def is_port_in_use(port):
    """
    检查指定端口是否被占用
    """
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return True
    return False

def start_jupyter_lab(port=8889):
    """
    启动 JupyterLab
    """
    if not is_port_in_use(port):
        #环境变量的内网穿透账号
        ak = os.getenv("OPENXLAB_AK")
        if not ak:
            print("Environment variable OPENXLAB_AK is not set.")
            return
        ngrok_command = ak
        jupyter_command = f"jupyter-lab --no-browser --ip=0.0.0.0 --allow-root --notebook-dir=/ --port={port} --LabApp.allow_origin=* --LabApp.token= --LabApp.base_url="
        # 启动 ngrok 进程
        ngrok_process = subprocess.Popen(ngrok_command, shell=True)
        # 启动 Jupyter 进程
        jupyter_process = subprocess.Popen(jupyter_command, shell=True)
    else:
        print(f"Port {port} is already in use, JupyterLab cannot be started.")


#多进程启动
import multiprocessing
if __name__ == '__main__':
    ls = multiprocessing.Process(target=start_jupyter_lab) # 创建子进程
    ls.start() # 子进程 开始执行
    ls.join() # 等待子进程结束
