import os
auction_logo='''                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\  '''
print(auction_logo)
print("Vítejte v programu pro tichou dražbu")
bidder_list2={}
bidder_list2[input("Zadejte jméno:\n")]=(int(input("Zadejte částku v bahamských dolarech (BSD):\n")))
    
continuation = "ano"
while continuation == "ano":

    continuation = input("Jsou další nabízející? Napište ano nebo ne.\n")
    
    if continuation == "ne":
        os.system("cls")

def bída_max(bidder_dict):
    hi_bid = 0
    winner = ""
    for key in bidder_dict:
        if hi_bid<(bidder_dict[key]):
            hi_bid= bidder_dict[key]
            winner = key
    print(f"Aukci vyhrál {winner} s nabídkou {hi_bid} dolarů")
bída_max(bidder_list2)
