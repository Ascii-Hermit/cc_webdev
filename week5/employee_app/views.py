from django.shortcuts import render
from datetime import datetime, timedelta
from .forms import PromotionForm

def check_promotion(request):
    result = None

    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            date_of_joining = form.cleaned_data['date_of_joining']
            experience = datetime.today().date() - date_of_joining
            result = "YES" if experience.days >= 5 * 365 else "NO"
    else:
        form = PromotionForm()

    return render(request, 'promotion_form.html', {'form': form, 'result': result})
