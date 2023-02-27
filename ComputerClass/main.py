import platform
import time as tm

class Computer():
    def __init__(self, maindashboard_name=platform.node(), computer_os=platform.system(),
                 computer_os_version=platform.release(), computer_progressor=platform.processor(),
                 microsoft_acc_password="00729400", computer_SSD_letterpath="C", computer_second_StorageUnit=None):

        self.maindashboard_name = maindashboard_name
        self.computer_os = computer_os
        self.computer_progressor = computer_progressor
        self.microsoft_acc_password = microsoft_acc_password
        self.computer_SSD_letterpath = computer_SSD_letterpath
        self.computer_second_StorageUnit = computer_second_StorageUnit
        print("System/Computer starting...")
        tm.sleep(2)
        print("System/Logging in...")
        tm.sleep(1)
        print("Welcome", maindashboard_name)

    def about_mycomputer(self):
        print("ABOUT MY COMPUTER")
        print("------------------")
        print("PC name:", self.maindashboard_name)
        print("PC Operating System:", self.computer_os, platform.release())
        print("PC Progressor:", self.computer_progressor)
        print("Microsoft Account Password:", self.microsoft_acc_password)
        print("Storage Path (1th unit):", self.computer_SSD_letterpath)
        print("Storage Path (2th unit):", self.computer_second_StorageUnit)

    def change_dashboard_name(self):
        new_dashboard_name = input("Please enter new dashboard's name:")
        print("System/Settings updating...")
        tm.sleep(2.5)
        caution_message = input("Your computer name show as {} do you allow? (Y/N)".format(new_dashboard_name))
        if(caution_message == "Y"):
            self.maindashboard_name = new_dashboard_name
            print("PC name:",self.maindashboard_name)
        else:
            print("System/Please try again")

    def update_win_to_version11(self):
        win11keys = ["A269N-WFGWX-YVC9B-4J6C9-T83GX","ZK7JG-NPHTM-C97JM-9MPGT-3V66T","Q269N-WFGWX-YVC9B-4J6C9-T83GX"]
        win11keyI = input("Please enter your win11 key first:")
        for keys in win11keys:
            if(win11keyI == keys): #here, system try match to keys
                allowing_message = input("Win(ver10) > Win(ver11) (Y/N)")
                if(allowing_message == "Y"):
                    print("System/Please wait...")
                    tm.sleep(3)
                    print("System/Downloading...")
                    tm.sleep(4)
                    print("System/Settings updating...")
                    tm.sleep(2)
                    print("Downloading successfull!")
                    print("Win version: 11")
                else:
                    print("Downloading failed")
                    break
    def down_win_to_version7(self):
        win7keys = ["BKLM-SSJH-YVC9B-4J6C9-T83GX", "ZK7JG-QQLP-C97JM-9MPGT-3V66T", "Q269N-WFGWX-YVC9B-4J6C9-T83GX"]
        win7keyI = input("Please enter your win7 key first:")
        for keys in win7keys:
            if (win7keyI == keys):  # here, system try match to keys
                allowing_message = input("Win(ver10) > Win(ver7) (Y/N)")
                if (allowing_message == "Y"):
                    print("System/Please wait...")
                    tm.sleep(3)
                    print("System/Downloading...")
                    tm.sleep(4)
                    print("System/Settings updating...")
                    tm.sleep(2)
                    print("Downloading successfull!")
                    print("Win version: 7")
                else:
                    print("Downloading failed")
                    break

Computer = Computer()
Computer.down_win_to_version7()
    if
