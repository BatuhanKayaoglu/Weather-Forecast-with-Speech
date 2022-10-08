import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtWidgets,QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *  ##Size metodunu kullanabilmek icin
import pyttsx3 
 




class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        self.setWindowTitle("Weather Forecast")
        self.setGeometry(650, 300,250, 420)
        self.setStyleSheet("background-color:white;")
        


        
        
        
    
    def init_ui(self):
        

        self.iconArea=QtWidgets.QLabel()
        self.iconArea.setAlignment(Qt.AlignCenter)  
        

        
        
        self.lineEditArea=QtWidgets.QLineEdit()
        self.lineEditArea.setFixedSize(QtCore.QSize(250, 35))
        self.lineEditArea.setStyleSheet("background-color:#666666; color:white;border-radius: 15px 15px 15px 15px;")
        self.lineEditArea.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditArea.setFont(QFont("Times font", 13))
 
        
        
        self.searchButton=QtWidgets.QPushButton("Weather Forecast")
        self.searchButton.setStyleSheet('QPushButton {background-color: #363636; color:white; font-weight:bold;}')
        self.searchButton.setFixedSize(QtCore.QSize(250, 40))
        self.searchButton.setFont(QFont('Times', 12))
        self.searchButton.setIcon(QIcon("C:/Users/pc/Documents/Python Scripts/PYQT5 Dersleri/weatherForecast/images/searchIcon2"))
        #buton üzerine gelindiginde renk değişmesi için
        # self.searchButton.setStyleSheet("QPushButton::hover"
        #                     "{"
        #                     "background-color :#828282;"
        #                     "}")
        
        
        #butona tıklandıktan sonra
        # self.searchButton.setStyleSheet("QPushButton"
        #                       "{"
        #                       "background-color :#363636;"
        #                       "}"
        #                       "QPushButton::pressed"
        #                       "{"
        #                       "background-color :#828282;"
        #                       "}"
        #                       )
        
        
        
        
        
        self.cityInfo=QtWidgets.QLabel()
        self.cityInfo.setFont(QFont('Times', 19))
        self.cityInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.cityInfo.setStyleSheet("font-style: italic")
        
        
        
        self.weatherTemp=QtWidgets.QLabel()
        self.weatherTemp.setFont(QFont('Times', 24))
        self.weatherTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherTemp.setStyleSheet("font-weight: bold")
        #self.weatherTemp.setStyleSheet("color:red")
        
        
        
        self.feltTemp=QtWidgets.QLabel()
        self.feltTemp.setFont(QFont('Times', 15))
        self.feltTemp.setAlignment(QtCore.Qt.AlignCenter)
        #self.feltTemp.setStyleSheet("font-weight: bold")
        
        
        
        self.descriptions=QtWidgets.QLabel()
        self.descriptions.setFont(QFont('Times', 19))
        self.descriptions.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptions.setStyleSheet("font-weight: bold")
        
        self.speech=QtWidgets.QPushButton("Speak")
        self.speech.setFixedSize(QtCore.QSize(250, 40))
        self.speech.setStyleSheet('QPushButton {background-color: #525151; color:white; font-weight:bold;}')
        self.speech.setFont(QFont('Times', 11))
        self.speech.setStyleSheet("background-color:#666666; color:white;border-radius: 15px 15px 15px 15px;")
        self.speech.setIcon(QIcon("C:/Users/pc/Documents/Python Scripts/PYQT5 Dersleri/weatherForecast/images/speechIcon"))
        size = QSize(30, 37) ##ICONA BOYUT VERME
        self.speech.setIconSize(size) ##ICONA BOYUT VERME
        self.speech.move(300,70)
        self.speech.hide()
        
        
        
        
        
        
        
        
        vBox=QtWidgets.QVBoxLayout()
        vBox.addWidget(self.lineEditArea)
        vBox.addWidget(self.searchButton)
        vBox.addWidget(self.iconArea)
        vBox.addWidget(self.iconArea, alignment=Qt.AlignCenter)
        vBox.addWidget(self.cityInfo)
        vBox.addWidget(self.weatherTemp)
        vBox.addWidget(self.feltTemp)
        vBox.addWidget(self.descriptions)
        vBox.addWidget(self.speech)


        vBox.addStretch()        
        self.setLayout(vBox) ## Üstteki kodları pencereye ekleme işine yarıyor.
        
        
        self.searchButton.clicked.connect(self.searching)  
        self.speech.clicked.connect(self.speeching)
        
        
        self.show()
    
            

        

        
       

        
    def searching(self):
        self.speech.show()
        url="https://api.openweathermap.org/data/2.5/weather?"
        apiKey="yourApiKey"
        city=self.lineEditArea.text()
        url2=url+"appid="+apiKey+"&q="+city 
        data=requests.get(url2)
        dataJson=data.json()
    
        temp=dataJson["main"]["temp"]
        self.temp=round((dataJson["main"]["temp"]-273.15),1)
        
        
        self.desc=dataJson["weather"][0]["description"].capitalize()
        pressure=dataJson["main"]["pressure"]
        country=dataJson["sys"]["country"]
        citys=dataJson["name"]
        icon=dataJson["weather"][0]["icon"]
        feelTemp=round((dataJson["main"]["feels_like"]-273.15),1)
        
        
        #Hava durumlarını türkçeye çevirmek için
        skyTypes = ['Clear Sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
        skyTypesTR = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
        
        for i in range(len(skyTypes)):
            if self.desc == skyTypes[i]:
                skyDescription = skyTypesTR[i]
        
        self.weatherTemp.setText(str(self.temp)+"°C")
        self.cityInfo.setText(citys+","+country)
        self.descriptions.setText(self.desc)
        self.feltTemp.setText("Felt Temperature: "+str(feelTemp))

        pixmap = QtGui.QPixmap("C:/Users/pc/Documents/Python Scripts/PYQT5 Dersleri/weatherForecast/images/"+(icon))
        self.iconArea.setPixmap(QtGui.QPixmap("C:/Users/pc/Documents/Python Scripts/PYQT5 Dersleri/weatherForecast/images/"+(icon)))


    def speeching(self):
       speak=pyttsx3.init()
       speak.setProperty("rate",110)
       speak.setProperty("volume",1.0)
       speak.say("Weather temperature is"+str(self.temp)+"degrees Celsius and"+self.desc)
       speak.runAndWait()
    
 



        



app=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(app.exec_())
