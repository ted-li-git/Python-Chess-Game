import tkinter as tk
from tkinter import messagebox, font

# 初始化棋盘
board = [" " for _ in range(9)]

# 检查胜利条件
def check_win(player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 横行
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 竖列
        (0, 4, 8), (2, 4, 6)              # 对角线
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# 检查平局
def check_draw():
    return " " not in board

# 更新棋盘
def update_board(index, player):
    board[index] = player
    buttons[index].config(text=player, state="disabled")

# 玩家点击按钮
def on_click(index):
    if board[index] == " ":
        update_board(index, current_player.get())
        if check_win(current_player.get()):
            messagebox.showinfo("游戏结束", f"玩家 {current_player.get()} 获胜！")
            reset_board()
        elif check_draw():
            messagebox.showinfo("游戏结束", "平局！")
            reset_board()
        else:
            switch_player()

# 切换玩家
def switch_player():
    if current_player.get() == "X":
        current_player.set("O")
    else:
        current_player.set("X")

# 重置棋盘
def reset_board():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal", bg="SystemButtonFace")
    current_player.set("X")
    status_label.config(text=f"当前玩家: {current_player.get()}")

# 创建游戏开始界面
def create_start_window():
    global start_window
    start_window = tk.Toplevel(root)
    start_window.title("游戏开始")
    start_window.geometry("200x100")

    start_button = tk.Button(start_window, text="开始游戏", command=start_game)
    start_button.pack(pady=20)

# 游戏开始界面
def start_game():
    start_window.destroy()  # 销毁开始窗口
    root.deiconify()  # 显示主游戏窗口
    status_label.config(text=f"当前玩家: {current_player.get()}")

# 创建主窗口
root = tk.Tk()
root.title("井字棋")
root.geometry("300x350")
root.withdraw()  # 隐藏主窗口，直到游戏开始

# 设置字体
custom_font = font.Font(family="Arial", size=24, weight="bold")

# 创建按钮
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=custom_font, width=5, height=2,
                       command=lambda i=i: on_click(i), bg="SystemButtonFace")
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# 当前玩家
current_player = tk.StringVar()
current_player.set("X")

# 创建重置按钮
reset_button = tk.Button(root, text="重置", font=custom_font, command=reset_board, bg="lightblue")
reset_button.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

# 创建状态标签
status_label = tk.Label(root, text="当前玩家: X", font=("Arial", 16))
status_label.grid(row=4, column=0, columnspan=3, pady=10)

# 创建游戏开始界面
create_start_window()

# 运行主循环
root.mainloop()