import irc.client

class Connection(irc.client.SimpleIRCClient):
    def __init__(self, target):
        irc.client.SimpleIRCClient.__init__(self)
        self.target = target

    def on_welcome(self, connection, event):
        if irc.client.is_channel(self.target):
            connection.join(self.target)
        else:
            self.send_it()

    def on_join(self, connection, event):
        self.send_it()

    # def on_disconnect(self, connection, event):
    #     sys.exit(0)

    def send_it(self):
        # while 1:
        #     line = "sys.stdin.readline().strip()"
        #     if not line:
        #         break
        self.connection.privmsg(self.target, "Hello")
        self.connection.quit("Using irc.client.py")

    

    

