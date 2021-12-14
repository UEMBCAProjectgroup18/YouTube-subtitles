from youtube_transcript_api import YouTubeTranscriptApi as yt
import sys
def wellcome(): #'''for welcome message'''
    print("\n")
    print ('╭╮╱╱╭╮╱╱╱╭━━━━╮╱╭╮╱╱╱╱╱╭━━━╮╱╱╭╮╱╭╮╱╭╮╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮\n┃╰╮╭╯┃╱╱╱┃╭╮╭╮┃╱┃┃╱╱╱╱╱┃╭━╮┃╱╱┃┃╭╯╰┳╯╰┫┃╱╱╱╱╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃\n╰╮╰╯╭┻━┳╮┣┫┃┃┣┫╭┫╰━┳━━╮┃╰━━┳╮╭┫╰┻╮╭╋╮╭┫┃╭━━╮╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮\n╱╰╮╭┫╭╮┃┃┃┃┃┃┃┃┃┃╭╮┃┃━┫╰━━╮┃┃┃┃╭╮┃┃┣┫┃┃┃┃┃━┫╱┃┃┃┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯\n╱╱┃┃┃╰╯┃╰╯┃┃┃┃╰╯┃╰╯┃┃━┫┃╰━╯┃╰╯┃╰╯┃╰┫┃╰┫╰┫┃━┫╭╯╰╯┃╰╯┣╮╭╮╭┫┃┃┃╰┫╰╯┃╭╮┃╰╯┃┃━┫┃\n╱╱╰╯╰━━┻━━╯╰╯╰━━┻━━┻━━╯╰━━━┻━━┻━━┻━┻┻━┻━┻━━╯╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯\n')
    print ('                            ¯\_( ͡ᵔ ͜ʖ ͡ᵔ)_/¯\n')



def exit():
    print ("\n╋┏┓┏┓╋╋╋╋╋╋╋┏┓\n┏┛┗┫┃╋╋╋╋╋╋╋┃┃\n┗┓┏┫┗━┳━━┳━┓┃┃┏┓┏┓╋┏┳━━┳┓┏┓\n╋┃┃┃┏┓┃┏┓┃┏┓┫┗┛┛┃┃╋┃┃┏┓┃┃┃┃\n╋┃┗┫┃┃┃┏┓┃┃┃┃┏┓┓┃┗━┛┃┗┛┃┗┛┃\n╋┗━┻┛┗┻┛┗┻┛┗┻┛┗┛┗━┓┏┻━━┻━━┛\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛\n")

def real_caption():#'''for normal caption extractor'''
    yt_trans= yt.get_transcript(ytv_id,languages=['en-IN','en'])
    global op
    op =""
    for i in yt_trans:
        op += ' \n'+i['text']
    #print (op)



def For_translation():#'''for translated caption extractor'''
    b = input("\nWe Support Three Language For Translation\nPlease Enter Which Language You Want \n\nFor Hindi Type = hi \nFor Bengali Type = bn\nFor Spanish Type = es\n:: ")
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
        



def for_output(a): # for output .txt file
    sys.stdout = open("output.txt", "w")
    print(a)
    sys.stdout.close()




def working():#'''switch case for selecting work'''
    temp = int(input("Enter 1 For Work With Subtitles\nEnter 2 For Work With Transteted Subtitles\n:: "))
    if temp == 1:
        real_caption()
    elif temp==2:
        For_translation()
    else:
        print("Something Being Wrong !! Please Try Again")



wellcome()
#'''vedio prossecing unit'''
yt_vedio = input("Please Enter The Vedio Link :: ")#"youtube.com/watch?v=PP9bexwAdwA" 
ytv_id = yt_vedio.split("=")[1]
working()
exit()
for_output(op)



