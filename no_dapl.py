#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import android

droid = android.Android()
data = open('/storage/external_SD/Download/nd_officals.txt')
text = droid.dialogGetInput("Text to public officials","type your message here","").result

for line in data:
    line = line.replace('\n','')
    droid.smsSend( (line),text)
data.close()
