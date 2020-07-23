from time import sleep
import configparser
import json
import asyncio
from datetime import date, datetime
from datetime import date
from telethon.sync import TelegramClient, events
from telethon.tl import functions
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPeerUser, InputMessagesFilterEmpty
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
today = date.today()
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)
config = configparser.ConfigParser()
config.read("copy.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

#  client created and connect....
client = TelegramClient(username, api_id, api_hash)
#filter=InputMessagesFilterMedia()
async def main(phone):
    await client.start()
    print("Client Created")
    d=input("do you want to todays quiz only? Yes or no ")
    if d.lower()=='y' or d.lower()=='yes':
        todayquiz=True
    else:
        todayquiz=False
    searchlist=['AIIMSquiz', 'LICAAO', 'Naik', 'MBAcrystalball', 'IPS', 'Raus IAS Study Circle', 'Aakash', 'Bansal',
 'SAARC', 'Symcom', 'IMUCETquiz', 'Mindworkzz', 'NATA', 'ifocus training services', 'VITEEEquiz', 
 '@UPSCFutureIAS', 'Alchemist', 'AUEET', 'KEE', 'IAS', 'SRMJEEEquiz', 'hindi', 'SSCJE', 'SSCJEquiz', 
 'sahilstudy', 'JEE', 'ADB', ' Reasoning Ability', 'CET Tutorials', 'Degradation', 'NABARD', 'ISROquiz',
  'Excel Management Foundation', 'unacademy', 'English', 'AMIEquiz', 'GRE', 'Meditech', '@TestSeries4UPSC ', 
  'IMS', 'JIPMER', 'KIITEEquiz', '@Notes4CivilServices', 'vidyamandir', 'IITJAM', 'Marigold Classes', 
  'UNASUR', 'neet', 'NABARDquiz', 'ECETFDHquiz', 'RRBSSE', 'IPUCETquiz', '@Ethics4UPSC', 'RRBNTPC', 'NATAquiz', 
  'Robotics', '@MathematicsOptionals ', 'CSIRNETquiz', 'AIIMS', 'LPUNESTquiz', 'IITJAM', 'Finance', 
  'Real Business Education', 'https://t.me/PollQuizeBreaker', 'Physical Geography', '@UPSCBooksStore', 
  'PGCETquiz', '@PubAdOptionals', '@LawForCivilServices', 'Phoenix Anglo Academy', 
  'Agricultural Finance & Insurance', 'VITEEE', 'RRBALP', '@Pdfs4AllExams', 'DRDOquiz', 'VMUEEEquiz',
   'Butchi Reddy Institute', 'ALS IAS Academy', 'NSG', 'Emphatic Result Academy', 'CAT', 'BIMSTEC', 'OSEE', 
   'CSEquiz', 'TripuraJEEquiz', '@All_Ncert_Books', 'SCO', 'IBPS', '@CivilServices_Mains', 'BVPCETquiz',
'RRBJE', 'Vajiram and Ravis IAS Academy', 'ssc', 'Slietquiz', 'Mathiit Learning', 'HSCquiz', 'chemistry', 
'@UPSCPrelimsMainsMaterials', '@EconomicsOptionals', 'ISRO', 'Quest', 'UPscquiz', 'JEEMAIN', 'Astitva I.C.S.',
 'Defence Academy Coimbatore', '@AnthropologyOptionals', 'data science', 'FCIquiz', 'TIME', 'DRDO', 'BRICS', 
 'CUSATCATquiz', 'IAS', 'IBPSquiz', '@UPSCMainsGS4', 'GCC', 'BITSATquiz', 'https://t.me/BotQuizGroup', 
 'WBJEEquiz', '@banking_quizs', 'CDS', 'SSCJHT', 'Professional Rating', '@UPSC_PrelimsMains', 'geography', 
 '@PSIROptionals', 'SSCCPOquiz', 'RRBJEquiz', 'Competitive Careers', 'AMUEEEquiz', 'IPSquiz',
  'Atomic Chemistry', 'JEEADVANCED', '@CSAT4_UPSC', 'Indian Soils', 'NDA', 'CATquiz', 'civics', 'QUAD',
   'Electronics', 'CSE', 'JIPMERquiz', ' Geophysical phenomena', 'Nanotechnology', 'GATE', 'BCECEquiz',
    'LICAAOquiz', 'Sathya IAS Academy', 'Advent', 'NEETquiz', 'RRBSSEquiz', 'ruby', 'MAHCETquiz', 
    'NarayanaGroup', 'NAFTA', 'SSCCPO', 'gujrati', 'agricultural produce', 'GATEquiz', 'Bio-Chemistry',
     'Quantitative Aptitude', '@OptionalsGeography', 'Indian Architecture incl. Art & Craft & Paintings',
      'SSCquiz', '@SociologyOptionals', 'KEAMquiz', 'Economics', 'Rao IIT', 'SSCMTS', '@UPSCMains_GS1', 
      '@UPSCMainsGS3', 'Technology', 'Electricity', 'Engineering', 'JEEADVANCEDquiz', 'BEEEquiz', 'ias',
       'SSCJHTquiz', 'XAT', 'Accountancy', 'BSAUEEEquiz', 'KRISHNA COACHING', 'allencareer', 
       '@Quiz_adda_24_7', '@HandWrittenNotesPdf', 'Vidyasagar', 'ITSATquiz', 'AEEEquiz', 'ITSAT',
        '@PhysicsOptionals', 'Resonance', 'CTETquiz', 'TIME (Triumphant Institute of Management Education)', 
        '@HistoryOptionals', 'UGCNETquiz', 'RailwayExam', 'ESIC', 'VSATquiz', 'Marketing', 'ESICquiz', 
        'Pathfinder', 'IT', '@CivilServicesPrelims', 'BYJUs CAT Classes', 'tamil', 'JEEMAINquiz', 'ASEM', 
        'Chanakya IAS Academy', 'Bulls Eye', 'XATquiz', 'Medical', 'magnetism', 'CTET', 'FCI', 
        'Brain Tree India', 'languages', 'Insight', 'UGCNET', '@UPSCMainsGS2', 'upsc', 'Magnus Institute',
         'General Awareness', 'Advance Education Center', 'ENATquiz', 'Khan Study Circle', 'physics', 
         'CSIRNET', 'Jayant Pai', 'biology', 'VEEquiz', 'elite', 'BITSAT', 'Programming', 'CDSquiz',
          'Career', 'IBSA', 'machine learning', 'FITJEE', 'Agrawal', 'Pie Education', 'SAATquiz', 'NATO', 
          'java', 'GREquiz', 'marathi', 'https://t.me/UnAcademyplusBotQUIZ', 'NDAquiz', '@Essay4CivilServices', 
          'python', 'Brilliant', 'SSCMTSquiz', 'Matrix Academy', 'RRBALPquiz', 'TCYonline', 'RRBNTPCquiz', 
          'mathematics', 'OrissaJEEquiz'
               ]    
    user_input_channel=[]
    for search in searchlist:
        sleep(10)
        try:
            channels= await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
        ))
            ch=channels.results
            for c in range (0,len(ch)):
                l=str(ch[c].channel_id)
                if l not in user_input_channel:
                    user_input_channel.append(l)
                print(l)
        except:
            continue        
    print(len(user_input_channel))    
    for i in user_input_channel:
        sleep(5)
        print(i)
        if i.isdigit():
            entity = PeerChannel(int(i))
        else:
            entity = i    
        my_channel = await client.get_entity(entity)
        if todayquiz==True:
            jsonname=str(my_channel.id)+"-"+str(date.today())+".json"
        else:    
            jsonname=str(my_channel.id)+".json"
        print(jsonname)    
        offset_id = 0
        all_messages = []
        total_messages = 0
        total_count_limit = 100
        quiz=[]
        limit = 10000
        while True:
            history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0,
            ))
            if not history.messages:
                break
            messages = history.messages
            for m in messages:
                all_messages.append(m.to_dict())
                d={}
                ans=[]
                try:    
                    r=m.media.results.results
                    anwer=m.media.poll.answers
                    now=str(m.date)
                    now1=now.split()
                    if now1[0]==str(date.today()) and todayquiz==True:
                        k=1
                        d['Date']=str(m.date)
                        d["question"]=m.media.poll.question
                        for j in anwer:        
                            m="option%s"%(k)
                            d[m]=j.text
                            ans.append(j.text)
                            k=k+1
                        try:
                            for t in r:
                                corr=t.correct
                                if corr is True:
                                    op=t.option.decode("utf-8")
                                    inte=int(op)
                                    d['Answer']=ans[inte]
                        except:
                            d['Answer']="No answer given"   
                        s=d.copy()    
                        quiz.append(s)
                    elif todayquiz==False:
                        k=1
                        d['Date']=str(m.date)
                        d["question"]=m.media.poll.question
                        for j in anwer:        
                            m="option%s"%(k)
                            d[m]=j.text
                            ans.append(j.text)
                            k=k+1
                        try:
                            for t in r:
                                corr=t.correct
                                if corr is True:
                                    op=t.option.decode("utf-8")
                                    inte=int(op)
                                    d['Answer']=ans[inte] 
                        except:
                            d['Answer']="No answer given"  
                        s=d.copy()    
                        quiz.append(s)
                except:
                    continue
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            print(quiz)
            if total_count_limit != 0 and total_messages >= total_count_limit:
                if len(quiz)!=0:
                    sleep(3)
                    with open(jsonname, 'w') as outfile:
                        json.dump(quiz, outfile)        
                break
with client:
    client.loop.run_until_complete(main(phone))
