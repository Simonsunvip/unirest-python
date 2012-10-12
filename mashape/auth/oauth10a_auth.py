from mashape.auth.oauth_auth import OAuthAuth
from mashape.exception.client_exception import MashapeClientException
from mashape.exception.exception_messages import ExceptionMessages


class OAuth10aAuth(OAuthAuth):

    def __init__(self, consumer_key, consumer_secret, callback_url):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = None
        self.access_secret = None
        self.callback_url = callback_url

    def handle_headers(self, url):
        if not url.endswith("/oauth_url"):
            if self.access_token is None or self.access_secret is None:
                raise MashapeClientException(
                        ExceptionMessages.EXCEPTION_OAUTH1_AUTHORIZE)

        headers = {}
        headers["x-mashape-oauth-consumerkey"] = self.consumer_key
        headers["x-mashape-oauth-consumersecret"] = self.consumer_secret
        headers["x-mashape-oauth-accesstoken"] = self.access_token
        headers["x-mashape-oauth-accesssecret"] = self.access_secret
        return headers
