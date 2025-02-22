from django.shortcuts import render
from .forms import CaptchaForm

def captcha_view(request):
    if "attempts" not in request.session:
        request.session["attempts"] = 0

    form = CaptchaForm()
    captcha_text, captcha_image = form.get_captcha()
    request.session["captcha_text"] = captcha_text

    message = ""
    disabled = False

    if request.method == "POST":
        user_input = request.POST.get("user_input", "").strip().upper()
        stored_captcha = request.session.get("captcha_text", "")

        if request.session["attempts"] >= 3:
            disabled = True
            message = "Too many failed attempts. Textbox disabled."
        else:
            if user_input == stored_captcha:
                message = "✅ Correct! You passed the captcha."
                request.session["attempts"] = 0  # Reset attempts on success
            else:
                request.session["attempts"] += 1
                message = f"❌ Incorrect! Attempts left: {3 - request.session['attempts']}"

            if request.session["attempts"] >= 3:
                disabled = True

    return render(request, "captcha_app/captcha.html", {
        "form": form,
        "captcha_image": captcha_image,
        "message": message,
        "disabled": disabled
    })
