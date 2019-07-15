from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLabel,QScrollArea)
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPainter, QPixmap,QFont,QPalette,QColor

text="""
    秦孝公据崤函之固，拥雍州之地，君臣固守以窥周室，有席卷天下，包举宇内，囊
括四海之意，并吞八荒之心。当是时也，商君佐之，内立法度，务耕织，修守战之具，
外连衡而斗诸侯。于是秦人拱手而取西河之外。 
    孝公既没，惠文、武、昭襄蒙故业，因遗策，南取汉中，西举巴、蜀，东割膏腴之
地，北收要害之郡。诸侯恐惧，会盟而谋弱秦，不爱珍器重宝肥饶之地，以致天下之士
，合从缔交，相与为一。当此之时，齐有孟尝，赵有平原，楚有春申，魏有信陵。此四
君者，皆明智而忠信，宽厚而爱人，尊贤而重士，约从离衡，兼韩、魏、燕、楚、齐、
赵、宋、卫、中山之众。于是六国之士，有宁越、徐尚、苏秦、杜赫之属为之谋，齐明、
周最、陈轸、召滑、楼缓、翟景、苏厉、乐毅之徒通其意，吴起、孙膑、带佗、倪良、
王廖、田忌、廉颇、赵奢之伦制其兵。尝以十倍之地，百万之众，叩关而攻秦。秦人开
关延敌，九国之师，逡巡而不敢进。秦无亡矢遗镞之费，而天下诸侯已困矣。于是从散
约败，争割地而赂秦。秦有余力而制其弊，追亡逐北，伏尸百万，流血漂橹；因利乘便，
宰割天下，分裂山河。强国请服，弱国入朝。 
    延及孝文王、庄襄王，享国之日浅，国家无事。 
    及至始皇，奋六世之余烈，振长策而御宇内，吞二周而亡诸侯，履至尊而制六合，
执敲扑而鞭笞天下，威振四海。南取百越之地，以为桂林、象郡；百越之君，俯首系颈，
委命下吏。乃使蒙恬北筑长城而守藩篱，却匈奴七百余里；胡人不敢南下而牧马，士不
敢弯弓而报怨。于是废先王之道，焚百家之言，以愚黔首；隳名城，杀豪杰；收天下之
兵，聚之咸阳，销锋镝，铸以为金人十二，以弱天下之民。然后践华为城，因河为池，
据亿丈之城，临不测之渊，以为固。良将劲弩守要害之处，信臣精卒陈利兵而谁何。天
下已定，始皇之心，自以为关中之固，金城千里，子孙帝王万世之业也。 
    始皇既没，余威震于殊俗。然陈涉瓮牖绳枢之子，氓隶之人，而迁徙之徒也；才能
不及中人，非有仲尼，墨翟之贤，陶朱、猗顿之富；蹑足行伍之间，而倔起阡陌之中，
率疲弊之卒，将数百之众，转而攻秦；斩木为兵，揭竿为旗，天下云集响应，赢粮而景
从。山东豪俊遂并起而亡秦族矣。 
    且夫天下非小弱也，雍州之地，崤函之固，自若也。陈涉之位，非尊于齐、楚、燕、
赵、韩、魏、宋、卫、中山之君也；锄櫌棘矜，非铦于钩戟长铩也；谪戍之众，非抗于九
国之师也；深谋远虑，行军用兵之道，非及向时之士也。然而成败异变，功业相反，何也？
试使山东之国与陈涉度长絜大，比权量力，则不可同年而语矣。然秦以区区之地，致万乘
之势，序八州而朝同列，百有余年矣；然后以六合为家，崤函为宫；一夫作难而七庙隳，
身死人手，为天下笑者，何也？仁义不施而攻守之势异也。 
"""

class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initHPW()

    def initHPW(self):
        #设置标题
        title = QLabel("帮助文档")
        #title.setStyleSheet("color:white")
        titlefont = QtGui.QFont('楷体', 24)
        titlefont.setBold(True)
        title.setFont(titlefont)
        #设置返回按钮
        quitbutn_hpw = QPushButton("返回")
        quitbutn_hpw.clicked.connect(self.close)
        #文本
        self.tlabel=QLabel()
        self.tlabel.setText(text)
        self.tlabel.setFont(QFont("宋体", 16))
        self.setStyleSheet("QLabel{background:white;}")
        #
        myscroll=QScrollArea()
        myscroll.setWidget(self.tlabel)
        #设置布局
        titlehbox = QHBoxLayout()
        titlehbox.addStretch(1)
        titlehbox.addWidget(title)
        titlehbox.addStretch(1)

        labelhbox=QHBoxLayout()
        labelhbox.addWidget(myscroll)


        endhbox = QHBoxLayout()
        endhbox.addStretch(1)
        endhbox.addWidget(quitbutn_hpw)

        vbox = QVBoxLayout()
        vbox.addLayout(titlehbox)
        vbox.addLayout(labelhbox)
        vbox.addLayout(endhbox)

        self.setLayout(vbox)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(888, 648)
        self.setWindowTitle('教程')
        self.center()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("..//gesmuse_resources//image//chidback.jpg")
        painter.drawPixmap(self.rect(), pixmap)
