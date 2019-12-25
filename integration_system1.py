import weather_system
import ebdm_system

class IntegrationSystem1:
    def __init__(self):
        # 二つのシステムを初期化する
        self.system1 = weather_system.AimlSystem()
        self.system2 = ebdm_system.EbdmSystem()

    def initial_message(self, input):
        # システムを全て初期化する
        self.system1.initial_message(input)
        self.system2.initial_message(input)
        return {'utt':'こんにちは。対話を始めましょう。', 'end':False}
        
    def reply(self, input):
        # 特定のキーワードが入っていたら，system1を，それ以外の場合はsystem2を呼びだす
        if '天気' in input['utt']:
            return self.system1.reply(input)
        else:
            return self.system2.reply(input)

if __name__ == '__main__':
    systems = IntegrationSystem1()
    print("SYS> " + systems.initial_message({'utt': '', 'sessionId': ''})['utt'])
    while 1:
        text = input("> ")
        print("SYS> " + systems.reply({'utt': text, 'sessionId': ''})['utt'])