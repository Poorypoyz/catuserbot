from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 19585788
    API_HASH = "59dfd4d2292eda33490c40a09ef224e9"
    # the name to display in your alive message
    ALIVE_NAME = "kdkdkxkpoory"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://extgjpiu:X3DweEr9RvatfCcT_NievXRwtyNnSXKz@otto.db.elephantsql.com/extgjpiu"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBuyvo03z7Uue-mOdnzAuYiRxkBSo9DCylogGrUKpa6sMrl9cEUkKyyv1gAtqR6R1BMT_UC4gD5s1C4woGRUd7myUxesIxr7MCVNtAanZnOYQGxW6dtvXjZa0tQz_g7zMkp9wo1jvZwtY3p3ZC8hl39KoUxwIKNRmGxniwVJjKv6Ro9NdjOeLncvvqbfHSC2k-tK2uahQOln_sdM6YTBcfdwSP9c2fWT4xp8qYF_10JC-3udoQ_qYS-TqUbAVZlLsjU1Owqn1jIc12nFfljvbGwBzBoOmpfjIEXeOKO45AUXU-1ogmNEp7KOiP4SEEORU2ZyAeT7qS3y_jIsSDhBE0lxM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5860655213:AAFAKzebV2eyFbtuOxbbDsWA5WjmBSgz1iM"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001849265388
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
