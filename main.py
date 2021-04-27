import random
import sys
import PySide2.QtCore
from PySide2.QtGui import QKeyEvent, QPixmap,  QTextDocument, QPainter, QFontMetrics, QPen, QColor, QLinearGradient
from PySide2.QtWidgets import QApplication, QListWidget, QMainWindow, QLabel, QWidget, QHeaderView, QHBoxLayout, QTableView, QSizePolicy, QVBoxLayout
from PySide2.QtCore import QFile, Slot, QEvent, QTimer, QEvent, QPropertyAnimation, QEasingCurve, QTimeLine, QObject, QPoint, QRandomGenerator, QPointF, Qt, Signal, QUrl
from PySide2.QtCharts import QtCharts
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from form import Ui_pipboy
import description 

class MainWindow(QMainWindow):
    def __init__(self):
        global pixmapDict, specialDescriptionDict
        super(MainWindow, self).__init__()
        self.ui = Ui_pipboy()
        self.ui.setupUi(self)
        
        self.ui.chartContainer.setContentsMargins(0, 0, 0, 0)
        
        self.anim = QTimeLine(20000, self)
        self.anim.setFrameRange(0, 500)
        self.anim.setLoopCount(0)
        self.anim.setUpdateInterval(16)
        self.anim.frameChanged[int].connect(self.ui.perks_description.verticalScrollBar().setValue)
        self.anim.frameChanged[int].connect(self.ui.aid_effect_label.verticalScrollBar().setValue)
        self.anim.frameChanged[int].connect(self.ui.data_description.verticalScrollBar().setValue)
        
        #self.anim2 = QPropertyAnimation(self.ui.main_tab, b"pos")
        #self.anim2.setEasingCurve(QEasingCurve.OutBounce)
        #self.anim2.setDuration(2000)
        #self.anim2.setStartValue(QPoint(10, -400))
        #self.anim2.setEndValue(QPoint(10, 0))
        #self.anim2.start()
        
        self.random = QRandomGenerator.global_()
        
        self.ui.stat_tab.setFocus()
        self.ui.stat_tab.currentChanged.connect(self.shift)
        self.ui.stat_tab.installEventFilter(self)
        self.ui.inv_tab.installEventFilter(self)
        
        self.ui.special_list.installEventFilter(self)
        self.ui.perks_list.installEventFilter(self)
        self.ui.test_list.installEventFilter(self)
        self.ui.apparel_list.installEventFilter(self)
        self.ui.aid_list.installEventFilter(self)
        self.ui.ammo_list.installEventFilter(self)
        self.ui.data_list.installEventFilter(self)
        self.ui.radio_list.installEventFilter(self)
        
        
        self.ui.main_img.setPixmap(description.main_img_pixmap)
        
        self.ui.special_image.setPixmap(description.pixmapDict.get(0))
        self.ui.perks_image.setPixmap(description.pixmatPerksDict.get(0))
        self.ui.weapon_image.setPixmap(description.pixmapWeaponDict.get(0))
        self.ui.apparel_image.setPixmap(description.pixmapWeaponDict.get(0))
        self.ui.aid_image.setPixmap(description.pixmapAidDict.get(0))
        self.ui.ammo_image.setPixmap(description.pixmapAmmoDict.get(0))
        
        lay = QVBoxLayout(self.ui.chartContainer)
        lay.setContentsMargins(0, 0, 0, 0)

        self.chartview = QtCharts.QChartView()
        self.chartview.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)
        
        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        
        self.series = QtCharts.QLineSeries()
        self.pen = QPen(QColor(119, 251, 81, 255))
        self.pen.setWidth(3)
        self.pen.setJoinStyle(Qt.RoundJoin)
        self.series.setPen(self.pen)
        
        backgroundGradient = QLinearGradient(QPointF(100, 100), QPointF(200, 200))
        
        backgroundGradient.setColorAt(0, QColor( 0, 0, 0, 255))
        backgroundGradient.setColorAt(1, QColor( 0, 0, 0, 255))
        self.chart.setBackgroundBrush(backgroundGradient)
        self.chart.setPlotAreaBackgroundBrush(backgroundGradient)
        
        self.chart.addSeries(self.series)
        
        self.chart.createDefaultAxes()
        
        self.chart.axisX(self.series).setVisible(False)
        self.chart.axisY(self.series).setVisible(False)
        self.chart.axisY(self.series).setRange(0, 100)
        self.chartview.setChart(self.chart)
        
        self.play = False
        self.player = QMediaPlayer()
        
        self.playlistFalloutNewVegas = QMediaPlaylist(self.player)
        self.playlistFalloutNewVegas.addMedia(QMediaContent(description.falooutNewVegas))
        self.playlistFalloutNewVegas.setCurrentIndex(1)
        
        self.playListMohaveMusic = QMediaPlaylist(self.player)
        
        for url in description.mohaveMusic:
            self.playListMohaveMusic.addMedia(QMediaContent(url))
        
        self.playListMohaveMusic.setCurrentIndex(1)
        
        self.playlisNewVegas = QMediaPlaylist(self.player)
        
        for url in description.newVegas:
            self.playlisNewVegas.addMedia(QMediaContent(url))
        
        self.playlisNewVegas.setCurrentIndex(1)
        
        self.playlistDict = {0: self.playlistFalloutNewVegas, 1:  self.playListMohaveMusic, 2: self.playlisNewVegas}
        
    def append_data_and_plot(self, d):
        """Append and update the plot"""
        num, m = d

        ax1 = self.chart.axisX(self.series)
        

        xmin = xmax = num

        step = 100
        
        for p in self.series.pointsVector()[-step:]:
            xmin = min(p.x(), xmin)
            xmax = max(p.x(), xmax)


        xmin = max(0, xmax - step)

        ax1.setMin(xmin)
        ax1.setMax(xmax)

        self.series.append(QPointF(num, m))
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            #print(obj)
            if event.key() == 49:
                self.ui.main_tab.setCurrentIndex(1)
                self.ui.stat_tab.setFocus()
                #self.ui.hp_head.setValue(self.random.bounded(50, 100))
                #self.ui.hp_left_arm.setValue(self.random.bounded(50, 100))
                #self.ui.hp_right_arm.setValue(self.random.bounded(50, 100))
                #self.ui.hp_left_leg.setValue(self.random.bounded(50, 100))
                #self.ui.hp_right_leg.setValue(self.random.bounded(50, 100))
                #self.ui.hp_body.setValue(self.random.bounded(50, 100))
                return True
            elif event.key() == 50:
                self.ui.main_tab.setCurrentIndex(2)
                self.ui.inv_tab.setFocus()
                return True
            elif event.key() == 51:
                self.ui.main_tab.setCurrentIndex(3)
                self.ui.data_list.setFocus()
                self.ui.data_list.setCurrentRow(0)
                return True
            elif event.key() == 52:
                self.ui.main_tab.setCurrentIndex(4)
                return True
            elif event.key() == 53:
                self.ui.main_tab.setCurrentIndex(5)
                self.ui.radio_list.setFocus()
                self.ui.radio_list.setCurrentRow(0)
                return True
            elif event.key() == 54:
                print(QApplication.focusWidget())
                return True
            #focus from stat_tab to special_list
            elif(obj == self.ui.stat_tab) and (self.ui.stat_tab.currentIndex() == 1) and (event.key() == 47):
                self.ui.special_list.setFocus()
                self.ui.special_list.setCurrentRow(0)
                self.ui.special_image.setPixmap(description.pixmapDict.get(0))
                self.ui.special_description.setText(description.specialDescriptionDict.get(0))
                return True
            #
            elif (obj == self.ui.special_list) and (event.key() == 16777236):
                self.ui.special_list.setCurrentRow(self.ui.special_list.currentRow() + 1)
                
                if(self.ui.special_list.currentRow() == -1):
                    self.ui.special_list.setCurrentRow(0)
                    
                self.ui.special_list.scrollToItem(self.ui.special_list.currentItem())
                
                self.ui.special_image.setPixmap(description.pixmapDict.get(self.ui.special_list.currentRow()))
                self.ui.special_description.setText(description.specialDescriptionDict.get(self.ui.special_list.currentRow()))
                
            elif (obj == self.ui.special_list) and (event.key() == 16777234):
                self.ui.special_list.setCurrentRow(self.ui.special_list.currentRow() - 1)
                
                if(self.ui.special_list.currentRow() == -1):
                    self.ui.special_list.setCurrentRow(0)
                    
                self.ui.special_list.scrollToItem(self.ui.special_list.currentItem())
                
                self.ui.special_image.setPixmap(description.pixmapDict.get(self.ui.special_list.currentRow()))
                self.ui.special_description.setText(description.specialDescriptionDict.get(self.ui.special_list.currentRow()))
            #focus from special_list to stat_tab
            elif(obj == self.ui.special_list) and (event.key() == 47):
                self.ui.special_list.setCurrentRow(-1)
                self.ui.stat_tab.setFocus()
                return True
            # focus from stat_tab to perks_list
            elif(obj == self.ui.stat_tab) and (self.ui.stat_tab.currentIndex() == 2) and (event.key() == 47):
                self.ui.perks_list.setFocus()
                self.ui.perks_list.setCurrentRow(0)
                self.anim.setCurrentTime(0)
                self.anim.start()
            elif (obj == self.ui.perks_list) and (event.key() == 16777236):
                self.ui.perks_list.setCurrentRow(self.ui.perks_list.currentRow() + 1)
                
                if(self.ui.perks_list.currentRow() == -1):
                    self.ui.perks_list.setCurrentRow(0)
                    
                self.ui.perks_list.scrollToItem(self.ui.perks_list.currentItem())
                
                self.ui.perks_image.setPixmap(description.pixmatPerksDict.get(self.ui.perks_list.currentRow()))
                self.ui.perks_description.setText(description.perksDescriptionDict.get(self.ui.perks_list.currentRow()))
                
                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            elif (obj == self.ui.perks_list) and (event.key() == 16777234):
                self.ui.perks_list.setCurrentRow(self.ui.perks_list.currentRow() - 1)
                
                if(self.ui.perks_list.currentRow() == -1):
                    self.ui.perks_list.setCurrentRow(0)
                    
                self.ui.perks_list.scrollToItem(self.ui.perks_list.currentItem())
            
                
                self.ui.perks_image.setPixmap(description.pixmatPerksDict.get(self.ui.perks_list.currentRow()))
                self.ui.perks_description.setText(description.perksDescriptionDict.get(self.ui.perks_list.currentRow()))
                
                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            #focus from perks_list to stat_tab
            elif(obj == self.ui.perks_list) and (event.key() == 47):
                self.ui.perks_list.setCurrentRow(-1)
                self.ui.stat_tab.setFocus()
                self.anim.stop()
                return True
            
            #/------------------------------------------------INV-WEAPON--------------------------------------------------/
            elif(obj == self.ui.inv_tab) and (self.ui.inv_tab.currentIndex() == 0) and (event.key() == 47):
                self.ui.test_list.setFocus()
                self.ui.test_list.setCurrentRow(0)
                return True
            elif(obj == self.ui.test_list) and (event.key() == 47):
                self.ui.test_list.setCurrentRow(-1)
                self.ui.inv_tab.setFocus()
                return True
            
            elif (obj == self.ui.test_list) and (event.key() == 16777236):
                self.ui.test_list.setCurrentRow(self.ui.test_list.currentRow() + 1)
                if(self.ui.test_list.currentRow() == -1):
                    self.ui.test_list.setCurrentRow(0)
                self.ui.test_list.scrollToItem(self.ui.test_list.currentItem())
                
                self.ui.weapon_image.setPixmap(description.pixmapWeaponDict.get(self.ui.test_list.currentRow()))
                
                self.ui.w_damage_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[0])
                self.ui.w_weight_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[1])
                self.ui.w_cost_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[2])
                self.ui.w_durability_PB.setValue(self.random.bounded(20,100))
                self.ui.w_ammo_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[3])
                self.ui.w_effect_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[4])
                
            elif (obj == self.ui.test_list) and (event.key() == 16777234):
                self.ui.test_list.setCurrentRow(self.ui.test_list.currentRow() - 1)
                
                if(self.ui.test_list.currentRow() == -1):
                    self.ui.test_list.setCurrentRow(0)
                    
                self.ui.test_list.scrollToItem(self.ui.test_list.currentItem())
                
                self.ui.weapon_image.setPixmap(description.pixmapWeaponDict.get(self.ui.test_list.currentRow()))
                
                self.ui.w_damage_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[0])
                self.ui.w_weight_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[1])
                self.ui.w_cost_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[2])
                self.ui.w_durability_PB.setValue(self.random.bounded(20,100))
                self.ui.w_ammo_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[3])
                self.ui.w_effect_label.setText(description.weaponDescriptionDict.get(self.ui.test_list.currentRow())[4])
                
            #/------------------------------------------------INV-APPAREL--------------------------------------------------/
            elif(obj == self.ui.inv_tab) and (self.ui.inv_tab.currentIndex() == 1) and (event.key() == 47):
                self.ui.apparel_list.setFocus()
                self.ui.apparel_list.setCurrentRow(0)
                return True
            elif(obj == self.ui.apparel_list) and (event.key() == 47):
                self.ui.apparel_list.setCurrentRow(-1)
                self.ui.inv_tab.setFocus()
                return True
            
            elif (obj == self.ui.apparel_list) and (event.key() == 16777236):
                self.ui.apparel_list.setCurrentRow(self.ui.apparel_list.currentRow() + 1)
                if(self.ui.apparel_list.currentRow() == -1):
                    self.ui.apparel_list.setCurrentRow(0)
                self.ui.apparel_list.scrollToItem(self.ui.apparel_list.currentItem())
                
                self.ui.apparel_image.setPixmap(description.pixmapClothesDict.get(self.ui.apparel_list.currentRow()))
                
                self.ui.a_damage_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[0])
                self.ui.a_weight_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[1])
                self.ui.a_cost_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[2])
                self.ui.a_durability_PB.setValue(self.random.bounded(0,100))
                self.ui.a_type_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[3])
                self.ui.a_effect_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[4])
                
            elif (obj == self.ui.apparel_list) and (event.key() == 16777234):
                self.ui.apparel_list.setCurrentRow(self.ui.apparel_list.currentRow() - 1)
                
                if(self.ui.apparel_list.currentRow() == -1):
                    self.ui.apparel_list.setCurrentRow(0)
                    
                self.ui.apparel_list.scrollToItem(self.ui.apparel_list.currentItem())
                
                self.ui.apparel_image.setPixmap(description.pixmapClothesDict.get(self.ui.apparel_list.currentRow()))
                
                self.ui.a_damage_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[0])
                self.ui.a_weight_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[1])
                self.ui.a_cost_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[2])
                self.ui.a_durability_PB.setValue(self.random.bounded(0,100))
                self.ui.a_type_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[3])
                self.ui.a_effect_label.setText(description.clothesDescriptionDict.get(self.ui.apparel_list.currentRow())[4])
                
            #/------------------------------------------------INV-AID--------------------------------------------------/
            elif(obj == self.ui.inv_tab) and (self.ui.inv_tab.currentIndex() == 2) and (event.key() == 47):
                self.ui.aid_list.setFocus()
                self.ui.aid_list.setCurrentRow(0)
                return True
            elif(obj == self.ui.aid_list) and (event.key() == 47):
                self.ui.aid_list.setCurrentRow(-1)
                self.ui.inv_tab.setFocus()
                return True
            
            elif (obj == self.ui.aid_list) and (event.key() == 16777236):
                self.ui.aid_list.setCurrentRow(self.ui.aid_list.currentRow() + 1)
                if(self.ui.aid_list.currentRow() == -1):
                    self.ui.aid_list.setCurrentRow(0)
                self.ui.aid_list.scrollToItem(self.ui.aid_list.currentItem())
                
                self.ui.aid_image.setPixmap(description.pixmapAidDict.get(self.ui.aid_list.currentRow()))
                
                self.ui.aid_weight_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[0])
                self.ui.aid_cost_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[1])
                self.ui.aid_effect_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[2])
                
                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            elif (obj == self.ui.aid_list) and (event.key() == 16777234):
                self.ui.aid_list.setCurrentRow(self.ui.aid_list.currentRow() - 1)
                
                if(self.ui.aid_list.currentRow() == -1):
                    self.ui.aid_list.setCurrentRow(0)
                    
                self.ui.aid_list.scrollToItem(self.ui.aid_list.currentItem())
                
                self.ui.aid_image.setPixmap(description.pixmapAidDict.get(self.ui.aid_list.currentRow()))
                
                self.ui.aid_weight_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[0])
                self.ui.aid_cost_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[1])
                self.ui.aid_effect_label.setText(description.aidDescriptionDict.get(self.ui.aid_list.currentRow())[2])
                
                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            #/------------------------------------------------INV-AMMO--------------------------------------------------/
            elif(obj == self.ui.inv_tab) and (self.ui.inv_tab.currentIndex() == 3) and (event.key() == 47):
                self.ui.ammo_list.setFocus()
                self.ui.ammo_list.setCurrentRow(0)
                return True
            elif(obj == self.ui.ammo_list) and (event.key() == 47):
                self.ui.ammo_list.setCurrentRow(-1)
                self.ui.inv_tab.setFocus()
                return True
            
            elif (obj == self.ui.ammo_list) and (event.key() == 16777236):
                self.ui.ammo_list.setCurrentRow(self.ui.ammo_list.currentRow() + 1)
                if(self.ui.ammo_list.currentRow() == -1):
                    self.ui.ammo_list.setCurrentRow(0)
                self.ui.ammo_list.scrollToItem(self.ui.ammo_list.currentItem())
                
                self.ui.ammo_image.setPixmap(description.pixmapAmmoDict.get(self.ui.ammo_list.currentRow()))
                
                self.ui.ammo_weight_label.setText(description.ammoDescriptionDict.get(self.ui.ammo_list.currentRow())[0])
                self.ui.ammo_cost_label.setText(description.ammoDescriptionDict.get(self.ui.ammo_list.currentRow())[1])
                
            elif (obj == self.ui.ammo_list) and (event.key() == 16777234):
                self.ui.ammo_list.setCurrentRow(self.ui.ammo_list.currentRow() - 1)
                
                if(self.ui.ammo_list.currentRow() == -1):
                    self.ui.ammo_list.setCurrentRow(0)
                    
                self.ui.ammo_list.scrollToItem(self.ui.ammo_list.currentItem())
                
                self.ui.ammo_image.setPixmap(description.pixmapAmmoDict.get(self.ui.ammo_list.currentRow()))
                
                self.ui.ammo_weight_label.setText(description.ammoDescriptionDict.get(self.ui.ammo_list.currentRow())[0])
                self.ui.ammo_cost_label.setText(description.ammoDescriptionDict.get(self.ui.ammo_list.currentRow())[1])
                
            #/------------------------------------------------DATA--------------------------------------------------/
            elif (obj == self.ui.data_list) and (event.key() == 16777236):
                self.ui.data_list.setCurrentRow(self.ui.data_list.currentRow() + 1)
                
                if(self.ui.data_list.currentRow() == -1):
                    self.ui.data_list.setCurrentRow(0)
                    
                self.ui.data_list.scrollToItem(self.ui.data_list.currentItem())
                
                self.ui.data_description.setText(description.questDescriptionDict.get(self.ui.data_list.currentRow()))

                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            elif (obj == self.ui.data_list) and (event.key() == 16777234):
                self.ui.data_list.setCurrentRow(self.ui.data_list.currentRow() - 1)
                
                if(self.ui.data_list.currentRow() == -1):
                    self.ui.data_list.setCurrentRow(0)
                    
                self.ui.data_list.scrollToItem(self.ui.data_list.currentItem())

                self.ui.data_description.setText(description.questDescriptionDict.get(self.ui.data_list.currentRow()))
                
                self.anim.stop()
                self.anim.setCurrentTime(0)
                self.anim.start()
            
            #/------------------------------------------------RADIO--------------------------------------------------/
            elif (obj == self.ui.radio_list) and (event.key() == 16777236):
                self.ui.radio_list.setCurrentRow(self.ui.radio_list.currentRow() + 1)
                
                if(self.ui.radio_list.currentRow() == -1):
                    self.ui.radio_list.setCurrentRow(0)
                
            elif (obj == self.ui.radio_list) and (event.key() == 16777234):
                self.ui.radio_list.setCurrentRow(self.ui.radio_list.currentRow() - 1)
                
                if(self.ui.radio_list.currentRow() == -1):
                    self.ui.radio_list.setCurrentRow(0)

                #self.ui.data_description.setText(description.questDescriptionDict.get(self.ui.radio_list.currentRow()))
            elif(obj == self.ui.radio_list) and (event.key() == 47):
                if self.play:
                    self.player.stop()
                    self.play = False
                else:
                    self.player.setPlaylist(self.playlistDict.get(self.ui.radio_list.currentRow()))
                    self.playListMohaveMusic.setCurrentIndex(self.random.bounded(0,9) + 1)
                    self.playlisNewVegas.setCurrentIndex(self.random.bounded(0,10) + 1)
                    
                    self.player.play()
                    self.play = True
                return True
            else:
                #print(event.key())
                return True
        
        return super(MainWindow, self).eventFilter(obj, event)

    @Slot()
    def shift(self):
        print(self.ui.stat_tab.currentIndex())
        
        index = self.ui.stat_tab.currentIndex()
        if index == 0:
            self.ui.stat_tab.setGeometry(0,0,904,380)
        elif index == 1:
            self.ui.stat_tab.setGeometry(-108,0,904,380)
        elif index == 2:
            self.ui.stat_tab.setGeometry(-214,0,904,380)

def create_data():
    i = 1
    while True:
        i += 1
        yield (
            i,
            random.uniform(0, 100)
        )
        
        
class Producer(QObject):
    dataChanged = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.iter = create_data()
        QTimer.singleShot(100, self.send_data)

    def send_data(self):
        d = list(next(self.iter))
        self.dataChanged.emit(d)
        QTimer.singleShot(100, self.send_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.installEventFilter(window)
    window.show()
    
    p = Producer()
    p.dataChanged.connect(window.append_data_and_plot)

    
    
    sys.exit(app.exec_())