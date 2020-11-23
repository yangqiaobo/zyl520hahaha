#史波克游戏
#作者：杨乔博
#日期：2020/11/23
import random
def name_to_number(name):
    if name=="石头":
        player_choice_number=0
        return player_choice_number
    elif name=="史波克":
        player_choice_number=1
        return player_choice_number
    elif name=="纸":
        player_choice_number=2
        return player_choice_number
    elif name=="蜥蜴":
        player_choice_number=3
        return player_choice_number
    else:
        player_choice_number=4
        return player_choice_number
def number_to_name(number):
    if number==0:
        number="石头"
        return number
    elif number==1:
        number="史波克"
        return number
    elif number==2:
        number="纸"
        return number
    elif number==3:
        number="蜥蜴"
        return number
    else:
        number="剪刀"
        return number
def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    jisuanji=number_to_name(comp_number)
    print("计算机的选择是%s"%(jisuanji))
    if comp_number==player_choice_number:
        print("您和计算机出的一样呢")
    elif player_choice_number==0:
        if comp_number==3 or comp_number==4:
            print("您赢了")
        else:
            print("您输了")
    elif player_choice_number==1:
        if comp_number==0 or comp_number==4:
            print("您赢了")
        else:
            print("您输了")
    elif player_choice_number==2:
        if comp_number==0 or comp_number==1:
            print("您赢了")
        else:
            print("您输了")
    elif player_choice_number==3:
        if comp_number==1 or comp_number==2:
            print("您赢了")
        else:
            print("您输了")
    else:
        if comp_number==2 or comp_number==3:
            print("您赢了")
        else:
            print("您输了")
print("欢迎使用RPSLS游戏")
print("_________________")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)

