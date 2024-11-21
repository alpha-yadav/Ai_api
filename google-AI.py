import requests as r
import time
import os
import mimetypes as mime
_mime_={"js":"javascript","py":"python","bat":"bash","sh":"bash"}
while True:
    try: 
        q=input("? ")
        if(q=='q'):
            break
        elif(q=="cls"):
            os.system(q)
            continue
        qx=q.split(">")
        req=r.request("POST","https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCw03bfTk5VlYmt-diyWiowxKqYZc9BnA4",data='{"contents":[{"parts":[{"text":"'+qx[0]+'"}]}]}',headers={"Content-Type": "application/json"})
        data=req.json()
        raw=data['candidates'][0]['content']['parts'][0]['text'].splitlines()
        if(len(qx)>1):
            i=0
            f_name=qx[1]
            k=1
            extx=_mime_.get(f_name.split(".")[1]) if("." in f_name) else 0
            if(extx==None):
                ext=f_name.split(".")[1]
            elif(extx==0):
                qx.pop()
            else:
                ext=extx
        for d in raw:
            data=""
            dat=d.split("**")
            if(len(dat)==3):
                data+="\033[91m\033[21m"+dat[1]+"\033[00m\033[93m"+dat[2]+"\033[00m\n"
            else:
                data+="\033[93m"+dat[0]+"\033[00m\n"
            time.sleep(0.1)
            print(data,end="")
            if(len(qx)>1 and k==1):
                if(ext=="md"):
                   qx[1]=open(f_name,"a")
                   qx[1].write(d+"\n")
                   qx[1].close() 
                   continue
                if(("```"+ext) in d):
                    i=1
                    continue
                if(i==1):
                    if("```" in d): #or ("#" in d and "Example" in d)):
                        i=0
                        k=0
                        break
                    qx[1]=open(f_name,"a")
                    qx[1].write(d+"\n")
                    qx[1].close()
        #print(ext)
    except KeyboardInterrupt:
        print("#"*42,"Context Switch","#"*42)
    except EOFError:
        print("for Exit Enter \"q\"")

    #if(len(qx)>1):
    #    qx[1].close()
#>>> k=r.request("POST","https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCw03bfTk5VlYmt-diyWiowxKqYZc9BnA4",data='{"contents":[{"parts":[{"text":"Explain how AI works"}]}]}',headers={"Content-Type": "application/json"})