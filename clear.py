import time;
while(1):
    with open("post.file","r",encoding="utf-8") as f:
        fl=f.readlines();
        for i in range(len(fl)):
            if(fl[i]!="\n"):
                if(int(time.time())-int(fl[i].split("||")[1])>=5):
                    fl[i]="";
            else:
                fl[i]="";
    with open("post.file","w",encoding="utf-8") as f:
        for i in fl:
            if(i.strip()!=""):
                f.write(i+"\n")
    time.sleep(1);


