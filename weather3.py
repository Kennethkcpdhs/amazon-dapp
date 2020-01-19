import requests, json
import xml.etree.ElementTree as ET
  
api_key = "29039888ecce7edd94fe4a51361c0faa"
  
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = 'Singapore'
  
complete_url = base_url+"appid="+api_key+"&q="+city_name+"&mode=xml"

response = requests.get(complete_url) 
root = ET.fromstring(response.text)
tree = ET.ElementTree(root)

#tree.write("file.xml")
for child in root.iter('*'):
    #print(child.tag,child.attrib)
    if str(child.tag) == 'precipitation':
        if child.attrib['mode'] == 'no':
            print('Not going to rain')
        else:
            print("Chance of precipitation",child.attrib)

'''
if response["cod"] != "404":
    
    y = x["main"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"]
    
    # print following values 
    print(x) 
  
else: 
    print(" City Not Found ") 
'''
