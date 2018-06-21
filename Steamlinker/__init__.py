import ts3lib, ts3defines, devtools
from ts3plugin import ts3plugin
from json import loads
from PythonQt.QtCore import Qt, QUrl
from PythonQt.QtGui import QMessageBox, QDialog, QDesktopServices
from PythonQt.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class testplugin(ts3plugin):
    name = "Steamlinker"
    requestAutoload = False
    version = "1.0.3"
    apiVersion = 21
    author = "Galtrox"
    description = "Steamlinker, adds a feature in to teamspeak 3 where you can click a steam link and it would open in your steam client instead of your default browser."
    offersConfigure = False
    commandKeyword = ""
    infoTitle = ""
    menuItems = []
    hotkeys = []
    domains = [
        "steamcommunity.com",
        "store.steampowered.com"
    ]
    updateurl = "https://raw.githubusercontent.com/Galtrox/Steamlinker/master/version.json"
    repourl = "https://github.com/{}/{}".format(author, name)

    def __init__(self):
        ts3lib.printMessageToCurrentTab("Steamlinker " + self.version + " loaded")
        self.nwmc = QNetworkAccessManager()
        self.nwmc.connect("finished(QNetworkReply*)", self.updateReply)
        self.nwmc.get(QNetworkRequest(QUrl(self.updateurl)))

    def updateReply(self, reply):
        version = loads(reply.readAll().data().decode('utf-8'))["version"]
        if version != self.version:
            x = QDialog()
            x.setAttribute(Qt.WA_DeleteOnClose)
            _x = QMessageBox.question(x, "{} v{} by {}".format(self.name, self.version, self.author), "New version v{} of Steamlinker found, do you want to update now?".format(version), QMessageBox.Yes, QMessageBox.No)
            if _x == QMessageBox.Yes:
                QDesktopServices.openUrl(QUrl(self.repourl))

    #This was a ugly way of doing it but fuck it for now :)
    def onTextMessageEvent(self, schid, targetMode, toID, fromID, fromName, fromUniqueIdentifier, message, ffIgnored):
        for url in self.domains:
            if url in message:
                ts3lib.printMessageToCurrentTab("[URL=steam://openurl/" + message[5:-6] + "]Open in Steam.[/URL]")
                return
