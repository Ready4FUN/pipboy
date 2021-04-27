# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import image_rc

class Ui_pipboy(object):
    def setupUi(self, pipboy):
        if not pipboy.objectName():
            pipboy.setObjectName(u"pipboy")
        pipboy.setEnabled(True)
        pipboy.resize(720, 478)
        font = QFont()
        font.setFamily(u"Monofonto")
        font.setPointSize(19)
        pipboy.setFont(font)
        pipboy.setStyleSheet(u"QWidget {\n"
"	color: #77fb51;\n"
"	background: black;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"	border: none;\n"
"}\n"
"\n"
"/* \u043e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c, \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0434\u0440\u0443\u0433\u0438\u0445 tab-bar*/\n"
"QTabBar::tab {\n"
"    \n"
"	border-bottom: 1px solid  #77fb51;\n"
"	background: black;\n"
"\n"
"  	min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 16px 10px 2px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-image: url(:/tab_border/image/tab_border.png);\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"/* main_ tab */\n"
"QTabWidget#main_tab{\n"
"\n"
"}\n"
"QTabWidget::pane#main_tab {\n"
"    border-top: 1px solid #77fb51;\n"
"    background: black;\n"
"	top: -1px;\n"
"}\n"
"\n"
""
                        "QTabWidget::tab-bar#main_tab {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* stat_tab, inv_tab */\n"
"QTabWidget::pane#stat_tab, QTabWidget::pane#inv_tab {\n"
"   \n"
"    background: black;\n"
"	top: -1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar#stat_tab, QTabWidget::tab-bar#inv_tab {\n"
"   left: 63px;\n"
"}\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* footer */\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #77fb51;\n"
"	background: #15350d;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #77fb51;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QLabel#hp, QLabel#level, QLabel#ap, QLabel#weight, QLabel#cup, QLabel#inv_space, QLabel#weight_img, QLabel#cup_img, QLabel#data_footer, QLabel#map_footer{\n"
"\n"
"	background: #15350d;\n"
"	margin: 1px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"/*-----------------------------------------------------*/\n"
"/* stimpak and radaway label */\n"
"\n"
"QLabel#stimpak, QLabel#radaway{\n"
""
                        "	color: 2e5017;\n"
"	background: #437520;\n"
"	padding: 0px 1px 1px 0px;\n"
"\n"
"}\n"
"\n"
"/* QListWidget */\n"
"QListView:focus {\n"
"   border: none;\n"
"   outline: none;\n"
"}\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* list */\n"
"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"	border: 0px;\n"
"    padding: 7px 0px 6px 20px;\n"
"	\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"	color:  #183a0f;\n"
"	background: #77fb51;\n"
"}\n"
"\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* special_description */\n"
"\n"
"QLabel#special_description{\n"
"	 padding: 0px 0px 12px 0px;\n"
"\n"
"}\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* perk_description */\n"
"QTextEdit#perks_description{\n"
"	border: none;\n"
"}\n"
"/*-----------------------------------------------------*/\n"
"\n"
"/* item label*/\n"
"QLabel#w_damage_label, QLabel#w_weight_label, QLabel#w_cost_label, QLabel#w_durability_label,  QLabel#w_ammo_l"
                        "abel, QLabel#w_effect_label, QLabel#a_damage_label, QLabel#a_weight_label, QLabel#a_cost_label, QLabel#a_durability_label,  QLabel#a_type_label, QLabel#a_effect_labe l, QLabel#aid_weight_label, QLabel#aid_cost_label, QTextBrowser#aid_effect_label, QLabel#ammo_weight_label, QLabel#ammo_cost_label{\n"
"	border-top: 1px solid #77fb51;\n"
"	border-right: 1px solid #77fb51;\n"
"	margin: 5px 0px 0px 0px;\n"
"\n"
"}\n"
"\n"
"QLabel#w_effect_label {\n"
"	padding-top: -7px; \n"
"}\n"
"/*-----------------------------------------------------*/")
        self.main_tab = QTabWidget(pipboy)
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setGeometry(QRect(10, 0, 700, 480))
        font1 = QFont()
        font1.setFamily(u"Roboto Mono")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.main_tab.setFont(font1)
        self.main_tab.setFocusPolicy(Qt.NoFocus)
        self.main_tab.setLayoutDirection(Qt.LeftToRight)
        self.main_tab.setAutoFillBackground(False)
        self.main_tab.setStyleSheet(u"")
        self.main_tab.setTabPosition(QTabWidget.North)
        self.main_tab.setTabShape(QTabWidget.Rounded)
        self.main_tab.setIconSize(QSize(16, 16))
        self.main_tab.setTabsClosable(False)
        self.main_tab.setMovable(False)
        self.main_tab.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.main_tab.addTab(self.tab_2, "")
        self.stat = QWidget()
        self.stat.setObjectName(u"stat")
        self.stat.setEnabled(True)
        self.stat.setLayoutDirection(Qt.LeftToRight)
        self.stat.setStyleSheet(u"")
        self.stat_tab = QTabWidget(self.stat)
        self.stat_tab.setObjectName(u"stat_tab")
        self.stat_tab.setGeometry(QRect(0, 0, 904, 381))
        font2 = QFont()
        font2.setFamily(u"Roboto Mono Medium")
        font2.setPointSize(17)
        self.stat_tab.setFont(font2)
        self.stat_tab.setFocusPolicy(Qt.NoFocus)
        self.stat_tab.setStyleSheet(u"QTabBar::tab {\n"
"    color: #77fb51;\n"
"	background: black;\n"
"\n"
"  	min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 2px 10px 1px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-image: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	color: rgba(119,251,81, 90);\n"
"	border: none;\n"
"}\n"
"")
        self.status = QWidget()
        self.status.setObjectName(u"status")
        self.main_img = QLabel(self.status)
        self.main_img.setObjectName(u"main_img")
        self.main_img.setGeometry(QRect(230, 30, 240, 251))
        self.stimpak = QLabel(self.status)
        self.stimpak.setObjectName(u"stimpak")
        self.stimpak.setGeometry(QRect(0, 320, 105, 29))
        font3 = QFont()
        font3.setFamily(u"Roboto Mono")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.stimpak.setFont(font3)
        self.radaway = QLabel(self.status)
        self.radaway.setObjectName(u"radaway")
        self.radaway.setGeometry(QRect(120, 320, 105, 29))
        self.radaway.setFont(font3)
        self.name = QLabel(self.status)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(315, 290, 71, 21))
        font4 = QFont()
        font4.setFamily(u"Roboto Mono")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.name.setFont(font4)
        self.head_bar = QProgressBar(self.status)
        self.head_bar.setObjectName(u"head_bar")
        self.head_bar.setGeometry(QRect(330, 10, 50, 12))
        self.head_bar.setValue(57)
        self.hp_right_arm = QProgressBar(self.status)
        self.hp_right_arm.setObjectName(u"hp_right_arm")
        self.hp_right_arm.setGeometry(QRect(440, 75, 50, 12))
        self.hp_right_arm.setValue(100)
        self.hp_left_arm = QProgressBar(self.status)
        self.hp_left_arm.setObjectName(u"hp_left_arm")
        self.hp_left_arm.setGeometry(QRect(215, 75, 50, 12))
        self.hp_left_arm.setValue(100)
        self.hp_body = QProgressBar(self.status)
        self.hp_body.setObjectName(u"hp_body")
        self.hp_body.setGeometry(QRect(330, 125, 50, 12))
        self.hp_body.setValue(100)
        self.hp_right_leg = QProgressBar(self.status)
        self.hp_right_leg.setObjectName(u"hp_right_leg")
        self.hp_right_leg.setGeometry(QRect(430, 220, 50, 12))
        self.hp_right_leg.setValue(100)
        self.hp_left_leg = QProgressBar(self.status)
        self.hp_left_leg.setObjectName(u"hp_left_leg")
        self.hp_left_leg.setGeometry(QRect(225, 220, 50, 12))
        self.hp_left_leg.setValue(100)
        self.stat_tab.addTab(self.status, "")
        self.special = QWidget()
        self.special.setObjectName(u"special")
        self.special_list = QListWidget(self.special)
        __qlistwidgetitem = QListWidgetItem(self.special_list)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.special_list)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        QListWidgetItem(self.special_list)
        QListWidgetItem(self.special_list)
        QListWidgetItem(self.special_list)
        QListWidgetItem(self.special_list)
        QListWidgetItem(self.special_list)
        self.special_list.setObjectName(u"special_list")
        self.special_list.setGeometry(QRect(108, 20, 345, 307))
        font5 = QFont()
        font5.setFamily(u"Roboto Mono")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.special_list.setFont(font5)
        self.special_list.setFocusPolicy(Qt.NoFocus)
        self.special_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.special_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.special_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.special_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.special_list.setAutoScroll(False)
        self.special_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.special_list.setProperty("showDropIndicator", False)
        self.special_list.setFlow(QListView.TopToBottom)
        self.special_list.setSelectionRectVisible(False)
        self.special_image = QLabel(self.special)
        self.special_image.setObjectName(u"special_image")
        self.special_image.setGeometry(QRect(468, 20, 331, 171))
        self.special_image.setAlignment(Qt.AlignCenter)
        self.special_description = QLabel(self.special)
        self.special_description.setObjectName(u"special_description")
        self.special_description.setGeometry(QRect(468, 191, 331, 136))
        font6 = QFont()
        font6.setFamily(u"Roboto Mono Medium")
        font6.setPointSize(12)
        self.special_description.setFont(font6)
        self.special_description.setTextFormat(Qt.AutoText)
        self.special_description.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.special_description.setWordWrap(True)
        self.stat_tab.addTab(self.special, "")
        self.perks = QWidget()
        self.perks.setObjectName(u"perks")
        self.perks_list = QListWidget(self.perks)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        QListWidgetItem(self.perks_list)
        self.perks_list.setObjectName(u"perks_list")
        self.perks_list.setGeometry(QRect(214, 20, 345, 307))
        self.perks_list.setFont(font5)
        self.perks_list.setFocusPolicy(Qt.NoFocus)
        self.perks_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.perks_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.perks_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.perks_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.perks_list.setAutoScroll(False)
        self.perks_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.perks_list.setProperty("showDropIndicator", False)
        self.perks_list.setFlow(QListView.TopToBottom)
        self.perks_list.setSelectionRectVisible(False)
        self.perks_image = QLabel(self.perks)
        self.perks_image.setObjectName(u"perks_image")
        self.perks_image.setGeometry(QRect(574, 20, 331, 171))
        self.perks_image.setAlignment(Qt.AlignCenter)
        self.perks_description = QTextEdit(self.perks)
        self.perks_description.setObjectName(u"perks_description")
        self.perks_description.setGeometry(QRect(574, 191, 331, 136))
        font7 = QFont()
        font7.setFamily(u"Roboto Mono Medium")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setWeight(50)
        self.perks_description.setFont(font7)
        self.perks_description.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.perks_description.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.perks_description.setReadOnly(True)
        self.stat_tab.addTab(self.perks, "")
        self.hp = QLabel(self.stat)
        self.hp.setObjectName(u"hp")
        self.hp.setGeometry(QRect(0, 386, 172, 32))
        self.hp.setFont(font4)
        self.hp.setFrameShape(QFrame.NoFrame)
        self.level = QLabel(self.stat)
        self.level.setObjectName(u"level")
        self.level.setGeometry(QRect(177, 386, 340, 32))
        self.level.setFont(font4)
        self.ap = QLabel(self.stat)
        self.ap.setObjectName(u"ap")
        self.ap.setGeometry(QRect(522, 386, 170, 32))
        self.ap.setFont(font4)
        self.ap.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.level_bar = QProgressBar(self.stat)
        self.level_bar.setObjectName(u"level_bar")
        self.level_bar.setGeometry(QRect(280, 396, 233, 13))
        font8 = QFont()
        font8.setFamily(u"Roboto Mono")
        self.level_bar.setFont(font8)
        self.level_bar.setValue(2)
        self.level_bar.setTextVisible(False)
        self.main_tab.addTab(self.stat, "")
        self.inv = QWidget()
        self.inv.setObjectName(u"inv")
        self.inv_tab = QTabWidget(self.inv)
        self.inv_tab.setObjectName(u"inv_tab")
        self.inv_tab.setGeometry(QRect(0, 0, 700, 381))
        self.inv_tab.setFont(font2)
        self.inv_tab.setFocusPolicy(Qt.NoFocus)
        self.inv_tab.setStyleSheet(u"QTabBar::tab {\n"
"    color: #77fb51;\n"
"	background: black;\n"
"\n"
"  	min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 2px 10px 1px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-image: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	color: rgba(119,251,81, 90);\n"
"	border: none;\n"
"}\n"
"")
        self.weapon = QWidget()
        self.weapon.setObjectName(u"weapon")
        self.test_list = QListWidget(self.weapon)
        QListWidgetItem(self.test_list)
        QListWidgetItem(self.test_list)
        QListWidgetItem(self.test_list)
        QListWidgetItem(self.test_list)
        QListWidgetItem(self.test_list)
        self.test_list.setObjectName(u"test_list")
        self.test_list.setGeometry(QRect(0, 20, 345, 307))
        font9 = QFont()
        font9.setFamily(u"Roboto Mono")
        font9.setPointSize(16)
        font9.setBold(False)
        font9.setWeight(50)
        self.test_list.setFont(font9)
        self.test_list.setFocusPolicy(Qt.NoFocus)
        self.test_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.test_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.test_list.setAutoScroll(False)
        self.test_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.test_list.setProperty("showDropIndicator", False)
        self.test_list.setFlow(QListView.TopToBottom)
        self.test_list.setSelectionRectVisible(False)
        self.weapon_image = QLabel(self.weapon)
        self.weapon_image.setObjectName(u"weapon_image")
        self.weapon_image.setGeometry(QRect(360, 20, 331, 151))
        self.weapon_image.setAlignment(Qt.AlignCenter)
        self.w_damage_label = QLabel(self.weapon)
        self.w_damage_label.setObjectName(u"w_damage_label")
        self.w_damage_label.setGeometry(QRect(360, 181, 107, 38))
        font10 = QFont()
        font10.setFamily(u"Roboto Mono")
        font10.setPointSize(14)
        self.w_damage_label.setFont(font10)
        self.w_weight_label = QLabel(self.weapon)
        self.w_weight_label.setObjectName(u"w_weight_label")
        self.w_weight_label.setGeometry(QRect(472, 181, 107, 38))
        self.w_weight_label.setFont(font10)
        self.w_cost_label = QLabel(self.weapon)
        self.w_cost_label.setObjectName(u"w_cost_label")
        self.w_cost_label.setGeometry(QRect(584, 181, 107, 38))
        self.w_cost_label.setFont(font10)
        self.w_durability_label = QLabel(self.weapon)
        self.w_durability_label.setObjectName(u"w_durability_label")
        self.w_durability_label.setGeometry(QRect(360, 224, 107, 38))
        self.w_durability_label.setFont(font10)
        self.w_durability_PB = QProgressBar(self.weapon)
        self.w_durability_PB.setObjectName(u"w_durability_PB")
        self.w_durability_PB.setGeometry(QRect(402, 242, 59, 12))
        self.w_durability_PB.setValue(96)
        self.w_durability_PB.setTextVisible(False)
        self.w_ammo_label = QLabel(self.weapon)
        self.w_ammo_label.setObjectName(u"w_ammo_label")
        self.w_ammo_label.setGeometry(QRect(472, 224, 219, 38))
        self.w_ammo_label.setFont(font10)
        self.w_effect_label = QLabel(self.weapon)
        self.w_effect_label.setObjectName(u"w_effect_label")
        self.w_effect_label.setGeometry(QRect(360, 267, 331, 61))
        self.w_effect_label.setFont(font10)
        self.w_effect_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.w_effect_label.setWordWrap(True)
        self.inv_tab.addTab(self.weapon, "")
        self.apparel = QWidget()
        self.apparel.setObjectName(u"apparel")
        self.apparel_list = QListWidget(self.apparel)
        QListWidgetItem(self.apparel_list)
        QListWidgetItem(self.apparel_list)
        QListWidgetItem(self.apparel_list)
        self.apparel_list.setObjectName(u"apparel_list")
        self.apparel_list.setGeometry(QRect(0, 20, 345, 307))
        self.apparel_list.setFont(font9)
        self.apparel_list.setFocusPolicy(Qt.TabFocus)
        self.apparel_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.apparel_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.apparel_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.apparel_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.apparel_list.setAutoScroll(False)
        self.apparel_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.apparel_list.setProperty("showDropIndicator", False)
        self.apparel_list.setFlow(QListView.TopToBottom)
        self.apparel_list.setProperty("isWrapping", True)
        self.apparel_list.setWordWrap(True)
        self.apparel_list.setSelectionRectVisible(False)
        self.apparel_list.setSortingEnabled(False)
        self.apparel_image = QLabel(self.apparel)
        self.apparel_image.setObjectName(u"apparel_image")
        self.apparel_image.setGeometry(QRect(360, 20, 331, 151))
        self.apparel_image.setAlignment(Qt.AlignCenter)
        self.a_damage_label = QLabel(self.apparel)
        self.a_damage_label.setObjectName(u"a_damage_label")
        self.a_damage_label.setGeometry(QRect(360, 181, 107, 38))
        self.a_damage_label.setFont(font10)
        self.a_weight_label = QLabel(self.apparel)
        self.a_weight_label.setObjectName(u"a_weight_label")
        self.a_weight_label.setGeometry(QRect(472, 181, 107, 38))
        self.a_weight_label.setFont(font10)
        self.a_cost_label = QLabel(self.apparel)
        self.a_cost_label.setObjectName(u"a_cost_label")
        self.a_cost_label.setGeometry(QRect(584, 181, 107, 38))
        self.a_cost_label.setFont(font10)
        self.a_durability_label = QLabel(self.apparel)
        self.a_durability_label.setObjectName(u"a_durability_label")
        self.a_durability_label.setGeometry(QRect(360, 224, 107, 38))
        self.a_durability_label.setFont(font10)
        self.a_durability_PB = QProgressBar(self.apparel)
        self.a_durability_PB.setObjectName(u"a_durability_PB")
        self.a_durability_PB.setGeometry(QRect(402, 242, 59, 12))
        self.a_durability_PB.setValue(96)
        self.a_durability_PB.setTextVisible(False)
        self.a_type_label = QLabel(self.apparel)
        self.a_type_label.setObjectName(u"a_type_label")
        self.a_type_label.setGeometry(QRect(472, 224, 219, 38))
        self.a_type_label.setFont(font10)
        self.a_effect_label = QLabel(self.apparel)
        self.a_effect_label.setObjectName(u"a_effect_label")
        self.a_effect_label.setGeometry(QRect(360, 267, 331, 61))
        self.a_effect_label.setFont(font10)
        self.a_effect_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.a_effect_label.setWordWrap(True)
        self.inv_tab.addTab(self.apparel, "")
        self.aid = QWidget()
        self.aid.setObjectName(u"aid")
        self.aid_list = QListWidget(self.aid)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        QListWidgetItem(self.aid_list)
        self.aid_list.setObjectName(u"aid_list")
        self.aid_list.setGeometry(QRect(0, 20, 345, 307))
        self.aid_list.setFont(font9)
        self.aid_list.setFocusPolicy(Qt.TabFocus)
        self.aid_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aid_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.aid_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.aid_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.aid_list.setAutoScroll(False)
        self.aid_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.aid_list.setProperty("showDropIndicator", False)
        self.aid_list.setFlow(QListView.TopToBottom)
        self.aid_list.setProperty("isWrapping", True)
        self.aid_list.setWordWrap(True)
        self.aid_list.setSelectionRectVisible(False)
        self.aid_list.setSortingEnabled(False)
        self.aid_image = QLabel(self.aid)
        self.aid_image.setObjectName(u"aid_image")
        self.aid_image.setGeometry(QRect(360, 20, 331, 151))
        self.aid_image.setAlignment(Qt.AlignCenter)
        self.aid_cost_label = QLabel(self.aid)
        self.aid_cost_label.setObjectName(u"aid_cost_label")
        self.aid_cost_label.setGeometry(QRect(584, 181, 107, 38))
        self.aid_cost_label.setFont(font10)
        self.aid_weight_label = QLabel(self.aid)
        self.aid_weight_label.setObjectName(u"aid_weight_label")
        self.aid_weight_label.setGeometry(QRect(472, 181, 107, 38))
        self.aid_weight_label.setFont(font10)
        self.aid_effect_label = QTextBrowser(self.aid)
        self.aid_effect_label.setObjectName(u"aid_effect_label")
        self.aid_effect_label.setGeometry(QRect(360, 224, 331, 103))
        self.aid_effect_label.setFont(font10)
        self.aid_effect_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.aid_effect_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inv_tab.addTab(self.aid, "")
        self.ammo = QWidget()
        self.ammo.setObjectName(u"ammo")
        self.ammo_list = QListWidget(self.ammo)
        QListWidgetItem(self.ammo_list)
        QListWidgetItem(self.ammo_list)
        QListWidgetItem(self.ammo_list)
        self.ammo_list.setObjectName(u"ammo_list")
        self.ammo_list.setGeometry(QRect(0, 20, 345, 307))
        self.ammo_list.setFont(font9)
        self.ammo_list.setFocusPolicy(Qt.TabFocus)
        self.ammo_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ammo_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ammo_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ammo_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.ammo_list.setAutoScroll(False)
        self.ammo_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ammo_list.setProperty("showDropIndicator", False)
        self.ammo_list.setFlow(QListView.TopToBottom)
        self.ammo_list.setProperty("isWrapping", True)
        self.ammo_list.setWordWrap(True)
        self.ammo_list.setSelectionRectVisible(False)
        self.ammo_list.setSortingEnabled(False)
        self.ammo_image = QLabel(self.ammo)
        self.ammo_image.setObjectName(u"ammo_image")
        self.ammo_image.setGeometry(QRect(360, 20, 331, 151))
        self.ammo_image.setAlignment(Qt.AlignCenter)
        self.ammo_weight_label = QLabel(self.ammo)
        self.ammo_weight_label.setObjectName(u"ammo_weight_label")
        self.ammo_weight_label.setGeometry(QRect(472, 181, 107, 38))
        self.ammo_weight_label.setFont(font10)
        self.ammo_cost_label = QLabel(self.ammo)
        self.ammo_cost_label.setObjectName(u"ammo_cost_label")
        self.ammo_cost_label.setGeometry(QRect(584, 181, 107, 38))
        self.ammo_cost_label.setFont(font10)
        self.inv_tab.addTab(self.ammo, "")
        self.weight = QLabel(self.inv)
        self.weight.setObjectName(u"weight")
        self.weight.setGeometry(QRect(25, 386, 115, 32))
        self.weight.setFont(font4)
        self.weight.setFrameShape(QFrame.NoFrame)
        self.weight_img = QLabel(self.inv)
        self.weight_img.setObjectName(u"weight_img")
        self.weight_img.setGeometry(QRect(0, 386, 31, 32))
        self.weight_img.setFont(font4)
        self.weight_img.setFrameShape(QFrame.NoFrame)
        self.cup_img = QLabel(self.inv)
        self.cup_img.setObjectName(u"cup_img")
        self.cup_img.setGeometry(QRect(145, 386, 31, 32))
        self.cup_img.setFont(font4)
        self.cup_img.setFrameShape(QFrame.NoFrame)
        self.cup = QLabel(self.inv)
        self.cup.setObjectName(u"cup")
        self.cup.setGeometry(QRect(175, 386, 120, 32))
        self.cup.setFont(font4)
        self.cup.setFrameShape(QFrame.NoFrame)
        self.inv_space = QLabel(self.inv)
        self.inv_space.setObjectName(u"inv_space")
        self.inv_space.setGeometry(QRect(300, 386, 401, 32))
        self.inv_space.setFont(font4)
        self.inv_space.setFrameShape(QFrame.NoFrame)
        self.main_tab.addTab(self.inv, "")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.data_footer = QLabel(self.data)
        self.data_footer.setObjectName(u"data_footer")
        self.data_footer.setGeometry(QRect(0, 386, 700, 32))
        self.data_footer.setFont(font4)
        self.data_footer.setFrameShape(QFrame.NoFrame)
        self.data_list = QListWidget(self.data)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        QListWidgetItem(self.data_list)
        self.data_list.setObjectName(u"data_list")
        self.data_list.setGeometry(QRect(0, 20, 345, 357))
        self.data_list.setFont(font9)
        self.data_list.setFocusPolicy(Qt.TabFocus)
        self.data_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.data_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.data_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.data_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.data_list.setAutoScroll(False)
        self.data_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_list.setProperty("showDropIndicator", False)
        self.data_list.setFlow(QListView.TopToBottom)
        self.data_list.setProperty("isWrapping", False)
        self.data_list.setWordWrap(True)
        self.data_list.setSelectionRectVisible(False)
        self.data_list.setSortingEnabled(False)
        self.data_description = QTextBrowser(self.data)
        self.data_description.setObjectName(u"data_description")
        self.data_description.setGeometry(QRect(360, 20, 331, 357))
        font11 = QFont()
        font11.setFamily(u"Roboto Mono")
        font11.setPointSize(16)
        self.data_description.setFont(font11)
        self.data_description.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.data_description.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_tab.addTab(self.data, "")
        self.map = QWidget()
        self.map.setObjectName(u"map")
        self.map_image = QLabel(self.map)
        self.map_image.setObjectName(u"map_image")
        self.map_image.setGeometry(QRect(0, 20, 700, 389))
        self.main_tab.addTab(self.map, "")
        self.radio = QWidget()
        self.radio.setObjectName(u"radio")
        self.radio.setLayoutDirection(Qt.LeftToRight)
        self.radio_list = QListWidget(self.radio)
        QListWidgetItem(self.radio_list)
        QListWidgetItem(self.radio_list)
        QListWidgetItem(self.radio_list)
        self.radio_list.setObjectName(u"radio_list")
        self.radio_list.setGeometry(QRect(0, 20, 345, 357))
        self.radio_list.setFont(font9)
        self.radio_list.setFocusPolicy(Qt.TabFocus)
        self.radio_list.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.radio_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.radio_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.radio_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.radio_list.setAutoScroll(False)
        self.radio_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.radio_list.setProperty("showDropIndicator", False)
        self.radio_list.setFlow(QListView.TopToBottom)
        self.radio_list.setProperty("isWrapping", True)
        self.radio_list.setWordWrap(True)
        self.radio_list.setSelectionRectVisible(False)
        self.radio_list.setSortingEnabled(False)
        self.map_footer = QLabel(self.radio)
        self.map_footer.setObjectName(u"map_footer")
        self.map_footer.setGeometry(QRect(0, 386, 700, 32))
        self.map_footer.setFont(font4)
        self.map_footer.setFrameShape(QFrame.NoFrame)
        self.chartContainer = QWidget(self.radio)
        self.chartContainer.setObjectName(u"chartContainer")
        self.chartContainer.setGeometry(QRect(360, 20, 331, 171))
        self.main_tab.addTab(self.radio, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.main_tab.addTab(self.tab, "")

        self.retranslateUi(pipboy)

        self.main_tab.setCurrentIndex(1)
        self.stat_tab.setCurrentIndex(0)
        self.special_list.setCurrentRow(-1)
        self.perks_list.setCurrentRow(-1)
        self.inv_tab.setCurrentIndex(0)
        self.test_list.setCurrentRow(-1)
        self.apparel_list.setCurrentRow(-1)
        self.aid_list.setCurrentRow(-1)
        self.ammo_list.setCurrentRow(-1)
        self.data_list.setCurrentRow(-1)
        self.radio_list.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(pipboy)
    # setupUi

    def retranslateUi(self, pipboy):
        pipboy.setWindowTitle(QCoreApplication.translate("pipboy", u"pipboy", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab_2), "")
        self.main_img.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.stimpak.setText(QCoreApplication.translate("pipboy", u"STIMPAK(4)", None))
        self.radaway.setText(QCoreApplication.translate("pipboy", u"RADAWAY(0)", None))
        self.name.setText(QCoreApplication.translate("pipboy", u"boopsy", None))
        self.stat_tab.setTabText(self.stat_tab.indexOf(self.status), QCoreApplication.translate("pipboy", u"STATUS", None))

        __sortingEnabled = self.special_list.isSortingEnabled()
        self.special_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.special_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("pipboy", u"Strength               2", None));
        ___qlistwidgetitem1 = self.special_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("pipboy", u"Perception             6", None));
        ___qlistwidgetitem2 = self.special_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("pipboy", u"Endurance              4", None));
        ___qlistwidgetitem3 = self.special_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("pipboy", u"Charisma              10", None));
        ___qlistwidgetitem4 = self.special_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("pipboy", u"Intelligence           7", None));
        ___qlistwidgetitem5 = self.special_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("pipboy", u"Agility                5", None));
        ___qlistwidgetitem6 = self.special_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("pipboy", u"Luck                   8", None));
        self.special_list.setSortingEnabled(__sortingEnabled)

        self.special_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.special_description.setText(QCoreApplication.translate("pipboy", u"\u0421\u0438\u043b\u0430 \u0440\u0430\u0441\u0441\u043a\u0430\u0436\u0435\u0442 \u0442\u0435\u0431\u0435, \u0441\u043c\u043e\u0436\u0435\u0442 \u043b\u0438 \u043a\u043e\u0432\u0431\u043e\u0439 \u043b\u0435\u0433\u043a\u043e \u0442\u0430\u0449\u0438\u0442\u044c \u0441\u0432\u043e\u0435 \u0441\u0435\u0434\u043b\u043e, \u043d\u0443 \u0438\u043b\u0438 \u0431\u043e\u043b\u044c\u0448\u0438\u0435 \u043f\u0443\u0448\u043a\u0438; \u0430 \u0437\u0430\u043e\u0434\u043d\u043e \u2013 \u043c\u043d\u043e\u0433\u043e \u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u044b \u043e\u0442 \u043d\u0435\u0433\u043e \u043f\u0440\u0438 \u0434\u0440\u0430\u043a\u0435 \u0432 \u0441\u0430\u043b\u0443\u043d\u0435.", None))
        self.stat_tab.setTabText(self.stat_tab.indexOf(self.special), QCoreApplication.translate("pipboy", u"SPECIAL", None))

        __sortingEnabled1 = self.perks_list.isSortingEnabled()
        self.perks_list.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.perks_list.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("pipboy", u"\u041a\u043e\u0432\u0431\u043e\u0439", None));
        ___qlistwidgetitem8 = self.perks_list.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("pipboy", u"\u0427\u0451\u0440\u043d\u0430\u044f \u0432\u0434\u043e\u0432\u0430", None));
        ___qlistwidgetitem9 = self.perks_list.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("pipboy", u"\u0428\u0435\u0440\u0448\u0435 \u043b\u044f \u0444\u0430\u043c", None));
        ___qlistwidgetitem10 = self.perks_list.item(3)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("pipboy", u"\u0414\u0443\u044d\u043b\u0438\u0441\u0442", None));
        ___qlistwidgetitem11 = self.perks_list.item(4)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("pipboy", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b", None));
        ___qlistwidgetitem12 = self.perks_list.item(5)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("pipboy", u"\u0425\u0430\u043b\u044f\u0432\u0449\u0438\u043a", None));
        ___qlistwidgetitem13 = self.perks_list.item(6)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("pipboy", u"\u0422\u0430\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043d\u0435\u0437\u043d\u0430\u043a\u043e\u043c\u0435\u0446", None));
        ___qlistwidgetitem14 = self.perks_list.item(7)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("pipboy", u"\u0421\u043d\u0430\u0439\u043f\u0435\u0440", None));
        ___qlistwidgetitem15 = self.perks_list.item(8)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("pipboy", u"\u0414\u0440\u0443\u0436\u0435\u0441\u043a\u0438\u0435 \u043f\u043e\u0434\u043a\u043e\u043b\u043a\u0438", None));
        ___qlistwidgetitem16 = self.perks_list.item(9)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("pipboy", u"\u041d\u043e\u0447\u043d\u043e\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e", None));
        ___qlistwidgetitem17 = self.perks_list.item(10)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("pipboy", u"\u0414\u0435\u043d\u044c \u043f\u043e\u0434 \u043a\u0430\u0439\u0444\u043e\u043c", None));
        ___qlistwidgetitem18 = self.perks_list.item(11)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("pipboy", u"\u0411\u0435\u0437\u0437\u0430\u0432\u0435\u0442\u043d\u0430\u044f \u043f\u0440\u0435\u0434\u0430\u043d\u043d\u043e\u0441\u0442\u044c", None));
        ___qlistwidgetitem19 = self.perks_list.item(12)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("pipboy", u"\u041a\u043b\u0430\u0434\u043e\u0438\u0441\u043a\u0430\u0442\u0435\u043b\u044c", None));
        ___qlistwidgetitem20 = self.perks_list.item(13)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("pipboy", u"\u0414\u0440\u0443\u0433 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445", None));
        ___qlistwidgetitem21 = self.perks_list.item(14)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("pipboy", u"\u0414\u043e\u043c\u0443\u0448\u043d\u0438\u043a", None));
        ___qlistwidgetitem22 = self.perks_list.item(15)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("pipboy", u"\u0412\u0438\u0441\u043a\u0438 \u0438 \u0440\u043e\u0437\u0430", None));
        ___qlistwidgetitem23 = self.perks_list.item(16)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("pipboy", u"\u041d\u0430\u0432\u043e\u0434\u0447\u0438\u043a", None));
        self.perks_list.setSortingEnabled(__sortingEnabled1)

        self.perks_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.perks_description.setHtml(QCoreApplication.translate("pipboy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto Mono Medium'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b \u043d\u0430\u043d\u043e\u0441\u0438\u0442\u0435 \u043d\u0430 25% \u0431\u043e\u043b\u044c\u0448\u0435 \u0443\u0440\u043e\u043d\u0430, \u0435\u0441\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0435 \u0440\u0435\u0432\u043e\u043b\u044c\u0432\u0435\u0440\u044b, \u0441\u0442\u0440\u0435\u043b\u043a\u043e\u0432\u043e\u0435 \u043e\u0440\u0443\u0436\u0438\u0435 \u0441 \u0440\u044b\u0447\u0430\u0436\u043d\u044b\u043c \u043c\u0435\u0445\u0430\u043d\u0438\u0437\u043c\u043e\u043c \u0437\u0430\u0442\u0432\u043e\u0440\u0430"
                        ", \u0434\u0438\u043d\u0430\u043c\u0438\u0442, \u043d\u043e\u0436\u0438 \u0438\u043b\u0438 \u0442\u043e\u043f\u043e\u0440\u0438\u043a\u0438.</p></body></html>", None))
        self.perks_description.setPlaceholderText(QCoreApplication.translate("pipboy", u"\u0412\u0441\u0435\u043c\u0443 \u043f\u0440\u043e\u0447\u0435\u043c\u0443 \u0432\u044b \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0438\u0442\u0430\u0435\u0442\u0435 \u0431\u043b\u0438\u0437\u043a\u043e\u0435 \u043b\u0438\u0447\u043d\u043e\u0435 \u043e\u0431\u0449\u0435\u043d\u0438\u0435. \u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0443\u0440\u043e\u043d \u043f\u0440\u0438 \u0441\u043a\u0440\u044b\u0442\u043d\u043e\u0439 \u0430\u0442\u0430\u043a\u0435 \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u043e\u0432, \u0440\u0435\u0432\u043e\u043b\u044c\u0432\u0435\u0440\u043e\u0432 \u0438 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u043e\u0432-\u043f\u0443\u043b\u0435\u043c\u0451\u0442\u043e\u0432 (\u043a\u0430\u043a \u043e\u0431\u044b\u0447\u043d\u044b\u0445, \u0442\u0430\u043a \u0438 \u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445) \u0443\u0432\u0435\u043b"
                        "\u0438\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 20 %.", None))
        self.stat_tab.setTabText(self.stat_tab.indexOf(self.perks), QCoreApplication.translate("pipboy", u"PERKS", None))
        self.hp.setText(QCoreApplication.translate("pipboy", u"HP 145/145", None))
        self.level.setText(QCoreApplication.translate("pipboy", u"LEVEL 24", None))
        self.ap.setText(QCoreApplication.translate("pipboy", u"AP 90/90", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.stat), QCoreApplication.translate("pipboy", u"STAT", None))

        __sortingEnabled2 = self.test_list.isSortingEnabled()
        self.test_list.setSortingEnabled(False)
        ___qlistwidgetitem24 = self.test_list.item(0)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("pipboy", u"\u00ab\u041c\u0430\u0433\u043d\u0443\u043c\u00bb \u043a\u0430\u043b. 44", None));
        ___qlistwidgetitem25 = self.test_list.item(1)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("pipboy", u"\u00ab\u0421\u0435\u043a\u0432\u043e\u0439\u044f\u00bb \u0440\u0435\u0439\u043d\u0434\u0436\u0435\u0440\u0430", None));
        ___qlistwidgetitem26 = self.test_list.item(2)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("pipboy", u"\u0421\u043d\u0430\u0439\u043f\u0435\u0440\u0441\u043a\u0430\u044f \u0432\u0438\u043d\u0442\u043e\u0432\u043a\u0430", None));
        ___qlistwidgetitem27 = self.test_list.item(3)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("pipboy", u"\u0411\u043e\u0435\u0432\u043e\u0439 \u043d\u043e\u0436", None));
        ___qlistwidgetitem28 = self.test_list.item(4)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("pipboy", u"\u0412\u044b\u043a\u0438\u0434\u043d\u043e\u0439 \u043d\u043e\u0436", None));
        self.test_list.setSortingEnabled(__sortingEnabled2)

        self.weapon_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.w_damage_label.setText(QCoreApplication.translate("pipboy", u"\u0423\u0420\u041e\u041d 38", None))
        self.w_weight_label.setText(QCoreApplication.translate("pipboy", u"\u0412\u0415\u0421 3.5", None))
        self.w_cost_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0422\u041e 2500", None))
        self.w_durability_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0421\u0422", None))
        self.w_ammo_label.setText(QCoreApplication.translate("pipboy", u".44 \u00ab\u041c\u0430\u0433\u043d\u0443\u043c\u00bb", None))
        self.w_effect_label.setText("")
        self.inv_tab.setTabText(self.inv_tab.indexOf(self.weapon), QCoreApplication.translate("pipboy", u"WEAPON", None))

        __sortingEnabled3 = self.apparel_list.isSortingEnabled()
        self.apparel_list.setSortingEnabled(False)
        ___qlistwidgetitem29 = self.apparel_list.item(0)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("pipboy", u"\u0411\u043e\u0435\u0432\u0430\u044f \u0431\u0440\u043e\u043d\u044f \u0440\u0435\u0439\u043d\u0434\u0436\u0435\u0440\u0430   \u041d\u041a\u0420", None));
        ___qlistwidgetitem30 = self.apparel_list.item(1)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("pipboy", u"\u0428\u043b\u0435\u043c \u0440\u0435\u0439\u043d\u0434\u0436\u0435\u0440\u0430", None));
        ___qlistwidgetitem31 = self.apparel_list.item(2)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("pipboy", u"\u041a\u043e\u0441\u0442\u044e\u043c \u041a\u043e\u0440\u043e\u043b\u044f", None));
        self.apparel_list.setSortingEnabled(__sortingEnabled3)

        self.apparel_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.a_damage_label.setText(QCoreApplication.translate("pipboy", u"\u041f\u0423 20", None))
        self.a_weight_label.setText(QCoreApplication.translate("pipboy", u"\u0412\u0415\u0421 35", None))
        self.a_cost_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0422\u041e 7500", None))
        self.a_durability_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0421\u0422", None))
        self.a_type_label.setText(QCoreApplication.translate("pipboy", u"\u041b\u0435\u0433\u043a\u0430\u044f", None))
        self.a_effect_label.setText(QCoreApplication.translate("pipboy", u"\u042d\u0424\u0424: \u0421\u0442\u0430\u0442\u0443\u0441 \u0433\u0440\u0430\u0436\u0434\u0430\u043d\u0438\u043d\u0430 \u041d\u041a\u0420", None))
        self.inv_tab.setTabText(self.inv_tab.indexOf(self.apparel), QCoreApplication.translate("pipboy", u"APPAREL", None))

        __sortingEnabled4 = self.aid_list.isSortingEnabled()
        self.aid_list.setSortingEnabled(False)
        ___qlistwidgetitem32 = self.aid_list.item(0)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("pipboy", u"\u0411\u0430\u0444\u0444\u0430\u0443\u0442", None));
        ___qlistwidgetitem33 = self.aid_list.item(1)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("pipboy", u"\u0412\u0438\u043d\u0442", None));
        ___qlistwidgetitem34 = self.aid_list.item(2)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("pipboy", u"\u041c\u0435\u043d\u0442\u0430\u0442\u044b", None));
        ___qlistwidgetitem35 = self.aid_list.item(3)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("pipboy", u"\u0421\u0442\u0438\u043c\u0443\u043b\u044f\u0442\u043e\u0440(4)", None));
        ___qlistwidgetitem36 = self.aid_list.item(4)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("pipboy", u"\u0421\u0430\u043d\u0441\u0435\u0442 \u0441\u0430\u0441\u043f\u0430\u0440\u0438\u043b\u043b\u0430", None));
        ___qlistwidgetitem37 = self.aid_list.item(5)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("pipboy", u"\u041b\u0435\u0434\u044f\u043d\u0430\u044f \u044f\u0434\u0435\u0440-\u043a\u043e\u043b\u0430", None));
        ___qlistwidgetitem38 = self.aid_list.item(6)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("pipboy", u"\u0421\u0432\u0435\u0436\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0444\u0435\u043b\u0438\u043d\u0430", None));
        self.aid_list.setSortingEnabled(__sortingEnabled4)

        self.aid_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.aid_cost_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0422\u041e 20", None))
        self.aid_weight_label.setText(QCoreApplication.translate("pipboy", u"\u0412\u0415\u0421 0", None))
        self.aid_effect_label.setHtml(QCoreApplication.translate("pipboy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto Mono'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042d\u0424\u0424: \u041e\u0447\u043a\u0438 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u044f: +60; \u0421\u0438\u043b\u0430: +2; \u0412\u044b\u043d\u043e\u0441\u043b\u0438\u0432\u043e\u0441\u0442\u044c: +3</p></body></html>", None))
        self.inv_tab.setTabText(self.inv_tab.indexOf(self.aid), QCoreApplication.translate("pipboy", u"AID", None))

        __sortingEnabled5 = self.ammo_list.isSortingEnabled()
        self.ammo_list.setSortingEnabled(False)
        ___qlistwidgetitem39 = self.ammo_list.item(0)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("pipboy", u"\u041f\u0430\u0442\u0440\u043e\u043d \u043a\u0430\u043b\u0438\u0431\u0440\u0430 .44 \u00ab\u041c\u0430\u0433\u043d\u0443\u043c\u00bb(60)", None));
        ___qlistwidgetitem40 = self.ammo_list.item(1)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("pipboy", u"\u041f\u0430\u0442\u0440\u043e\u043d \u043a\u0430\u043b\u0438\u0431\u0440\u0430 .45-70(60)", None));
        ___qlistwidgetitem41 = self.ammo_list.item(2)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("pipboy", u"\u041f\u0430\u0442\u0440\u043e\u043d \u043a\u0430\u043b\u0438\u0431\u0440\u0430 .308(60)", None));
        self.ammo_list.setSortingEnabled(__sortingEnabled5)

        self.ammo_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><br/></p></body></html>", None))
        self.ammo_weight_label.setText(QCoreApplication.translate("pipboy", u"\u0412\u0415\u0421 0.043", None))
        self.ammo_cost_label.setText(QCoreApplication.translate("pipboy", u"\u0421\u0422\u041e 2", None))
        self.inv_tab.setTabText(self.inv_tab.indexOf(self.ammo), QCoreApplication.translate("pipboy", u"AMMO", None))
        self.weight.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p>69/250</p></body></html>", None))
        self.weight_img.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><img src=\":/futter/image/weight.png\"/></p></body></html>", None))
        self.cup_img.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><img src=\":/futter/image/cap.png\"/></p></body></html>", None))
        self.cup.setText(QCoreApplication.translate("pipboy", u"5000", None))
        self.inv_space.setText("")
        self.main_tab.setTabText(self.main_tab.indexOf(self.inv), QCoreApplication.translate("pipboy", u"INV", None))
        self.data_footer.setText("")

        __sortingEnabled6 = self.data_list.isSortingEnabled()
        self.data_list.setSortingEnabled(False)
        ___qlistwidgetitem42 = self.data_list.item(0)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("pipboy", u"Happy Birthday", None));
        ___qlistwidgetitem43 = self.data_list.item(1)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("pipboy", u"\u0414\u0435\u043d\u044c \u0438\u0433\u0440 ", None));
        ___qlistwidgetitem44 = self.data_list.item(2)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("pipboy", u"\u0414\u0435\u0442\u0438 \u0438\u0437 \u0442\u043e\u0432\u0430\u0440\u043d\u044f\u043a\u0430", None));
        ___qlistwidgetitem45 = self.data_list.item(3)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("pipboy", u"\u0423\u0431\u0435\u0436\u0438\u0449\u0435 84", None));
        ___qlistwidgetitem46 = self.data_list.item(4)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("pipboy", u"\u0418\u0414\u0418\u041e\u041e\u041e\u041e\u0422!!!", None));
        ___qlistwidgetitem47 = self.data_list.item(5)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("pipboy", u"\u0428\u0443\u0442 \u0433\u043e\u0440\u043e\u0445\u043e\u0432\u044b\u0439", None));
        ___qlistwidgetitem48 = self.data_list.item(6)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("pipboy", u"\u0412 \u0431\u043b\u0430\u0433\u043e\u0440\u043e\u0434\u0441\u0442\u0432\u043e \u0438\u0433\u0440\u0430\u0442\u044c \u043d\u0435 \u0431\u0443\u0434\u0435\u043c", None));
        ___qlistwidgetitem49 = self.data_list.item(7)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("pipboy", u"\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0435 \u0430\u0433\u0435\u043d\u0442\u0441\u0442\u0432\u043e \u041b.\u0421. \u041a\u0435\u043d\u043d\u0435\u0434\u0438", None));
        self.data_list.setSortingEnabled(__sortingEnabled6)

        self.data_description.setHtml(QCoreApplication.translate("pipboy", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto Mono'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u25a1 \u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u0434\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0441 \u0440\u043e\u0434\u043d\u044b\u043c\u0438, \u0431\u043b\u0438\u0437\u043a\u0438\u043c\u0438 \u0438 \u0434\u0440\u0443\u0437\u044c\u044f\u043c\u0438<br />\u25a0 (\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e) \u043f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u0447\u043d\u044b\u0439 \u0441\u0442\u0440\u0438\u043c</p></body></html>", None))
        self.data_description.setPlaceholderText("")
        self.main_tab.setTabText(self.main_tab.indexOf(self.data), QCoreApplication.translate("pipboy", u"DATA", None))
        self.map_image.setText(QCoreApplication.translate("pipboy", u"<html><head/><body><p><img src=\":/map/image/map.png\"/></p></body></html>", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.map), QCoreApplication.translate("pipboy", u"MAP", None))

        __sortingEnabled7 = self.radio_list.isSortingEnabled()
        self.radio_list.setSortingEnabled(False)
        ___qlistwidgetitem50 = self.radio_list.item(0)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("pipboy", u"Fallout: New Vegas", None));
        ___qlistwidgetitem51 = self.radio_list.item(1)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("pipboy", u"\u041c\u0443\u0437\u044b\u043a\u0430 \u041c\u043e\u0445\u0430\u0432\u0435", None));
        ___qlistwidgetitem52 = self.radio_list.item(2)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("pipboy", u"\u041d\u044c\u044e-\u0412\u0435\u0433\u0430\u0441", None));
        self.radio_list.setSortingEnabled(__sortingEnabled7)

        self.map_footer.setText("")
        self.main_tab.setTabText(self.main_tab.indexOf(self.radio), QCoreApplication.translate("pipboy", u"RADIO", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab), "")
    # retranslateUi

