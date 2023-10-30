import time

class TV():

    def __init__(self,tv_status = "Turned Off",tv_volume = 0,channel_list = ["TRT"], channel = "TRT"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel
    def tv_open(self):
        if self.tv_status == "Turned On":
            print("TV is turned on already.")
        else: 
            print("TV is turning on... ")
            time.sleep(1)
            print("TV turned on")
            self.tv_status = "Turned On"
    def tv_close(self):
        if self.tv_status == "Turned Off":
            print("TV is turned off already.")
        else: 
            print("TV is turning off... ")
            time.sleep(1)
            print("TV turned off")
            self.tv_status = "Turned Off"
    def volume_settings(self):
        if self.tv_status == "Turned On":
            while True:
                select = input("For upping volume: '>'\nFor downing volume: '<'\nFor finish changing volume: 'q'")
                if select == '>':
                    if self.tv_volume != 100:
                        print("Volume is upping....")
                        self.tv_volume += 10
                        print("Ses: ", self.tv_volume)
                elif select == '<':
                    if self.tv_volume != 0:
                        print("Volume is downing....")
                        print("Ses: ", self.tv_volume)
                elif select == 'q':
                    break
        else: print("Please, turn on the TV for changing volume...")
    def adding_channel(self,channel_name):
        print("Channel is added", channel_name)
        time.sleep(1)
        self.channel_list.append(channel_name) 
    def changing_channel(self):
        print("You can select these channels", self.channel_list)
        selection = int(input("Select Channel: "))
        if selection <= len(self.channel_list):
            print("Channel is changing...")
            self.channel = self.channel_list[selection - 1]
            print("Channel is: ", self.channel)
    def __len__(self):
        return len(self.channel_list)
    def __str__(self):
        return "TV Status: {}, TV Volume: {}, Channel List: {}, Channel: {}".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)

control = TV()
print("""
TV Program

1.TV Turn On
2.TV Turn Off
3.Volume Settings
4.Add Channel
5.Number of Channels
6.Change Channel
7.TV Info
Press 'q' for closing program.
""")


while True:
    proccess = input("Select your proccess: ")
    if proccess == 'q':
        break
    elif proccess == '1':
        control.tv_open()
    elif proccess == '2':
        control.tv_close()
    elif proccess == '3':
        control.volume_settings()
    elif proccess == '4':
        channels = input("Enter names of channels separate by ','")
        new_channels = channels.split(",")
        for adds in new_channels:
            control.adding_channel(adds)
    elif proccess == '5':
        print("Number of channels: ", len(control))
    elif proccess == '6':
        control.changing_channel()
    elif proccess == '7':
        print(control)
    else: print("Invalid proccess")
