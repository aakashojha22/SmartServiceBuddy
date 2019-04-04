from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, ClientRequest, timestamp):
        return (
            six.text_type(ClientRequest.pk) + six.text_type(timestamp)
        )
email_verification = TokenGenerator()
