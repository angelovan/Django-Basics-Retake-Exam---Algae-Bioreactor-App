from datetime import timedelta
from django import forms
from .models import NutrientFeed


class NutrientFeedForm(forms.ModelForm):
    class Meta:
        model = NutrientFeed
        fields = ['bioreactor', 'completed_date', 'is_completed', 'notes']
        widgets = {
            'bioreactor': forms.Select(attrs={'class': 'form-control'}),
            'completed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        bioreactor = cleaned_data.get('bioreactor')
        completed_date = cleaned_data.get('completed_date')

        if bioreactor and completed_date:
            interval_days = (
                bioreactor.algae_species.feed_interval_days
                if bioreactor.algae_species
                else 7
            )

            previous_feeds = NutrientFeed.objects.filter(
                bioreactor=bioreactor,
                completed_date__isnull=False
            )
            if self.instance.pk:
                previous_feeds = previous_feeds.exclude(pk=self.instance.pk)

            last_feed = previous_feeds.order_by('-completed_date').first()

            if last_feed:
                next_due_date = last_feed.due_date or (
                    last_feed.completed_date + timedelta(days=interval_days)
                )

                if completed_date < next_due_date:
                    formatted_date = next_due_date.strftime('%d-%b-%Y')
                    raise forms.ValidationError(
                        f"It is too early to feed this algae strain! This colony must be fed every "
                        f"{interval_days} days. The next scheduled feeding is on {formatted_date}."
                    )

        return cleaned_data