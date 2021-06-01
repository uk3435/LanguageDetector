from langdetect import detect_langs


def ayir(text): # seperates the detect_langs() function output to probability values. exp: from [eng:0.9,tr:0.1] to [0.9,0.1]

    deger=text.split(":")
    return deger[1]

def dilSonucu(text):# seperates the detect_langs() function output to langs. exp: from [eng:0.9,tr:0.1] to [eng, tr]

    sonuc=text.split(":")
    return sonuc[0]

NihaiSonuc="" #Final result in Turkish :)

with open("yourFile.txt", "r", encoding="utf-8") as f: # reads the txt file 
    lines = [line.rstrip() for line in f]
    for text in lines:
        print(text)
        olasiliklar=detect_langs(text) #probabilities list
        
        
        if len(olasiliklar)>1 : #if more than one language is forecasted
            
            o1=float(ayir(str(olasiliklar[0]))) #first probability
            o2=float(ayir(str(olasiliklar[1]))) #second probability
          
            if o1 >= 0.75:
                NihaiSonuc=dilSonucu(str(olasiliklar[0]))
                print(NihaiSonuc)
            if o1<0.75:
                print("Tahmin Edemedi") # can't forecast (below %75)
                
    
        else:

            o1=ayir(str(olasiliklar[0]))
            print(o1)
            NihaiSonuc=dilSonucu(str(olasiliklar[0]))
            print(NihaiSonuc)
        
        print(detect_langs(text))
        
