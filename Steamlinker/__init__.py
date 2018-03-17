from ts3plugin import ts3plugin
import ts3lib, ts3defines
import devtools


class testplugin(ts3plugin):
    name = "Steamlinker"
    requestAutoload = False
    version = "1.0.2"
    apiVersion = 21
    author = "Galtrox"
    description = "Steamlinker, adds a feature in to teamspeak 3 where you can click a steam link and it would open in your steam client instead of your default browser."
    offersConfigure = False
    commandKeyword = ""
    infoTitle = ""
    menuItems = []#[(ts3defines.PluginMenuType.PLUGIN_MENU_TYPE_CLIENT, 0, "text", "icon.png")]
    hotkeys = []#[("keyword", "description")]
    devTools = devtools.installedPackages()
    number = len(devTools)
    link1 = "steamcommunity.com"
    link2 = "store.steampowered.com"


    def __init__(self):
        ts3lib.printMessageToCurrentTab("Steamlinker " + self.version + " loaded")
        for i in range(self.number):
            name = self.devTools[i]['name']
            if name == "requests":
                ts3lib.printMessageToCurrentTab("Yay! eveything is installed :)")
                break
        else:
            from devtools import PluginInstaller
            PluginInstaller().installPackages(['requests'])
            ts3lib.printMessageToCurrentTab("I've downloaded everything you need :D")
            ts3lib.printMessageToCurrentTab("post them steam links!")

    #This was a ugly way of doing it but fuck it for now :)
    def onTextMessageEvent(self, schid, targetMode, toID, fromID, fromName, fromUniqueIdentifier, message, ffIgnored):
        import requests
        response = requests.get("https://raw.githubusercontent.com/Galtrox/Steamlinker/master/version.json")
        dataN = response.json()
        MainData = dataN["version"]
        if self.version >= MainData and self.link1 in message:
            ts3lib.printMessageToCurrentTab("[URL=steam://openurl/" + message[5:-6] + "]Open in Steam.[/URL]")
        else:
            if self.link1 in (message):
                ts3lib.printMessageToCurrentTab("[URL=steam://openurl/" + message[5:-6] + "]Open in Steam.[/URL] [URL=https://github.com/Galtrox/Steamlinker/releases][COLOR=#ef0000]New version of steamlinker is out[/COLOR][/URL] ")
            else:
                if self.version >= MainData and self.link2 in message:
                    ts3lib.printMessageToCurrentTab("[URL=steam://openurl/" + message[5:-6] + "]Open in Steam.[/URL]")
                else:
                    if self.link2 in (message):
                        ts3lib.printMessageToCurrentTab("[URL=steam://openurl/" + message[5:-6] + "]Open in Steam.[/URL] [URL=https://github.com/Galtrox/Steamlinker/releases][COLOR=#ef0000]New version of steamlinker is out[/COLOR][/URL] ")