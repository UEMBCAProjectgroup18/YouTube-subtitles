#!/usr/bin/python
from youtube_transcript_api import YouTubeTranscriptApi as yt
import sys, time 




		# (For Welcome Message)

def wellcome(): 
    print("\n")
    print ('\033[91m╭╮╱╱╭╮╱╱╱╭━━━━╮╱╭╮╱╱╱╱╱╭━━━╮╱╱╭╮╱╭╮╱╭╮╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮\n┃╰╮╭╯┃╱╱╱┃╭╮╭╮┃╱┃┃╱╱╱╱╱┃╭━╮┃╱╱┃┃╭╯╰┳╯╰┫┃╱╱╱╱╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃\n╰╮╰╯╭┻━┳╮┣┫┃┃┣┫╭┫╰━┳━━╮┃╰━━┳╮╭┫╰┻╮╭╋╮╭┫┃╭━━╮╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮\n╱╰╮╭┫╭╮┃┃┃┃┃┃┃┃┃┃╭╮┃┃━┫╰━━╮┃┃┃┃╭╮┃┃┣┫┃┃┃┃┃━┫╱┃┃┃┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯\n╱╱┃┃┃╰╯┃╰╯┃┃┃┃╰╯┃╰╯┃┃━┫┃╰━╯┃╰╯┃╰╯┃╰┫┃╰┫╰┫┃━┫╭╯╰╯┃╰╯┣╮╭╮╭┫┃┃┃╰┫╰╯┃╭╮┃╰╯┃┃━┫┃\n╱╱╰╯╰━━┻━━╯╰╯╰━━┻━━┻━━╯╰━━━┻━━┻━━┻━┻┻━┻━┻━━╯╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯\n\033[00m')
    print ('                            \033[92m¯\_( ͡ᵔ ͜ʖ ͡ᵔ)_/¯\n\033[00m')






		# (This is the Thank You!! Part For User)

def exit():
    print("\n\033[96m▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █ █\n░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   ▄ ▄\n\033[00m")





		# (For English Transcript)

def real_caption():
    yt_trans= yt.get_transcript(ytv_id,languages=['en-IN','en'])
    global op
    op =""
    for i in yt_trans:
        op += ' \n'+i['text']
    #print (op)





		# (For Translated Transcript)

def For_translation():
    b = input("\n\033[92mWe Support Three Language For Translation\033[00m\n\nPlease Enter Which Language You Want \n\nFor Hindi Type = hi \nFor Bengali Type = bn\nFor Spanish Type = es\n\n:: ")
    sys.stdout.write("\n\033[93mWork in Progress...\n\033[00m\n") #(For Waiting Pop-Up)
    yt_trans_list = yt.list_transcripts(ytv_id)
    yt_trans = yt_trans_list.find_transcript(['en'])
    yt_trans.fetch()
    translated_yt_trans = yt_trans.translate(b)
    yt_tr_final=translated_yt_trans.fetch()
    global op
    op =""
    for i in yt_tr_final:
        op += '\n'+i['text']
    #print(op)
        
        
        
        

		# (For Output File)

def for_output(a):
    temp = input("A name for Your Output File :: ") 
    exit()
    sys.stdout = open(temp+".txt", "w")
    print(a)
    sys.stdout.close()
    




		# (Switch Case For Selecting language) 

def working():
    temp = int(input("\n\033[94mEnter 1 For Work With Subtitles\nEnter 2 For Work With Transteted Subtitles\n\033[00m:: "))
    if temp == 1:
        sys.stdout.write("\n\033[93mWork in Progress...\n\033[00m\n") #(For Waiting Pop-Up)
        real_caption()
    elif temp==2:
        For_translation()
    else:
        print("Something Being Wrong !! Please Try Again")




		#(This is The Combine All The Work or Functions) 

wellcome()                                              #(For Wellcome User)
yt_vedio = input("Please Enter The Vedio Link :: ")     #("youtube.com/watch?v=PP9bexwAdwA")  
ytv_id = yt_vedio.split("=")[1]                         #(Help Us To extract the Vedio ID for Transcript API)
working()                                               #(Working Prossecing Unit)
for_output(op)                                          #(This is for last part of our project, the output unit)
#op=a (in for_output function)



