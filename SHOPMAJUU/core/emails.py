from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_invoice_email(invoice):
    pkg = invoice.package
    subject = f"Invoice for package {pkg.tracking_number}"
    ctx = {"invoice": invoice, "package": pkg}

    # ✅ Correct function name
    text = render_to_string("emails/invoice_email.txt", ctx)
    html = render_to_string("emails/invoice_email.html", ctx)

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[pkg.user.email],
    )
    msg.attach_alternative(html, "text/html")
    msg.send()
