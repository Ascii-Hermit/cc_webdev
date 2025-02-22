from django import forms
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import base64

class CaptchaForm(forms.Form):
    user_input = forms.CharField(label="Enter Captcha", max_length=6)

    def generate_captcha_text(self):
        """Generate a random 6-character captcha text."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def generate_captcha_image(self, captcha_text):
        """Create an image of the captcha text."""
        image = Image.new('RGB', (150, 50), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((20, 15), captcha_text, fill=(0, 0, 0), font=font)

        # Save image to a buffer
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue()).decode()

    def get_captcha(self):
        """Generate and return captcha text and its image."""
        captcha_text = self.generate_captcha_text()
        captcha_image = self.generate_captcha_image(captcha_text)
        return captcha_text, captcha_image
