from .account import Account
from .followers import Followers
from posts import Posts

from .env import USERNAME, PASSWORD
from .drivers import driver_desktop, driver_mobile

username = USERNAME
password = PASSWORD

acc = Account(username, password, driver_desktop, driver_mobile)
fol = Followers(driver_desktop)
posts = Posts(driver_mobile)

acc.login_desktop()

fol.unfollow_target_users(50, 3600)

img = r"\uil.jpg"
posts.send_post(img, "O bot Funciona!!!", [
                "#bottest", "#bot", "#test", "#amongus"])
