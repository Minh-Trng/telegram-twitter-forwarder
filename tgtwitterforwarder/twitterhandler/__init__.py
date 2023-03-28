from helium import *
from tgtwitterforwarder import config


def start_driver():
    start_chrome('twitter.com', headless=bool(config.general_params["HEADLESS_BROWSER"]))
    __login_if_necessary()


def __login_if_necessary():
    if len(find_all(Link("Log in"))) > 0:
        click("Log in")
        #text field hint starts with "Phone"
        write(config.general_params["TWITTER_USERNAME"], into='Phone')
        press(ENTER)
        write(config.general_params["TWITTER_PASSWORD"], into='Password')
        press(ENTER)


def send_tweet(message):
    write(message, into="What’s happening?")
    click("Tweet")
    try:
        wait_until(Link("View").exists)
    except:
        go_to("twitter.com") # hoping that popup is gone
        return False
    return True


def __try_dismiss_alert():
    """
    NOTE: does not work as expected
    TODO need other way to get rid of popups
    dismiss alerts if there are any
    :return:
    """
    try:
        Alert().dismiss()
    except:
        return
