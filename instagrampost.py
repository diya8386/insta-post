client = Client()
username = "team22testaccountproject"
password = "Linux_World22"
client.login(username, password)
# This line might be the reason for error
# kyonki hum raw string shayad nahi de pa rahe hain
post_caption = "manicure poop routine"
media_id = client.photo_upload("google.png", caption=post_caption).pk
client.photo_publish(media_id)
