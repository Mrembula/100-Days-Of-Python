import internet_speed

download_speed = 20
upload_speed = 10

bot = internet_speed.InternetSpeedTwitterBot()
speed = bot.get_internet_speed()

isp_text = (f"Hey Internet Provider, why is my internet speed {speed[0]}down/{speed[1]}up "
            f"when I pay for {download_speed}down/{upload_speed}up?")

bot.tweet_at_provider(isp_text)
