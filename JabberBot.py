
import logging
import sleekxmpp
import API

from API import Help
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout

"""def Help(body):
    for words in body:
        if words == "Help" or words == "help":
            X = "What do you need help with? Right now all I do is ask if you need help. \n Hopefully soon I will be able to do more than this."
            return X"""

class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # If you wanted more functionality, here's how to register plugins:
        # self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0199') # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()
        
        
 

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            if msg['body'] == "Hello" or msg['body'] == "hello":
                self.send_message(msg['from'], "Hello, How are you?", mtype = 'chat').send()
                
            #msg.reply("Thanks for sending\n%(body)s" % msg).send()
            msg_str = msg['body']
            msg_split = msg_str.split(None)
            X = Help.Help(msg_split)
            
            self.send_message(msg['from'], X , mtype = 'chat')
            """for words in msg_split:
                #self.send_message(msg['from'], words, mtype = 'chat')
                if words == "Help" or words == "help":
                    self.send_message(msg['from'], "What do you need help with?", mtype = 'chat')
                if words == "The" or words == "the":
                    self.send_message(msg['from'],"Don't you dare tell me about a cow", mtype = 'chat')"""

if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = EchoBot('sigil@sudopriest.com', 'test001')
    xmpp.connect()
    xmpp.process(block=True)