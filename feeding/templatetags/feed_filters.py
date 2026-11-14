from django import template

register = template.Library()


@register.filter(name='feed_status')
def feed_status(feed):
    if feed.is_completed:
        if feed.completed_date:
            return f"Completed ({feed.completed_date.strftime('%d-%m-%Y')})"
        return "Completed"
    return "Pending"


@register.filter(name='status_color')
def status_color(is_completed):
    return "success" if is_completed else "warning"