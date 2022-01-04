# (Impor Libs)

from youtube_transcript_api import YouTubeTranscriptApi as yt
import sys,re

def wellcome(): # (This is the Wellcome Part For User)
    print("\n")
    print ('\033[91m╭╮╱╱╭╮╱╱╱╭━━━━╮╱╭╮╱╱╱╱╱╭━━━╮╱╱╭╮╱╭╮╱╭╮╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮\n┃╰╮╭╯┃╱╱╱┃╭╮╭╮┃╱┃┃╱╱╱╱╱┃╭━╮┃╱╱┃┃╭╯╰┳╯╰┫┃╱╱╱╱╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃\n╰╮╰╯╭┻━┳╮┣┫┃┃┣┫╭┫╰━┳━━╮┃╰━━┳╮╭┫╰┻╮╭╋╮╭┫┃╭━━╮╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮\n╱╰╮╭┫╭╮┃┃┃┃┃┃┃┃┃┃╭╮┃┃━┫╰━━╮┃┃┃┃╭╮┃┃┣┫┃┃┃┃┃━┫╱┃┃┃┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯\n╱╱┃┃┃╰╯┃╰╯┃┃┃┃╰╯┃╰╯┃┃━┫┃╰━╯┃╰╯┃╰╯┃╰┫┃╰┫╰┫┃━┫╭╯╰╯┃╰╯┣╮╭╮╭┫┃┃┃╰┫╰╯┃╭╮┃╰╯┃┃━┫┃\n╱╱╰╯╰━━┻━━╯╰╯╰━━┻━━┻━━╯╰━━━┻━━┻━━┻━┻┻━┻━┻━━╯╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯\n\033[00m')
    print ('                            \033[92m¯\_( ͡ᵔ ͜ʖ ͡ᵔ)_/¯\n\033[00m')

def exit(): # (This is the Thank You!! Part For User)
    print("\n\033[96m▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █ █\n░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   ▄ ▄\n\033[00m")

def wrong(): # (For Anything Wrong Input By User)
    print("\n\033[91m█▀ █▀█ █▀▄▀█ █▀▀ ▀█▀ █░█ █ █▄░█ █▀▀   █ █▀   █░█░█ █▀█ █▀█ █▄░█ █▀▀   █ █\n▄█ █▄█ █░▀░█ ██▄ ░█░ █▀█ █ █░▀█ █▄█   █ ▄█   ▀▄▀▄▀ █▀▄ █▄█ █░▀█ █▄█   ▄ ▄\n\n█▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   ▀█▀ █▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█\n█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ░█░ █▀▄ ░█░   █▀█ █▄█ █▀█ █ █░▀█\n\033[00m")

def real_caption(ytv_id): # (For English Transcript)
    yt_trans= yt.get_transcript(ytv_id,languages=['en-IN','en'])
    global op
    op =""
    for i in yt_trans:
        op += ' \n'+i['text']
    #print (op)

def For_translation(ytv_id): # (For Translated Transcript)
    lang = input("\n\033[92mWe Support Three Language For Translation\033[00m\n\nPlease Enter Which Language You Want \n\nFor Hindi Type = hi \nFor Bengali Type = bn\nFor Spanish Type = es\n\n:: ")
    sys.stdout.write("\n\033[93mWork in Progress...\n\033[00m\n") #(For Waiting Pop-Up)
    if lang=='hi':
        yt_trans_list = yt.list_transcripts(ytv_id)
        yt_trans = yt_trans_list.find_transcript(['en'])
        yt_trans.fetch()
        translated_yt_trans = yt_trans.translate('hi')
    elif lang=='bn':
        yt_trans_list = yt.list_transcripts(ytv_id)
        yt_trans = yt_trans_list.find_transcript(['en'])
        yt_trans.fetch()
        translated_yt_trans = yt_trans.translate('bn')
    elif lang=='es':
        yt_trans_list = yt.list_transcripts(ytv_id)
        yt_trans = yt_trans_list.find_transcript(['en'])
        yt_trans.fetch()
        translated_yt_trans = yt_trans.translate('es')
    else:
        wrong()
        sys.exit()

    yt_tr_final=translated_yt_trans.fetch()
    global op
    op =""
    for i in yt_tr_final:
        op += '\n'+i['text']
    #print(op)

def for_output(a):  # (For Output) 
    temp = input("A name for Your Output File :: ") 
    exit()
    sys.stdout = open(temp+".txt", "w")
    print(a)
    sys.stdout.close()
    
def working(ytv_id): # (Switch Case For Selecting language)
    temp = int(input("\n\033[94mEnter 1 For Work With Subtitles\nEnter 2 For Work With Transteted Subtitles\n\033[00m:: "))
    if temp == 1:
        sys.stdout.write("\n\033[93mWork in Progress...\n\033[00m\n") #(For Waiting Pop-Up)
        real_caption(ytv_id)
    elif temp==2:
        For_translation(ytv_id)
    else:
        wrong()
        sys.exit()




		#(This is The Combine All The Work or Functions) 

def id_extractor(): # For Extract The Link Id 
    yt_vedio = input("Please Enter The Vedio Link :: ")     #("youtube.com/watch?v=PP9bexwAdwA")   
    temp= re.findall('(http(s|):\/\/|)(www.|)youtube.(com|nl)\/watch\?v\=([a-zA-Z0-9-_=]+)',yt_vedio) # (Check Youtube link Is True or Not)
    if temp:
        ytv_id = yt_vedio.split("=")[1]      #(Help Us To extract the Vedio ID for Transcript API)
        return ytv_id                        #return ytv_id
    else:
        wrong()
        sys.exit()
          

wellcome()                                              #(For Wellcome User)
ytv_id=id_extractor()                                   #(For Id Extracting Part)
working(ytv_id)                                         #(Working Prossecing Unit)
for_output(op)                                          #(This is for last part of our project, the output unit)
#op=a (in for_output function)                          #("youtube.com/watch?v=PP9bexwAdwA")





