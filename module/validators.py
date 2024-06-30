from rest_framework.serializers import ValidationError


class YoutubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_url = dict(value).get(self.field)
        if video_url and not video_url.startswith("https://www.youtube.com/watch?v="):
            raise ValidationError("Недопустимая ссылка на видео.")
