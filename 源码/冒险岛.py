# 定义玩家和坐骑的起始位置
player_position = [0, 0]
mount_position = [0, 0]

# 定义坐骑类型
mount_type = "火龙"

# 定义移动玩家和坐骑的函数


def move(direction, distance):
    if direction == "上":
        player_position[1] += distance
        mount_position[1] += distance
    elif direction == "下":
        player_position[1] -= distance
        mount_position[1] -= distance
    elif direction == "左":
        player_position[0] -= distance
        mount_position[0] -= distance
    elif direction == "右":
        player_position[0] += distance
        mount_position[0] += distance

# 定义检查玩家和坐骑是否在同一位置的函数


def check_collision():
    if player_position == mount_position:
        return True
    else:
        return False

# 定义开始游戏的函数


def start_game():
    print("欢迎来到冒险岛！")
    print("你的初始坐骑是", mount_type)
    print("使用箭头键移动你的角色。")
    print("尝试在不与你的坐骑碰撞的情况下到达关卡的终点。")
    print("祝你好运！")
    while True:
        direction = input("输入一个方向（上、下、左、右）：")
        move(direction, 1)
        if check_collision():
            print("你与你的坐骑碰撞了！游戏结束。")
            break
        elif player_position == [9, 9]:
            print("恭喜你！你到达了关卡的终点。")
            break


# 调用start_game函数开始游戏
start_game()
