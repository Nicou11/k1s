import subprocess
import json
import time

# 설정 변수
def get_cpu_usage():
    cpu_usage=[]
    subprocess.run(["docker", "compose", "up", "-d"])
    for i in range(1,+1):
        r = subprocess.check_output(["docker", "stats", f"samdul-blog-{i}", "--no-stream", "--format", "{{json .}}"])
        j = json.loads(r.decode("utf-8"))
        cpu_usage.append(float(j.get("CPUPerc", "사용량 없음").strip('%')))
        print(cpu_usage)
    scale = 1
    while True:
        # Scale Out
        if sum(cpu_usage) < 0.09 and scale < 4:
            print("Start Scale Out")
            scale += 1
            subprocess.run(["docker", "compose", "up", "--scale", f"blog={scale}", "-d"])
            print(sum(cpu_usage))
        # Scale In
        #elif sum(cpu_usage) >= 0.08 and scale > 9:  # 최소 scale 제한
        elif scale >= 4:  # 최소 scale 제한
            print("Start Scale In")
            try:
                scale -= 1
                subprocess.run(["docker", "compose", "up", "--scale", f"blog={scale}", "-d"])
            except:
                print(f"Stop Scale in")
        time.sleep(2)

get_cpu_usage()