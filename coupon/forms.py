from django import forms


class AddCouponForm(forms.Form):
    code = forms.CharField(label='Input Coupon Code')
