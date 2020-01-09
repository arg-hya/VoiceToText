import speech_recognition as sr
import docx


#samples per second (Hertz)
sample_rate = 48000
#Higher chunk_size values help avoid triggering on rapidly changing ambient noise,
#but also makes detection less sensitive. This value, generally, should be left at its default.
chunk_size = 2048 #1024

r = sr.Recognizer() 

device_id = 0 
record_text = "You said: "
record = False

with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    
    r.adjust_for_ambient_noise(source) 
    print ("Say Something...")
    while (True) :
        
        audio = r.listen(source) 
              
        try: 
            text = r.recognize_google(audio)            
            record_text += text
##            if (text.find('begin') != -1):
##                print ("begin")
##                record = True
##
##            if (record == True):
##                record_text += text
##                
            if (text.find('stop') != -1):
                print ("\n Module Stoped...")
##                record = False
                break
            print ("you said: " + text) 
          
        
          
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
          
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

print ("\n Processing and Writing to DOC...")
record_text.replace("stop", ' \n ')
record_text.replace("newline", ' \n ')
record_text += "\n"
doc = docx.Document("SampleDoc.docx")
doc_para = doc.add_paragraph(record_text)
doc.save("InstallerNotes.docx")


print (record_text)
