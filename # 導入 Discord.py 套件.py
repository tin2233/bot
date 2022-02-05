# 導入 Discord.py 套件
import discord
from discord.ext import commands 
import json

# 導入隨機數套件
import random

# 取得 Discord client 物件才能操作
client = discord.Client()
# 調用 event 函式庫
@client.event



# 當機器人完成啟動時在終端機顯示提示訊息
async def on_ready():
    print(f'目前登入身份：{client.user}')

# 調用 event 函式庫
@client.event
# 當有訊息時
async def on_message(message):
    
    # 排除機器人本身發出的訊息，避免機器人自問自答的無限迴圈
    if message.author == client.user:
        return

    # 預設錯誤訊息
    error = []

    # 處理輸入文字
    content = message.content.replace(' ', '').lower()

    # 如果是「!roll」開頭的訊息
    if message.content == '誰是機器人':
        await message.channel.send('誰叫我？')
    if message.content == '嘿':
        await message.channel.send('嗨')
    if message.content.startswith('!roll'):
        content = content.replace('!roll', '')

        # 骰子數量計算
        dice_cont = content.split('d')[0]

        try:
            dice_cont = int(dice_cont)

        except ValueError:
            error.append('How many dice you roll must be an interger!')

        # 骰子類型判斷
        content = content.split('d')[1]
        dice_type = content.split('>')[0]
        try:
            dice_type = int(dice_type)

        except ValueError:
            error.append('Dice type must be an interger!')

        # 成功判斷
        if '>' in content:
            success = content.split('>')[1]
            try:
                success = int(success)    
            except ValueError:
                error.append('Success condition must be an interger!')

        else:
            success = 0

        if len(error) == 0:
            success_count = 0
            result_msg = ''

            # 擲骰子
            results = [random.randint(1, dice_type) for _ in range(dice_cont)]

            for result in results:
                if success > 0 and result >= success:
                    success_count += 1
                result_msg += f'`{result}`, '
            
            await message.channel.send(result_msg)

            if success > 0:
                await message.channel.send(f'Success: `{success_count}`')
        else:
            await message.channel.send(error)


# TOKEN 在 Discord Developer 的「BOT」頁取得
client.run('OTM5NTA4MTEzODM5NjQ0Nzcy.Yf53HQ.0jKHyL-qSGxNcRAw97wsEaeBHz4')