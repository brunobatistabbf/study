class App:
    def start(self):
        print("Starting")

class Android(App):
    def getVersion(self):
        print("android version")

app = Android()
app.start()
app.getVersion()



